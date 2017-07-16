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


	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_01_good();");
	CWE191_Integer_Underflow__char_min_multiply_01_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_02_good();");
	CWE191_Integer_Underflow__char_min_multiply_02_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_03_good();");
	CWE191_Integer_Underflow__char_min_multiply_03_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_04_good();");
	CWE191_Integer_Underflow__char_min_multiply_04_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_05_good();");
	CWE191_Integer_Underflow__char_min_multiply_05_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_06_good();");
	CWE191_Integer_Underflow__char_min_multiply_06_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_07_good();");
	CWE191_Integer_Underflow__char_min_multiply_07_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_08_good();");
	CWE191_Integer_Underflow__char_min_multiply_08_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_09_good();");
	CWE191_Integer_Underflow__char_min_multiply_09_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_10_good();");
	CWE191_Integer_Underflow__char_min_multiply_10_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_11_good();");
	CWE191_Integer_Underflow__char_min_multiply_11_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_12_good();");
	CWE191_Integer_Underflow__char_min_multiply_12_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_13_good();");
	CWE191_Integer_Underflow__char_min_multiply_13_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_14_good();");
	CWE191_Integer_Underflow__char_min_multiply_14_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_15_good();");
	CWE191_Integer_Underflow__char_min_multiply_15_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_16_good();");
	CWE191_Integer_Underflow__char_min_multiply_16_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_17_good();");
	CWE191_Integer_Underflow__char_min_multiply_17_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_18_good();");
	CWE191_Integer_Underflow__char_min_multiply_18_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_21_good();");
	CWE191_Integer_Underflow__char_min_multiply_21_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_22_good();");
	CWE191_Integer_Underflow__char_min_multiply_22_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_31_good();");
	CWE191_Integer_Underflow__char_min_multiply_31_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_32_good();");
	CWE191_Integer_Underflow__char_min_multiply_32_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_34_good();");
	CWE191_Integer_Underflow__char_min_multiply_34_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_41_good();");
	CWE191_Integer_Underflow__char_min_multiply_41_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_42_good();");
	CWE191_Integer_Underflow__char_min_multiply_42_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_44_good();");
	CWE191_Integer_Underflow__char_min_multiply_44_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_45_good();");
	CWE191_Integer_Underflow__char_min_multiply_45_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_51_good();");
	CWE191_Integer_Underflow__char_min_multiply_51_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_52_good();");
	CWE191_Integer_Underflow__char_min_multiply_52_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_53_good();");
	CWE191_Integer_Underflow__char_min_multiply_53_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_54_good();");
	CWE191_Integer_Underflow__char_min_multiply_54_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_61_good();");
	CWE191_Integer_Underflow__char_min_multiply_61_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_63_good();");
	CWE191_Integer_Underflow__char_min_multiply_63_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_64_good();");
	CWE191_Integer_Underflow__char_min_multiply_64_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_65_good();");
	CWE191_Integer_Underflow__char_min_multiply_65_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_66_good();");
	CWE191_Integer_Underflow__char_min_multiply_66_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_67_good();");
	CWE191_Integer_Underflow__char_min_multiply_67_good();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_68_good();");
	CWE191_Integer_Underflow__char_min_multiply_68_good();

	/* END-AUTOGENERATED-C-GOOD-FUNCTION-CALLS */


#endif /* OMITGOOD */

#ifndef OMITBAD

	/* Calling C bad functions */
	/* BEGIN-AUTOGENERATED-C-BAD-FUNCTION-CALLS */

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_01_bad();");
	CWE191_Integer_Underflow__char_min_multiply_01_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_02_bad();");
	CWE191_Integer_Underflow__char_min_multiply_02_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_03_bad();");
	CWE191_Integer_Underflow__char_min_multiply_03_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_04_bad();");
	CWE191_Integer_Underflow__char_min_multiply_04_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_05_bad();");
	CWE191_Integer_Underflow__char_min_multiply_05_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_06_bad();");
	CWE191_Integer_Underflow__char_min_multiply_06_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_07_bad();");
	CWE191_Integer_Underflow__char_min_multiply_07_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_08_bad();");
	CWE191_Integer_Underflow__char_min_multiply_08_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_09_bad();");
	CWE191_Integer_Underflow__char_min_multiply_09_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_10_bad();");
	CWE191_Integer_Underflow__char_min_multiply_10_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_11_bad();");
	CWE191_Integer_Underflow__char_min_multiply_11_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_12_bad();");
	CWE191_Integer_Underflow__char_min_multiply_12_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_13_bad();");
	CWE191_Integer_Underflow__char_min_multiply_13_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_14_bad();");
	CWE191_Integer_Underflow__char_min_multiply_14_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_15_bad();");
	CWE191_Integer_Underflow__char_min_multiply_15_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_16_bad();");
	CWE191_Integer_Underflow__char_min_multiply_16_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_17_bad();");
	CWE191_Integer_Underflow__char_min_multiply_17_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_18_bad();");
	CWE191_Integer_Underflow__char_min_multiply_18_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_21_bad();");
	CWE191_Integer_Underflow__char_min_multiply_21_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_22_bad();");
	CWE191_Integer_Underflow__char_min_multiply_22_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_31_bad();");
	CWE191_Integer_Underflow__char_min_multiply_31_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_32_bad();");
	CWE191_Integer_Underflow__char_min_multiply_32_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_34_bad();");
	CWE191_Integer_Underflow__char_min_multiply_34_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_41_bad();");
	CWE191_Integer_Underflow__char_min_multiply_41_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_42_bad();");
	CWE191_Integer_Underflow__char_min_multiply_42_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_44_bad();");
	CWE191_Integer_Underflow__char_min_multiply_44_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_45_bad();");
	CWE191_Integer_Underflow__char_min_multiply_45_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_51_bad();");
	CWE191_Integer_Underflow__char_min_multiply_51_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_52_bad();");
	CWE191_Integer_Underflow__char_min_multiply_52_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_53_bad();");
	CWE191_Integer_Underflow__char_min_multiply_53_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_54_bad();");
	CWE191_Integer_Underflow__char_min_multiply_54_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_61_bad();");
	CWE191_Integer_Underflow__char_min_multiply_61_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_63_bad();");
	CWE191_Integer_Underflow__char_min_multiply_63_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_64_bad();");
	CWE191_Integer_Underflow__char_min_multiply_64_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_65_bad();");
	CWE191_Integer_Underflow__char_min_multiply_65_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_66_bad();");
	CWE191_Integer_Underflow__char_min_multiply_66_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_67_bad();");
	CWE191_Integer_Underflow__char_min_multiply_67_bad();

	printLine("Calling CWE191_Integer_Underflow__char_min_multiply_68_bad();");
	CWE191_Integer_Underflow__char_min_multiply_68_bad();


	/* END-AUTOGENERATED-C-BAD-FUNCTION-CALLS */


#endif /* OMITBAD */

	return 0;

} 
