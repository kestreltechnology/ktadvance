/*
 * This file is part of Cleanflight.
 *
 * Cleanflight is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Cleanflight is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Cleanflight.  If not, see <http://www.gnu.org/licenses/>.
 */

/* ========================================================================== *
 * KT-Advance Workshop version                                                *
 * ========================================================================== */

// Inertial Measurement Unit (IMU)

/*
#include <stdbool.h>
#include <stdint.h>
#include <math.h>

#include "platform.h"

#include "build/build_config.h"
#include "build/debug.h"

#include "common/axis.h"

#include "pg/pg.h"
#include "pg/pg_ids.h"

#include "drivers/time.h"

#include "fc/runtime_config.h"

#include "flight/imu.h"
#include "flight/mixer.h"
#include "flight/pid.h"

#include "io/gps.h"

#include "sensors/acceleration.h"
#include "sensors/barometer.h"
#include "sensors/compass.h"
#include "sensors/gyro.h"
#include "sensors/sensors.h"

#if defined(SIMULATOR_BUILD) && defined(SIMULATOR_MULTITHREAD)
#include <stdio.h>
#include <pthread.h>

static pthread_mutex_t imuUpdateLock;

#if defined(SIMULATOR_IMU_SYNC)
static uint32_t imuDeltaT = 0;
static bool imuUpdated = false;
#endif

#define IMU_LOCK pthread_mutex_lock(&imuUpdateLock)
#define IMU_UNLOCK pthread_mutex_unlock(&imuUpdateLock)

#else

#define IMU_LOCK
#define IMU_UNLOCK

#endif

*/

#include "../flight_h.h"

#define NULL  ((void *)0)
#define false 0
#define true 1
#define bool _Bool
#define STATIC_UNIT_TESTED static

#define M_PIf 3.14159265358979323846f
#define XYZ_AXIS_COUNT 3

// the limit (in degrees/second) beyond which we stop integrating
// omega_I. At larger spin rates the DCM PI controller can get 'dizzy'
// which results in false gyro drift. See
// http://gentlenav.googlecode.com/files/fastRotations.pdf

#define SPIN_RATE_LIMIT 20

int32_t accSum[XYZ_AXIS_COUNT];

uint32_t accTimeSum = 0;        // keep track for integration of acc
int accSumCount = 0;
float accVelScale;

static float throttleAngleScale;
static float fc_acc;
static float smallAngleCosZ = 0;

static imuRuntimeConfig_t imuRuntimeConfig;

STATIC_UNIT_TESTED float rMat[3][3];

// quaternion of sensor frame relative to earth frame
// STATIC_UNIT_TESTED quaternion q = QUATERNION_INITIALIZE;
// STATIC_UNIT_TESTED quaternionProducts qP = QUATERNION_PRODUCTS_INITIALIZE;
static quaternion q = {.w=1, .x=0, .y=0,.z=0};
static quaternionProducts qP = {.ww=1, .wx=0, .wy=0, .wz=0, .xx=0, .xy=0, .xz=0, .yy=0, .yz=0, .zz=0};

// headfree quaternions
// quaternion headfree = QUATERNION_INITIALIZE;
// quaternion offset = QUATERNION_INITIALIZE;
quaternion headfree = {.w=1, .x=0, .y=0,.z=0};
quaternion offset = {.w=1, .x=0, .y=0,.z=0};

// absolute angle inclination in multiple of 0.1 degree    180 deg = 1800
// attitudeEulerAngles_t attitude = EULER_INITIALIZE;
attitudeEulerAngles_t attitude = { { 0, 0, 0 } };

/*
PG_REGISTER_WITH_RESET_TEMPLATE(imuConfig_t, imuConfig, PG_IMU_CONFIG, 0);

PG_RESET_TEMPLATE(imuConfig_t, imuConfig,
    .dcm_kp = 2500,                // 1.0 * 10000
    .dcm_ki = 0,                   // 0.003 * 10000
    .small_angle = 25,
    .accDeadband = {.xy = 40, .z= 40},
    .acc_unarmedcal = 1
);
*/

extern const imuConfig_t pgResetTemplate_imuConfig;
imuConfig_t imuConfig_System;
imuConfig_t imuConfig_Copy;
extern const pgRegistry_t imuConfig_Registry;
const pgRegistry_t imuConfig_Registry __attribute__ ((section(".pg_registry"), used, aligned(4))) = {
  .pgn = 22 | (0 << 12),
  .size = sizeof(imuConfig_t) | PGR_SIZE_SYSTEM_FLAG,
  .address = (uint8_t*)&imuConfig_System,
  .copy = (uint8_t*)&imuConfig_Copy,
  .ptr = 0,
  .reset = {.ptr = (void*)&pgResetTemplate_imuConfig}, };

const imuConfig_t pgResetTemplate_imuConfig __attribute__ ((section(".pg_resetdata"), used, aligned(2))) = { .dcm_kp = 2500,
  .dcm_ki = 0,
  .small_angle = 25,
  .accDeadband = {.xy = 40, .z= 40},									     .acc_unarmedcal = 1 };



static void imuComputeRotationMatrix(void){
    imuQuaternionComputeProducts(&q, &qP);

    rMat[0][0] = 1.0f - 2.0f * qP.yy - 2.0f * qP.zz;
    rMat[0][1] = 2.0f * (qP.xy + -qP.wz);
    rMat[0][2] = 2.0f * (qP.xz - -qP.wy);

    rMat[1][0] = 2.0f * (qP.xy - -qP.wz);
    rMat[1][1] = 1.0f - 2.0f * qP.xx - 2.0f * qP.zz;
    rMat[1][2] = 2.0f * (qP.yz + -qP.wx);

    rMat[2][0] = 2.0f * (qP.xz + -qP.wy);
    rMat[2][1] = 2.0f * (qP.yz - -qP.wx);
    rMat[2][2] = 1.0f - 2.0f * qP.xx - 2.0f * qP.yy;
}

/*
* Calculate RC time constant used in the accZ lpf.
*/
static float calculateAccZLowPassFilterRCTimeConstant(float accz_lpf_cutoff)
{
    return 0.5f / (M_PIf * accz_lpf_cutoff);
}

static float calculateThrottleAngleScale(uint16_t throttle_correction_angle)
{
    return (1800.0f / M_PIf) * (900.0f / throttle_correction_angle);
}

void imuConfigure(uint16_t throttle_correction_angle)
{
    imuRuntimeConfig.dcm_kp = imuConfig()->dcm_kp / 10000.0f;
    imuRuntimeConfig.dcm_ki = imuConfig()->dcm_ki / 10000.0f;
    imuRuntimeConfig.acc_unarmedcal = imuConfig()->acc_unarmedcal;
    imuRuntimeConfig.small_angle = imuConfig()->small_angle;

    fc_acc = calculateAccZLowPassFilterRCTimeConstant(5.0f); // Set to fix value
    throttleAngleScale = calculateThrottleAngleScale(throttle_correction_angle);
}

void imuInit(void)
{
    smallAngleCosZ = cos_approx(degreesToRadians(imuRuntimeConfig.small_angle));
    accVelScale = 9.80665f / acc.dev.acc_1G / 10000.0f;

    imuComputeRotationMatrix();
}

void imuResetAccelerationSum(void)
{
    accSum[0] = 0;
    accSum[1] = 0;
    accSum[2] = 0;
    accSumCount = 0;
    accTimeSum = 0;
}

static float invSqrt(float x)
{
    return 1.0f / sqrtf(x);
}

static bool imuUseFastGains(void)
{
  // return !ARMING_FLAG(ARMED) && millis() < 20000;
  return !(armingFlags & (ARMED)) && millis() < 20000;
}

static float imuGetPGainScaleFactor(void)
{
    if (imuUseFastGains()) {
        return 10.0f;
    }
    else {
        return 1.0f;
    }
}

static void imuMahonyAHRSupdate(float dt, float gx, float gy, float gz,
                                bool useAcc, float ax, float ay, float az,
                                bool useMag, float mx, float my, float mz,
                                bool useYaw, float yawError)
{
    static float integralFBx = 0.0f,  integralFBy = 0.0f, integralFBz = 0.0f;    // integral error terms scaled by Ki

    // Calculate general spin rate (rad/s)
    // const float spin_rate = sqrtf(sq(gx) + sq(gy) + sq(gz));
    const float spin_rate = sqrtf(((gx)*(gx)) + ((gy)*(gy)) + ((gz)*(gz)));

    // Use raw heading error (from GPS or whatever else)
    float ex = 0, ey = 0, ez = 0;
    if (useYaw) {
        while (yawError >  M_PIf) yawError -= (2.0f * M_PIf);
        while (yawError < -M_PIf) yawError += (2.0f * M_PIf);
        ez += sin_approx(yawError / 2.0f);
    }

    (void)(useMag);
    (void)(mx);
    (void)(my);
    (void)(mz);


    // Use measured acceleration vector
    // float recipAccNorm = sq(ax) + sq(ay) + sq(az);
    float recipAccNorm = ((ax)*(ax)) + ((ay)*(ay)) + ((az)*(az));
    if (useAcc && recipAccNorm > 0.01f) {
        // Normalise accelerometer measurement
        recipAccNorm = invSqrt(recipAccNorm);
        ax *= recipAccNorm;
        ay *= recipAccNorm;
        az *= recipAccNorm;

        // Error is sum of cross product between estimated direction and measured direction of gravity
        ex += (ay * rMat[2][2] - az * rMat[2][1]);
        ey += (az * rMat[2][0] - ax * rMat[2][2]);
        ez += (ax * rMat[2][1] - ay * rMat[2][0]);
    }

    // Compute and apply integral feedback if enabled
    if (imuRuntimeConfig.dcm_ki > 0.0f) {
        // Stop integrating if spinning beyond the certain limit
        // if (spin_rate < DEGREES_TO_RADIANS(SPIN_RATE_LIMIT)) {
      if (spin_rate < ((20) * 0.0174532925f)) {
            const float dcmKiGain = imuRuntimeConfig.dcm_ki;
            integralFBx += dcmKiGain * ex * dt;    // integral error scaled by Ki
            integralFBy += dcmKiGain * ey * dt;
            integralFBz += dcmKiGain * ez * dt;
        }
    } else {
        integralFBx = 0.0f;    // prevent integral windup
        integralFBy = 0.0f;
        integralFBz = 0.0f;
    }

    // Calculate kP gain. If we are acquiring initial attitude (not armed and within 20 sec from powerup) scale the kP to converge faster
    const float dcmKpGain = imuRuntimeConfig.dcm_kp * imuGetPGainScaleFactor();

    // Apply proportional and integral feedback
    gx += dcmKpGain * ex + integralFBx;
    gy += dcmKpGain * ey + integralFBy;
    gz += dcmKpGain * ez + integralFBz;

    // Integrate rate of change of quaternion
    gx *= (0.5f * dt);
    gy *= (0.5f * dt);
    gz *= (0.5f * dt);

    quaternion buffer;
    buffer.w = q.w;
    buffer.x = q.x;
    buffer.y = q.y;
    buffer.z = q.z;

    q.w += (-buffer.x * gx - buffer.y * gy - buffer.z * gz);
    q.x += (+buffer.w * gx + buffer.y * gz - buffer.z * gy);
    q.y += (+buffer.w * gy - buffer.x * gz + buffer.z * gx);
    q.z += (+buffer.w * gz + buffer.x * gy - buffer.y * gx);

    // Normalise quaternion
    // float recipNorm = invSqrt(sq(q.w) + sq(q.x) + sq(q.y) + sq(q.z));
    float recipNorm = invSqrt(((q.w)*(q.w)) + ((q.x)*(q.x)) + ((q.y)*(q.y)) + ((q.z)*(q.z)));
    q.w *= recipNorm;
    q.x *= recipNorm;
    q.y *= recipNorm;
    q.z *= recipNorm;

    // Pre-compute rotation matrix from quaternion
    imuComputeRotationMatrix();
}

STATIC_UNIT_TESTED void imuUpdateEulerAngles(void)
{
    quaternionProducts buffer;

    // if (FLIGHT_MODE(HEADFREE_MODE)) {
    if ((flightModeFlags & (HEADFREE_MODE))) {
       imuQuaternionComputeProducts(&headfree, &buffer);

       attitude.values.roll = lrintf(atan2_approx((+2.0f * (buffer.wx + buffer.yz)), (+1.0f - 2.0f * (buffer.xx + buffer.yy))) * (1800.0f / M_PIf));
       attitude.values.pitch = lrintf(((0.5f * M_PIf) - acos_approx(+2.0f * (buffer.wy - buffer.xz))) * (1800.0f / M_PIf));
       attitude.values.yaw = lrintf((-atan2_approx((+2.0f * (buffer.wz + buffer.xy)), (+1.0f - 2.0f * (buffer.yy + buffer.zz))) * (1800.0f / M_PIf)));
    } else {
       attitude.values.roll = lrintf(atan2_approx(rMat[2][1], rMat[2][2]) * (1800.0f / M_PIf));
       attitude.values.pitch = lrintf(((0.5f * M_PIf) - acos_approx(-rMat[2][0])) * (1800.0f / M_PIf));
       attitude.values.yaw = lrintf((-atan2_approx(rMat[1][0], rMat[0][0]) * (1800.0f / M_PIf)));
    }

    if (attitude.values.yaw < 0)
        attitude.values.yaw += 3600;

    // Update small angle state
    if (rMat[2][2] > smallAngleCosZ) {
      // ENABLE_STATE(SMALL_ANGLE);
      (stateFlags |= (SMALL_ANGLE));
    } else {
      // DISABLE_STATE(SMALL_ANGLE);
      (stateFlags &= ~(SMALL_ANGLE));
    }
}

static bool imuIsAccelerometerHealthy(void)
{
    float accMagnitude = 0;
    for (int axis = 0; axis < 3; axis++) {
        const float a = acc.accADC[axis];
        accMagnitude += a * a;
    }

    // accMagnitude = accMagnitude * 100 / (sq((int32_t)acc.dev.acc_1G));
    accMagnitude = accMagnitude * 100 / ((((int32_t)acc.dev.acc_1G)*((int32_t)acc.dev.acc_1G)));

    // Accept accel readings only in range 0.90g - 1.10g
    return (81 < accMagnitude) && (accMagnitude < 121);
}

static void imuCalculateEstimatedAttitude(timeUs_t currentTimeUs)
{
    static timeUs_t previousIMUUpdateTime;
    float rawYawError = 0;
    bool useAcc = false;
    bool useMag = false;
    bool useYaw = false;

    const timeDelta_t deltaT = currentTimeUs - previousIMUUpdateTime;
    previousIMUUpdateTime = currentTimeUs;

    if (imuIsAccelerometerHealthy()) {
        useAcc = true;
    }

    float gyroAverage[XYZ_AXIS_COUNT];
    gyroGetAccumulationAverage(gyroAverage);
    float accAverage[XYZ_AXIS_COUNT];
    if (!accGetAccumulationAverage(accAverage)) {
        useAcc = false;
    }
    imuMahonyAHRSupdate(deltaT * 1e-6f,
                        // DEGREES_TO_RADIANS(gyroAverage[X]), DEGREES_TO_RADIANS(gyroAverage[Y]), DEGREES_TO_RADIANS(gyroAverage[Z]),
			((gyroAverage[X]) * 0.0174532925f), ((gyroAverage[Y]) * 0.0174532925f), ((gyroAverage[Z]) * 0.0174532925f),
                        useAcc, accAverage[X], accAverage[Y], accAverage[Z],
                        useMag, mag.magADC[X], mag.magADC[Y], mag.magADC[Z],
                        useYaw, rawYawError);

    imuUpdateEulerAngles();
}

void imuUpdateAttitude(timeUs_t currentTimeUs)
{
    if (sensors(SENSOR_ACC) && acc.isAccelUpdatedAtLeastOnce) {
        imuCalculateEstimatedAttitude(currentTimeUs);
    } else {
        acc.accADC[X] = 0;
        acc.accADC[Y] = 0;
        acc.accADC[Z] = 0;
    }
}

float getCosTiltAngle(void)
{
    return rMat[2][2];
}

int16_t calculateThrottleAngleCorrection(uint8_t throttle_correction_value)
{
    /*
    * Use 0 as the throttle angle correction if we are inverted, vertical or with a
    * small angle < 0.86 deg
    * TODO: Define this small angle in config.
    */
    if (rMat[2][2] <= 0.015f) {
        return 0;
    }
    int angle = lrintf(acos_approx(rMat[2][2]) * throttleAngleScale);
    if (angle > 900)
        angle = 900;
    return lrintf(throttle_correction_value * sin_approx(angle / (900.0f * M_PIf / 2.0f)));
}


void imuQuaternionComputeProducts(quaternion *quat, quaternionProducts *quatProd)
{
    quatProd->ww = quat->w * quat->w;
    quatProd->wx = quat->w * quat->x;
    quatProd->wy = quat->w * quat->y;
    quatProd->wz = quat->w * quat->z;
    quatProd->xx = quat->x * quat->x;
    quatProd->xy = quat->x * quat->y;
    quatProd->xz = quat->x * quat->z;
    quatProd->yy = quat->y * quat->y;
    quatProd->yz = quat->y * quat->z;
    quatProd->zz = quat->z * quat->z;
}

bool imuQuaternionHeadfreeOffsetSet(void)
{
  // if ((ABS(attitude.values.roll) < 450)  && (ABS(attitude.values.pitch) < 450)) {
    if ((__extension__ ({
	    __typeof__ (attitude.values.roll) _x = (attitude.values.roll);
	    _x > 0 ? _x : -_x; }) < 450)
      && (__extension__ ({ __typeof__ (attitude.values.pitch) _x = (attitude.values.pitch);
	    _x > 0 ? _x : -_x; }) < 450)) {
        const float yaw = -atan2_approx((+2.0f * (qP.wz + qP.xy)), (+1.0f - 2.0f * (qP.yy + qP.zz)));

        offset.w = cos_approx(yaw/2);
        offset.x = 0;
        offset.y = 0;
        offset.z = sin_approx(yaw/2);

        return true;
    } else {
        return false;
    }
}

void imuQuaternionMultiplication(quaternion *q1, quaternion *q2, quaternion *result)
{
    const float A = (q1->w + q1->x) * (q2->w + q2->x);
    const float B = (q1->z - q1->y) * (q2->y - q2->z);
    const float C = (q1->w - q1->x) * (q2->y + q2->z);
    const float D = (q1->y + q1->z) * (q2->w - q2->x);
    const float E = (q1->x + q1->z) * (q2->x + q2->y);
    const float F = (q1->x - q1->z) * (q2->x - q2->y);
    const float G = (q1->w + q1->y) * (q2->w - q2->z);
    const float H = (q1->w - q1->y) * (q2->w + q2->z);

    result->w = B + (- E - F + G + H) / 2.0f;
    result->x = A - (+ E + F + G + H) / 2.0f;
    result->y = C + (+ E - F + G - H) / 2.0f;
    result->z = D + (+ E - F - G + H) / 2.0f;
}

void imuQuaternionHeadfreeTransformVectorEarthToBody(t_fp_vector_def *v)
{
    quaternionProducts buffer;

    imuQuaternionMultiplication(&offset, &q, &headfree);
    imuQuaternionComputeProducts(&headfree, &buffer);

    const float x = (buffer.ww + buffer.xx - buffer.yy - buffer.zz) * v->X + 2.0f * (buffer.xy + buffer.wz) * v->Y + 2.0f * (buffer.xz - buffer.wy) * v->Z;
    const float y = 2.0f * (buffer.xy - buffer.wz) * v->X + (buffer.ww - buffer.xx + buffer.yy - buffer.zz) * v->Y + 2.0f * (buffer.yz + buffer.wx) * v->Z;
    const float z = 2.0f * (buffer.xz + buffer.wy) * v->X + 2.0f * (buffer.yz - buffer.wx) * v->Y + (buffer.ww - buffer.xx - buffer.yy + buffer.zz) * v->Z;

    v->X = x;
    v->Y = y;
    v->Z = z;
}
