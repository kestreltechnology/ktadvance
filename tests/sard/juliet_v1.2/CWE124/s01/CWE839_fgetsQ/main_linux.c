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

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_01_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_01_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_02_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_02_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_03_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_03_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_04_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_04_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_05_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_05_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_06_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_06_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_07_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_07_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_08_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_08_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_09_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_09_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_10_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_10_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_11_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_11_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_12_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_12_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_13_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_13_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_14_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_14_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_15_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_15_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_16_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_16_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_17_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_17_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_18_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_18_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_21_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_21_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_22_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_22_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_31_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_31_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_32_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_32_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_34_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_34_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_41_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_41_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_42_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_42_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_44_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_44_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_45_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_45_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_51_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_51_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_52_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_52_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_53_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_53_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_54_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_54_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_61_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_61_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_63_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_63_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_64_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_64_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_65_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_65_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_66_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_66_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_67_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_67_good();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_68_good();");
	CWE124_Buffer_Underwrite__CWE839_fgets_68_good();

	/* END-AUTOGENERATED-C-GOOD-FUNCTION-CALLS */



#endif /* OMITGOOD */

#ifndef OMITBAD

	/* Calling C bad functions */
	/* BEGIN-AUTOGENERATED-C-BAD-FUNCTION-CALLS */

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_01_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_01_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_02_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_02_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_03_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_03_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_04_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_04_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_05_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_05_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_06_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_06_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_07_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_07_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_08_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_08_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_09_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_09_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_10_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_10_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_11_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_11_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_12_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_12_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_13_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_13_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_14_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_14_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_15_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_15_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_16_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_16_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_17_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_17_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_18_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_18_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_21_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_21_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_22_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_22_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_31_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_31_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_32_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_32_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_34_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_34_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_41_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_41_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_42_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_42_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_44_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_44_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_45_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_45_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_51_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_51_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_52_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_52_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_53_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_53_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_54_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_54_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_61_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_61_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_63_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_63_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_64_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_64_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_65_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_65_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_66_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_66_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_67_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_67_bad();

	printLine("Calling CWE124_Buffer_Underwrite__CWE839_fgets_68_bad();");
	CWE124_Buffer_Underwrite__CWE839_fgets_68_bad();


	/* END-AUTOGENERATED-C-BAD-FUNCTION-CALLS */



#endif /* OMITBAD */

	return 0;

} 
