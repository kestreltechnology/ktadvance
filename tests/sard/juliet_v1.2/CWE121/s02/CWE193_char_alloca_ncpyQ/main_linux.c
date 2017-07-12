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


	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_01_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_01_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_02_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_02_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_03_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_03_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_04_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_04_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_05_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_05_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_06_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_06_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_07_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_07_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_08_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_08_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_09_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_09_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_10_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_10_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_11_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_11_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_12_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_12_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_13_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_13_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_14_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_14_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_15_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_15_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_16_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_16_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_17_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_17_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_18_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_18_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_31_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_31_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_32_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_32_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_34_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_34_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_41_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_41_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_44_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_44_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_45_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_45_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_51_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_51_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_52_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_52_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_53_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_53_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_54_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_54_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_63_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_63_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_64_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_64_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_65_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_65_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_66_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_66_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_67_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_67_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_68_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_68_good();

	/* END-AUTOGENERATED-C-GOOD-FUNCTION-CALLS */


#endif /* OMITGOOD */

#ifndef OMITBAD

	/* Calling C bad functions */
	/* BEGIN-AUTOGENERATED-C-BAD-FUNCTION-CALLS */


	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_01_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_01_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_02_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_02_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_03_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_03_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_04_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_04_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_05_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_05_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_06_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_06_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_07_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_07_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_08_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_08_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_09_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_09_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_10_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_10_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_11_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_11_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_12_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_12_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_13_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_13_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_14_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_14_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_15_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_15_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_16_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_16_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_17_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_17_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_18_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_18_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_31_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_31_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_32_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_32_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_34_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_34_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_41_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_41_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_44_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_44_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_45_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_45_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_51_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_51_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_52_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_52_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_53_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_53_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_54_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_54_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_63_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_63_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_64_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_64_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_65_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_65_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_66_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_66_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_67_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_67_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_68_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE193_char_alloca_ncpy_68_bad();

	/* END-AUTOGENERATED-C-BAD-FUNCTION-CALLS */


#endif /* OMITBAD */

	return 0;

} 