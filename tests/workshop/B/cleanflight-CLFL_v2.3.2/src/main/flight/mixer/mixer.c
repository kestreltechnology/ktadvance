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

/*
#include <stdbool.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

#include "platform.h"

#include "build/build_config.h"
#include "build/debug.h"

#include "common/axis.h"
#include "common/filter.h"
#include "common/maths.h"

#include "config/feature.h"
#include "pg/pg.h"
#include "pg/pg_ids.h"

#include "drivers/pwm_output.h"
#include "drivers/pwm_esc_detect.h"
#include "drivers/time.h"

#include "io/motors.h"

#include "fc/config.h"
#include "fc/rc_controls.h"
#include "fc/rc_modes.h"
#include "fc/runtime_config.h"
#include "fc/fc_core.h"
#include "fc/fc_rc.h"

#include "flight/failsafe.h"
#include "flight/imu.h"
#include "flight/mixer.h"
#include "flight/mixer_tricopter.h"
#include "flight/pid.h"

#include "rx/rx.h"

#include "sensors/battery.h"
*/

#include "../flight_h.h"

typedef _Bool bool;
#define true 1
#define false 0
#define NULL ((void *)0)

#define BRUSHLESS_MOTORS_PWM_RATE 480
#define DSHOT_DISARM_COMMAND 0
#define DSHOT_MAX_THROTTLE 2047
#define DSHOT_MIN_THROTTLE  48
#define DSHOT_3D_DEADBAND_LOW 1047
#define DSHOT_3D_DEADBAND_HIGH 1048
#define ENABLE_DSHOT_DMAR 0
#define MAX_SUPPORTED_MOTORS 8
#define PID_MIXER_SCALING 1000.0f
#define PWM_RANGE_MAX 2000
#define PWM_RANGE_MID 1500
#define PWM_RANGE_MIN 1000
#define USABLE_TIMER_CHANNEL_COUNT 12

/* =====================================================================
 * from mixer_tricopter.c
 * ===================================================================== */

extern const tricopterMixerConfig_t pgResetTemplate_tricopterMixerConfig;
tricopterMixerConfig_t tricopterMixerConfig_System;
tricopterMixerConfig_t tricopterMixerConfig_Copy;
extern const pgRegistry_t tricopterMixerConfig_Registry;
const pgRegistry_t tricopterMixerConfig_Registry __attribute__ ((section(".pg_registry"), used, aligned(4))) = {
  .pgn = 528 | (0 << 12),
  .size = sizeof(tricopterMixerConfig_t) | PGR_SIZE_SYSTEM_FLAG,
  .address = (uint8_t*)&tricopterMixerConfig_System,
  .copy = (uint8_t*)&tricopterMixerConfig_Copy,
  .ptr = 0,
  .reset = {.ptr = (void*)&pgResetTemplate_tricopterMixerConfig}, };

const tricopterMixerConfig_t pgResetTemplate_tricopterMixerConfig __attribute__ ((section(".pg_resetdata"), used, aligned(2))) = { .dummy = 0 };

_Bool mixerTricopterIsServoSaturated(float errorRate)
{
    return errorRate > 75;
}

float mixerTricopterMotorCorrection(int motor)
{
    (void)(motor);
    return 0.0f;
}

void mixerTricopterInit(void){ }


// PG_REGISTER_WITH_RESET_TEMPLATE(mixerConfig_t, mixerConfig, PG_MIXER_CONFIG, 0);
extern const mixerConfig_t pgResetTemplate_mixerConfig;
mixerConfig_t mixerConfig_System;
mixerConfig_t mixerConfig_Copy;
extern const pgRegistry_t mixerConfig_Registry;
const pgRegistry_t mixerConfig_Registry __attribute__ ((section(".pg_registry"), used, aligned(4))) =
{ .pgn = 20 | (0 << 12),
  .size = sizeof(mixerConfig_t) | PGR_SIZE_SYSTEM_FLAG,
  .address = (uint8_t*)&mixerConfig_System,
  .copy = (uint8_t*)&mixerConfig_Copy,
  .ptr = 0,
  .reset = {.ptr = (void*)&pgResetTemplate_mixerConfig}, };

/*
#ifndef TARGET_DEFAULT_MIXER
#define TARGET_DEFAULT_MIXER    MIXER_QUADX
#endif
PG_RESET_TEMPLATE(mixerConfig_t, mixerConfig,
    .mixerMode = TARGET_DEFAULT_MIXER,
    .yaw_motors_reversed = false,
);
*/
const mixerConfig_t pgResetTemplate_mixerConfig __attribute__ ((section(".pg_resetdata"), used, aligned(2))) = { .mixerMode = MIXER_QUADX, .yaw_motors_reversed = 0, };

// PG_REGISTER_WITH_RESET_FN(motorConfig_t, motorConfig, PG_MOTOR_CONFIG, 1);
extern void pgResetFn_motorConfig(motorConfig_t *);
motorConfig_t motorConfig_System;
motorConfig_t motorConfig_Copy;
extern const pgRegistry_t motorConfig_Registry;
const pgRegistry_t motorConfig_Registry __attribute__ ((section(".pg_registry"), used, aligned(4))) = {
  .pgn = 6 | (1 << 12),
  .size = sizeof(motorConfig_t) | PGR_SIZE_SYSTEM_FLAG,
  .address = (uint8_t*)&motorConfig_System,
  .copy = (uint8_t*)&motorConfig_Copy,
  .ptr = 0,
  .reset = {.fn = (pgResetFunc*)&pgResetFn_motorConfig }, };

void pgResetFn_motorConfig(motorConfig_t *motorConfig)
{
    {
        motorConfig->minthrottle = 1070;
        motorConfig->dev.motorPwmRate = BRUSHLESS_MOTORS_PWM_RATE;
        motorConfig->dev.motorPwmProtocol = PWM_TYPE_ONESHOT125;
    }
    motorConfig->maxthrottle = 2000;
    motorConfig->mincommand = 1000;
    motorConfig->digitalIdleOffsetValue = 450;
    motorConfig->dev.useBurstDshot = ENABLE_DSHOT_DMAR;

    int motorIndex = 0;
    for (int i = 0; i < USABLE_TIMER_CHANNEL_COUNT && motorIndex < MAX_SUPPORTED_MOTORS; i++) {
        if (timerHardware[i].usageFlags & TIM_USE_MOTOR) {
            motorConfig->dev.ioTags[motorIndex] = timerHardware[i].tag;
            motorIndex++;
        }
    }
}

// PG_REGISTER_ARRAY(motorMixer_t, MAX_SUPPORTED_MOTORS, customMotorMixer, PG_MOTOR_MIXER, 0);
motorMixer_t customMotorMixer_SystemArray[8];
motorMixer_t customMotorMixer_CopyArray[8];
extern const pgRegistry_t customMotorMixer_Registry;
const pgRegistry_t customMotorMixer_Registry __attribute__ ((section(".pg_registry"), used, aligned(4))) = {
  .pgn = 4 | (0 << 12),
  .size = (sizeof(motorMixer_t) * 8) | PGR_SIZE_SYSTEM_FLAG,
  .address = (uint8_t*)&customMotorMixer_SystemArray,
  .copy = (uint8_t*)&customMotorMixer_CopyArray,
  .ptr = 0,
  .reset = {.ptr = 0}, };

#define PWM_RANGE_MID 1500

static uint8_t motorCount;
static float motorMixRange;

float motor[MAX_SUPPORTED_MOTORS];
float motor_disarmed[MAX_SUPPORTED_MOTORS];

mixerMode_e currentMixerMode;
static motorMixer_t currentMixer[MAX_SUPPORTED_MOTORS];


static const motorMixer_t mixerQuadX[] = {
    { 1.0f, -1.0f,  1.0f, -1.0f },          // REAR_R
    { 1.0f, -1.0f, -1.0f,  1.0f },          // FRONT_R
    { 1.0f,  1.0f,  1.0f,  1.0f },          // REAR_L
    { 1.0f,  1.0f, -1.0f, -1.0f },          // FRONT_L
};

static const motorMixer_t mixerTricopter[] = {
    { 1.0f,  0.0f,  1.333333f,  0.0f },     // REAR
    { 1.0f, -1.0f, -0.666667f,  0.0f },     // RIGHT
    { 1.0f,  1.0f, -0.666667f,  0.0f },     // LEFT
};

static const motorMixer_t mixerQuadP[] = {
    { 1.0f,  0.0f,  1.0f, -1.0f },          // REAR
    { 1.0f, -1.0f,  0.0f,  1.0f },          // RIGHT
    { 1.0f,  1.0f,  0.0f,  1.0f },          // LEFT
    { 1.0f,  0.0f, -1.0f, -1.0f },          // FRONT
};

static const motorMixer_t mixerY4[] = {
    { 1.0f,  0.0f,  1.0f, -1.0f },          // REAR_TOP CW
    { 1.0f, -1.0f, -1.0f,  0.0f },          // FRONT_R CCW
    { 1.0f,  0.0f,  1.0f,  1.0f },          // REAR_BOTTOM CCW
    { 1.0f,  1.0f, -1.0f,  0.0f },          // FRONT_L CW
};


static const motorMixer_t mixerHex6X[] = {
    { 1.0f, -0.5f,  0.866025f,  1.0f },     // REAR_R
    { 1.0f, -0.5f, -0.866025f,  1.0f },     // FRONT_R
    { 1.0f,  0.5f,  0.866025f, -1.0f },     // REAR_L
    { 1.0f,  0.5f, -0.866025f, -1.0f },     // FRONT_L
    { 1.0f, -1.0f,  0.0f,      -1.0f },     // RIGHT
    { 1.0f,  1.0f,  0.0f,       1.0f },     // LEFT
};

static const motorMixer_t mixerVtail4[] = {
    { 1.0f,  -0.58f,  0.58f, 1.0f },        // REAR_R
    { 1.0f,  -0.46f, -0.39f, -0.5f },       // FRONT_R
    { 1.0f,  0.58f,  0.58f, -1.0f },        // REAR_L
    { 1.0f,  0.46f, -0.39f, 0.5f },         // FRONT_L
};

static const motorMixer_t mixerAtail4[] = {
    { 1.0f,  0.0f,  1.0f,  1.0f },          // REAR_R
    { 1.0f, -1.0f, -1.0f,  0.0f },          // FRONT_R
    { 1.0f,  0.0f,  1.0f, -1.0f },          // REAR_L
    { 1.0f,  1.0f, -1.0f, -0.0f },          // FRONT_L
};

static const motorMixer_t mixerSingleProp[] = {
    { 1.0f,  0.0f,  0.0f, 0.0f },
};

static const motorMixer_t mixerQuadX1234[] = {
    { 1.0f,  1.0f, -1.0f, -1.0f },          // FRONT_L
    { 1.0f, -1.0f, -1.0f,  1.0f },          // FRONT_R
    { 1.0f, -1.0f,  1.0f, -1.0f },          // REAR_R
    { 1.0f,  1.0f,  1.0f,  1.0f },          // REAR_L
};

// Keep synced with mixerMode_e
const mixer_t mixers[] = {
    // motors, use servo, motor mixer
    { 0, false, NULL },                // entry 0
    { 3, true,  mixerTricopter },      // MIXER_TRI
    { 4, false, mixerQuadP },          // MIXER_QUADP
    { 4, false, mixerQuadX },          // MIXER_QUADX
    { 2, true,  NULL },                // MIXER_BICOPTER
    { 0, true,  NULL },                // * MIXER_GIMBAL
    { 6, false, NULL },                // MIXER_Y6
    { 6, false, NULL },                // MIXER_HEX6
    { 1, true,  mixerSingleProp },     // * MIXER_FLYING_WING
    { 4, false, mixerY4 },             // MIXER_Y4
    { 6, false, mixerHex6X },          // MIXER_HEX6X
    { 8, false, NULL },                // MIXER_OCTOX8
    { 8, false, NULL },                // MIXER_OCTOFLATP
    { 8, false, NULL },                // MIXER_OCTOFLATX
    { 1, true,  mixerSingleProp },     // * MIXER_AIRPLANE
    { 1, true,  mixerSingleProp },     // * MIXER_HELI_120_CCPM
    { 0, true,  NULL },                // * MIXER_HELI_90_DEG
    { 4, false, mixerVtail4 },         // MIXER_VTAIL4
    { 6, false, NULL },                // MIXER_HEX6H
    { 0, true,  NULL },                // MIXER_RX_TO_SERVO
    { 2, true,  NULL },                // MIXER_DUALCOPTER
    { 1, true,  NULL },                // MIXER_SINGLECOPTER
    { 4, false, mixerAtail4 },         // MIXER_ATAIL4
    { 0, false, NULL },                // MIXER_CUSTOM
    { 2, true,  NULL },                // MIXER_CUSTOM_AIRPLANE
    { 3, true,  NULL },                // MIXER_CUSTOM_TRI
    { 4, false, mixerQuadX1234 }       // MIXER_QUADX_1234
};
// #endif // !USE_QUAD_MIXER_ONLY

float motorOutputHigh, motorOutputLow;

static float disarmMotorOutput, deadbandMotor3dHigh, deadbandMotor3dLow;
static uint16_t rcCommand3dDeadBandLow;
static uint16_t rcCommand3dDeadBandHigh;
static float rcCommandThrottleRange, rcCommandThrottleRange3dLow, rcCommandThrottleRange3dHigh;

uint8_t getMotorCount(void)
{
    return motorCount;
}

float getMotorMixRange(void)
{
    return motorMixRange;
}

bool areMotorsRunning(void)
{
    bool motorsRunning = false;
    // if (ARMING_FLAG(ARMED)) {
    if  ((armingFlags & (ARMED))) {
        motorsRunning = true;
    } else {
        for (int i = 0; i < motorCount; i++) {
            if (motor_disarmed[i] != disarmMotorOutput) {
                motorsRunning = true;

                break;
            }
        }
    }

    return motorsRunning;
}

bool mixerIsTricopter(void)
{
    return (currentMixerMode == MIXER_TRI || currentMixerMode == MIXER_CUSTOM_TRI);
}

bool mixerIsOutputSaturated(int axis, float errorRate)
{
    if (axis == FD_YAW && mixerIsTricopter()) {
        return mixerTricopterIsServoSaturated(errorRate);
    } else {
        return motorMixRange >= 1.0f;
    }
    return false;
}

// All PWM motor scaling is done to standard PWM range of 1000-2000 for easier tick conversion with legacy code / configurator
// DSHOT scaling is done to the actual dshot range
void initEscEndpoints(void)
{
    // Can't use 'isMotorProtocolDshot()' here since motors haven't been initialised yet
    switch (motorConfig()->dev.motorPwmProtocol) {
#ifdef USE_DSHOT
    case PWM_TYPE_PROSHOT1000:
    case PWM_TYPE_DSHOT1200:
    case PWM_TYPE_DSHOT600:
    case PWM_TYPE_DSHOT300:
    case PWM_TYPE_DSHOT150:
        disarmMotorOutput = DSHOT_DISARM_COMMAND;
        if (feature(FEATURE_3D)) {
	  motorOutputLow = DSHOT_MIN_THROTTLE + ((DSHOT_3D_DEADBAND_LOW - DSHOT_MIN_THROTTLE) / 100.0f) * (0.01 * motorConfig()->digitalIdleOffsetValue);
        } else {
            motorOutputLow = DSHOT_MIN_THROTTLE + ((DSHOT_MAX_THROTTLE - DSHOT_MIN_THROTTLE) / 100.0f) * (0.01 * motorConfig()->digitalIdleOffsetValue);
        }
        motorOutputHigh = DSHOT_MAX_THROTTLE;
        deadbandMotor3dHigh = DSHOT_3D_DEADBAND_HIGH + ((DSHOT_MAX_THROTTLE - DSHOT_3D_DEADBAND_HIGH) / 100.0f) * (0.01 * motorConfig()->digitalIdleOffsetValue);
        deadbandMotor3dLow = DSHOT_3D_DEADBAND_LOW;

        break;
#endif
    default:
        if (feature(FEATURE_3D)) {
            disarmMotorOutput = flight3DConfig()->neutral3d;
            motorOutputLow = PWM_RANGE_MIN;
        } else {
            disarmMotorOutput = motorConfig()->mincommand;
            motorOutputLow = motorConfig()->minthrottle;
        }
        motorOutputHigh = motorConfig()->maxthrottle;
        deadbandMotor3dHigh = flight3DConfig()->deadband3d_high;
        deadbandMotor3dLow = flight3DConfig()->deadband3d_low;

        break;
    }

    rcCommandThrottleRange = PWM_RANGE_MAX - rxConfig()->mincheck;

    rcCommand3dDeadBandLow = rxConfig()->midrc - flight3DConfig()->deadband3d_throttle;
    rcCommand3dDeadBandHigh = rxConfig()->midrc + flight3DConfig()->deadband3d_throttle;

    rcCommandThrottleRange3dLow = rcCommand3dDeadBandLow - PWM_RANGE_MIN;
    rcCommandThrottleRange3dHigh = PWM_RANGE_MAX - rcCommand3dDeadBandHigh;
}

void mixerInit(mixerMode_e mixerMode)
{
    currentMixerMode = mixerMode;

    initEscEndpoints();
    if (mixerIsTricopter()) {
        mixerTricopterInit();
    }
}

void mixerConfigureOutput(void)
{
    motorCount = 0;

    if (currentMixerMode == MIXER_CUSTOM || currentMixerMode == MIXER_CUSTOM_TRI || currentMixerMode == MIXER_CUSTOM_AIRPLANE) {
        // load custom mixer into currentMixer
        for (int i = 0; i < MAX_SUPPORTED_MOTORS; i++) {
            // check if done
            if (customMotorMixer(i)->throttle == 0.0f) {
                break;
            }
            currentMixer[i] = *customMotorMixer(i);
            motorCount++;
        }
    } else {
        motorCount = mixers[currentMixerMode].motorCount;
        if (motorCount > MAX_SUPPORTED_MOTORS) {
            motorCount = MAX_SUPPORTED_MOTORS;
        }
        // copy motor-based mixers
        if (mixers[currentMixerMode].motor) {
            for (int i = 0; i < motorCount; i++)
                currentMixer[i] = mixers[currentMixerMode].motor[i];
        }
    }

    // in 3D mode, mixer gain has to be halved
    if (feature(FEATURE_3D)) {
        if (motorCount > 1) {
            for (int i = 0; i < motorCount; i++) {
                currentMixer[i].pitch *= 0.5f;
                currentMixer[i].roll *= 0.5f;
                currentMixer[i].yaw *= 0.5f;
            }
        }
    }

    mixerResetDisarmedMotors();
}

void mixerLoadMix(int index, motorMixer_t *customMixers)
{
    // we're 1-based
    index++;
    // clear existing
    for (int i = 0; i < MAX_SUPPORTED_MOTORS; i++) {
        customMixers[i].throttle = 0.0f;
    }
    // do we have anything here to begin with?
    if (mixers[index].motor != NULL) {
        for (int i = 0; i < mixers[index].motorCount; i++) {
            customMixers[i] = mixers[index].motor[i];
        }
    }
}

void mixerResetDisarmedMotors(void)
{
    // set disarmed motor values
    for (int i = 0; i < MAX_SUPPORTED_MOTORS; i++) {
        motor_disarmed[i] = disarmMotorOutput;
    }
}

void writeMotors(void)
{
    if (pwmAreMotorsEnabled()) {
        for (int i = 0; i < motorCount; i++) {
            pwmWriteMotor(i, motor[i]);
        }
        pwmCompleteMotorUpdate(motorCount);
    }
}

static void writeAllMotors(int16_t mc)
{
    // Sends commands to all motors
    for (int i = 0; i < motorCount; i++) {
        motor[i] = mc;
    }
    writeMotors();
}

void stopMotors(void)
{
    writeAllMotors(disarmMotorOutput);
    delay(50); // give the timers and ESCs a chance to react.
}

void stopPwmAllMotors(void)
{
    pwmShutdownPulsesForAllMotors(motorCount);
    delayMicroseconds(1500);
}

static float throttle = 0;
static float motorOutputMin;
static float motorRangeMin;
static float motorRangeMax;
static float motorOutputRange;
static int8_t motorOutputMixSign;

static void calculateThrottleAndCurrentMotorEndpoints(timeUs_t currentTimeUs)
{
    static uint16_t rcThrottlePrevious = 0;   // Store the last throttle direction for deadband transitions
    static timeUs_t reversalTimeUs = 0; // time when motors last reversed in 3D mode
    float currentThrottleInputRange = 0;

    if (feature(FEATURE_3D)) {
    // if (!ARMING_FLAG(ARMED)) {
        if (!(armingFlags & (ARMED))) {
            rcThrottlePrevious = rxConfig()->midrc; // When disarmed set to mid_rc. It always results in positive direction after arming.
        }

        if (rcCommand[THROTTLE] <= rcCommand3dDeadBandLow) {
            // INVERTED
            motorRangeMin = motorOutputLow;
            motorRangeMax = deadbandMotor3dLow;
            if (isMotorProtocolDshot()) {
                motorOutputMin = motorOutputLow;
                motorOutputRange = deadbandMotor3dLow - motorOutputLow;
            } else {
                motorOutputMin = deadbandMotor3dLow;
                motorOutputRange = motorOutputLow - deadbandMotor3dLow;
            }
            if (motorOutputMixSign != -1) {
                reversalTimeUs = currentTimeUs;
            }
            motorOutputMixSign = -1;
            rcThrottlePrevious = rcCommand[THROTTLE];
            throttle = rcCommand3dDeadBandLow - rcCommand[THROTTLE];
            currentThrottleInputRange = rcCommandThrottleRange3dLow;
        } else if (rcCommand[THROTTLE] >= rcCommand3dDeadBandHigh) {
            // NORMAL
            motorRangeMin = deadbandMotor3dHigh;
            motorRangeMax = motorOutputHigh;
            motorOutputMin = deadbandMotor3dHigh;
            motorOutputRange = motorOutputHigh - deadbandMotor3dHigh;
            if (motorOutputMixSign != 1) {
                reversalTimeUs = currentTimeUs;
            }
            motorOutputMixSign = 1;
            rcThrottlePrevious = rcCommand[THROTTLE];
            throttle = rcCommand[THROTTLE] - rcCommand3dDeadBandHigh;
            currentThrottleInputRange = rcCommandThrottleRange3dHigh;
        } else if ((rcThrottlePrevious <= rcCommand3dDeadBandLow &&
                !flight3DConfigMutable()->switched_mode3d) ||
                isMotorsReversed()) {
            // INVERTED_TO_DEADBAND
            motorRangeMin = motorOutputLow;
            motorRangeMax = deadbandMotor3dLow;
            if (isMotorProtocolDshot()) {
                motorOutputMin = motorOutputLow;
                motorOutputRange = deadbandMotor3dLow - motorOutputLow;
            } else {
                motorOutputMin = deadbandMotor3dLow;
                motorOutputRange = motorOutputLow - deadbandMotor3dLow;
            }
            if (motorOutputMixSign != -1) {
                reversalTimeUs = currentTimeUs;
            }
            motorOutputMixSign = -1;
            throttle = 0;
            currentThrottleInputRange = rcCommandThrottleRange3dLow;
        } else {
            // NORMAL_TO_DEADBAND
            motorRangeMin = deadbandMotor3dHigh;
            motorRangeMax = motorOutputHigh;
            motorOutputMin = deadbandMotor3dHigh;
            motorOutputRange = motorOutputHigh - deadbandMotor3dHigh;
            if (motorOutputMixSign != 1) {
                reversalTimeUs = currentTimeUs;
            }
            motorOutputMixSign = 1;
            throttle = 0;
            currentThrottleInputRange = rcCommandThrottleRange3dHigh;
        }
        if (currentTimeUs - reversalTimeUs < 250000) {
            // keep ITerm zero for 250ms after motor reversal
            pidResetITerm();
        }
    } else {
        throttle = rcCommand[THROTTLE] - rxConfig()->mincheck;
        currentThrottleInputRange = rcCommandThrottleRange;
        motorRangeMin = motorOutputLow;
        motorRangeMax = motorOutputHigh;
        motorOutputMin = motorOutputLow;
        motorOutputRange = motorOutputHigh - motorOutputLow;
        motorOutputMixSign = 1;
    }

    throttle = constrainf(throttle / currentThrottleInputRange, 0.0f, 1.0f);
}

#define CRASH_FLIP_DEADBAND 20
#define CRASH_FLIP_STICK_MINF 0.15f

static void applyFlipOverAfterCrashModeToMotors(void)
{
  // if (ARMING_FLAG(ARMED)) {
    if ((armingFlags & (ARMED))) {
        float stickDeflectionPitchAbs = getRcDeflectionAbs(FD_PITCH);
        float stickDeflectionRollAbs = getRcDeflectionAbs(FD_ROLL);
        float stickDeflectionYawAbs = getRcDeflectionAbs(FD_YAW);
        float signPitch = getRcDeflection(FD_PITCH) < 0 ? 1 : -1;
        float signRoll = getRcDeflection(FD_ROLL) < 0 ? 1 : -1;
        float signYaw = (getRcDeflection(FD_YAW) < 0 ? 1 : -1) * (mixerConfig()->yaw_motors_reversed ? 1 : -1);

        float stickDeflectionLength = sqrtf(stickDeflectionPitchAbs*stickDeflectionPitchAbs + stickDeflectionRollAbs*stickDeflectionRollAbs);

        // if (stickDeflectionYawAbs > MAX(stickDeflectionPitchAbs, stickDeflectionRollAbs)) {
        if (stickDeflectionYawAbs > __extension__ ({ __typeof__ (stickDeflectionPitchAbs) _a = (stickDeflectionPitchAbs); __typeof__ (stickDeflectionRollAbs) _b = (stickDeflectionRollAbs); _a > _b ? _a : _b; })) {
            // If yaw is the dominant, disable pitch and roll
            stickDeflectionLength = stickDeflectionYawAbs;
            signRoll = 0;
            signPitch = 0;
        } else {
            // If pitch/roll dominant, disable yaw
            signYaw = 0;
        }

        float cosPhi = (stickDeflectionPitchAbs + stickDeflectionRollAbs) / (sqrtf(2.0f) * stickDeflectionLength);
        const float cosThreshold = sqrtf(3.0f)/2.0f; // cos(PI/6.0f)

        if (cosPhi < cosThreshold) {
            // Enforce either roll or pitch exclusively, if not on diagonal
            if (stickDeflectionRollAbs > stickDeflectionPitchAbs) {
                signPitch = 0;
            } else {
                signRoll = 0;
            }
        }

        // Apply a reasonable amount of stick deadband
        const float flipStickRange = 1.0f - CRASH_FLIP_STICK_MINF;
	//        float flipPower = MAX(0.0f, stickDeflectionLength - CRASH_FLIP_STICK_MINF) / flipStickRange;
        float flipPower = __extension__ ({
	    __typeof__ (0.0f) _a = (0.0f);
	    __typeof__ (stickDeflectionLength - 0.15f) _b = (stickDeflectionLength - 0.15f);
	    _a > _b ? _a : _b; }) / flipStickRange;

        for (int i = 0; i < motorCount; ++i) {
            float motorOutput =
                signPitch*currentMixer[i].pitch +
                signRoll*currentMixer[i].roll +
                signYaw*currentMixer[i].yaw;

            // motorOutput = MIN(1.0f, flipPower*motorOutput);
            motorOutput = __extension__ ({
		__typeof__ (1.0f) _a = (1.0f);
		__typeof__ (flipPower*motorOutput) _b = (flipPower*motorOutput);
		_a < _b ? _a : _b; });
            motorOutput = motorOutputMin + motorOutput*motorOutputRange;

            // Add a little bit to the motorOutputMin so props aren't spinning when sticks are centered
            motorOutput = (motorOutput < motorOutputMin + CRASH_FLIP_DEADBAND) ? disarmMotorOutput : (motorOutput - CRASH_FLIP_DEADBAND);
            motor[i] = motorOutput;
        }
    } else {
        // Disarmed mode
        for (int i = 0; i < motorCount; i++) {
            motor[i] = motor_disarmed[i];
        }
    }
}

static void applyMixToMotors(float motorMix[MAX_SUPPORTED_MOTORS])
{
    // Now add in the desired throttle, but keep in a range that doesn't clip adjusted
    // roll/pitch/yaw. This could move throttle down, but also up for those low throttle flips.
    for (int i = 0; i < motorCount; i++) {
        float motorOutput = motorOutputMin + (motorOutputRange * (motorOutputMixSign * motorMix[i] + throttle * currentMixer[i].throttle));
        if (mixerIsTricopter()) {
            motorOutput += mixerTricopterMotorCorrection(i);
        }
        if (failsafeIsActive()) {
            if (isMotorProtocolDshot()) {
                motorOutput = (motorOutput < motorRangeMin) ? disarmMotorOutput : motorOutput; // Prevent getting into special reserved range
            }
            motorOutput = constrain(motorOutput, disarmMotorOutput, motorRangeMax);
        } else {
            motorOutput = constrain(motorOutput, motorRangeMin, motorRangeMax);
        }
        // Motor stop handling
        // if (feature(FEATURE_MOTOR_STOP) && ARMING_FLAG(ARMED) && !feature(FEATURE_3D) && !isAirmodeActive()) {
        if (feature(FEATURE_MOTOR_STOP) && (armingFlags & (ARMED)) && !feature(FEATURE_3D) && !isAirmodeActive()) {
            if (((rcData[THROTTLE]) < rxConfig()->mincheck)) {
                motorOutput = disarmMotorOutput;
            }
        }
        motor[i] = motorOutput;
    }

    // Disarmed mode
    // if (!ARMING_FLAG(ARMED)) {
    if (!(armingFlags & (ARMED))) {
        for (int i = 0; i < motorCount; i++) {
            motor[i] = motor_disarmed[i];
        }
    }
}

void mixTable(timeUs_t currentTimeUs, uint8_t vbatPidCompensation)
{
    if (isFlipOverAfterCrashMode()) {
        applyFlipOverAfterCrashModeToMotors();
        return;
    }

    // Find min and max throttle based on conditions. Throttle has to be known before mixing
    calculateThrottleAndCurrentMotorEndpoints(currentTimeUs);

    // Calculate and Limit the PIDsum
    const float scaledAxisPidRoll =
        constrainf(axisPIDSum[FD_ROLL], -currentPidProfile->pidSumLimit, currentPidProfile->pidSumLimit) / PID_MIXER_SCALING;
    const float scaledAxisPidPitch =
        constrainf(axisPIDSum[FD_PITCH], -currentPidProfile->pidSumLimit, currentPidProfile->pidSumLimit) / PID_MIXER_SCALING;
    float scaledAxisPidYaw =
        constrainf(axisPIDSum[FD_YAW], -currentPidProfile->pidSumLimitYaw, currentPidProfile->pidSumLimitYaw) / PID_MIXER_SCALING;
    if (!mixerConfig()->yaw_motors_reversed) {
        scaledAxisPidYaw = -scaledAxisPidYaw;
    }

    // Calculate voltage compensation
    const float vbatCompensationFactor = vbatPidCompensation ? calculateVbatPidCompensation() : 1.0f;

    // Find roll/pitch/yaw desired output
    float motorMix[MAX_SUPPORTED_MOTORS];
    float motorMixMax = 0, motorMixMin = 0;
    for (int i = 0; i < motorCount; i++) {
        float mix =
            scaledAxisPidRoll  * currentMixer[i].roll +
            scaledAxisPidPitch * currentMixer[i].pitch +
            scaledAxisPidYaw   * currentMixer[i].yaw;

        mix *= vbatCompensationFactor;  // Add voltage compensation

        if (mix > motorMixMax) {
            motorMixMax = mix;
        } else if (mix < motorMixMin) {
            motorMixMin = mix;
        }
        motorMix[i] = mix;
    }

    motorMixRange = motorMixMax - motorMixMin;

    if (motorMixRange > 1.0f) {
        for (int i = 0; i < motorCount; i++) {
            motorMix[i] /= motorMixRange;
        }
        // Get the maximum correction by setting offset to center when airmode enabled
        if (isAirmodeActive()) {
            throttle = 0.5f;
        }
    } else {
        if (isAirmodeActive() || throttle > 0.5f) {  // Only automatically adjust throttle when airmode enabled. Airmode logic is always active on high throttle
            const float throttleLimitOffset = motorMixRange / 2.0f;
            throttle = constrainf(throttle, 0.0f + throttleLimitOffset, 1.0f - throttleLimitOffset);
        }
    }

    // Apply the mix to motor endpoints
    applyMixToMotors(motorMix);
}

float convertExternalToMotor(uint16_t externalValue)
{
    uint16_t motorValue;
    switch ((int)isMotorProtocolDshot()) {

    case true:
        externalValue = constrain(externalValue, PWM_RANGE_MIN, PWM_RANGE_MAX);

        if (feature(FEATURE_3D)) {
            if (externalValue == PWM_RANGE_MID) {
                motorValue = DSHOT_DISARM_COMMAND;
            } else if (externalValue < PWM_RANGE_MID) {
                motorValue = scaleRange(externalValue, PWM_RANGE_MIN, PWM_RANGE_MID - 1, DSHOT_3D_DEADBAND_LOW, DSHOT_MIN_THROTTLE);
            } else {
                motorValue = scaleRange(externalValue, PWM_RANGE_MID + 1, PWM_RANGE_MAX, DSHOT_3D_DEADBAND_HIGH, DSHOT_MAX_THROTTLE);
            }
        } else {
            motorValue = (externalValue == PWM_RANGE_MIN) ? DSHOT_DISARM_COMMAND : scaleRange(externalValue, PWM_RANGE_MIN + 1, PWM_RANGE_MAX, DSHOT_MIN_THROTTLE, DSHOT_MAX_THROTTLE);
        }

        break;
    case false:

    default:
        motorValue = externalValue;
        break;
    }

    return (float)motorValue;
}

uint16_t convertMotorToExternal(float motorValue)
{
    uint16_t externalValue;
    switch ((int)isMotorProtocolDshot()) {
#ifdef USE_DSHOT
    case true:
        if (feature(FEATURE_3D)) {
            if (motorValue == DSHOT_DISARM_COMMAND || motorValue < DSHOT_MIN_THROTTLE) {
                externalValue = PWM_RANGE_MID;
            } else if (motorValue <= DSHOT_3D_DEADBAND_LOW) {
                externalValue = scaleRange(motorValue, DSHOT_MIN_THROTTLE, DSHOT_3D_DEADBAND_LOW, PWM_RANGE_MID - 1, PWM_RANGE_MIN);
            } else {
                externalValue = scaleRange(motorValue, DSHOT_3D_DEADBAND_HIGH, DSHOT_MAX_THROTTLE, PWM_RANGE_MID + 1, PWM_RANGE_MAX);
            }
        } else {
            externalValue = (motorValue < DSHOT_MIN_THROTTLE) ? PWM_RANGE_MIN : scaleRange(motorValue, DSHOT_MIN_THROTTLE, DSHOT_MAX_THROTTLE, PWM_RANGE_MIN + 1, PWM_RANGE_MAX);
        }
        break;
    case false:
#endif
    default:
        externalValue = motorValue;
        break;
    }

    return externalValue;
}
