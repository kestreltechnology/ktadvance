/* NOTE - eventually this file will be automatically updated using a Perl script that understand
 * the naming of test case files, functions, and namespaces.
 */

#include <time.h>   /* for time() */
#include <stdlib.h> /* for srand() */

#include "std_testcase.h"
#include "testcases.h"

int main(int argc, char * argv[]) {

	/* seed randomness */

	srand( (unsigned)time(NULL) );

	globalArgc = argc;
	globalArgv = argv;

#ifndef OMITGOOD

	/* Calling C good functions */
	/* BEGIN-AUTOGENERATED-C-GOOD-FUNCTION-CALLS */

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_01_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_01_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_02_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_02_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_03_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_03_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_04_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_04_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_05_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_05_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_06_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_06_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_07_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_07_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_08_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_08_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_09_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_09_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_10_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_10_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_11_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_11_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_12_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_12_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_13_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_13_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_14_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_14_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_15_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_15_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_16_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_16_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_17_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_17_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_18_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_18_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_21_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_21_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_22_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_22_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_31_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_31_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_32_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_32_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_34_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_34_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_41_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_41_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_42_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_42_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_44_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_44_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_45_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_45_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_51_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_51_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_52_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_52_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_53_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_53_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_54_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_54_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_61_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_61_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_63_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_63_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_64_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_64_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_65_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_65_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_66_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_66_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_67_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_67_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_68_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_68_good();



#endif /* OMITGOOD */

#ifndef OMITBAD

	/* Calling C bad functions */
	/* BEGIN-AUTOGENERATED-C-BAD-FUNCTION-CALLS */

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_01_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_01_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_02_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_02_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_03_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_03_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_04_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_04_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_05_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_05_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_06_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_06_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_07_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_07_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_08_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_08_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_09_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_09_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_10_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_10_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_11_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_11_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_12_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_12_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_13_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_13_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_14_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_14_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_15_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_15_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_16_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_16_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_17_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_17_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_18_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_18_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_21_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_21_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_22_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_22_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_31_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_31_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_32_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_32_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_34_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_34_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_41_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_41_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_42_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_42_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_44_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_44_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_45_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_45_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_51_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_51_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_52_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_52_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_53_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_53_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_54_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_54_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_61_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_61_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_63_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_63_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_64_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_64_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_65_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_65_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_66_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_66_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_67_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_67_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_68_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_68_bad();

	/* END-AUTOGENERATED-C-BAD-FUNCTION-CALLS */

#endif /* OMITBAD */

	return 0;

} 