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
	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_01_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_01_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_02_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_02_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_03_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_03_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_04_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_04_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_05_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_05_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_06_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_06_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_07_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_07_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_08_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_08_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_09_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_09_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_10_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_10_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_11_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_11_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_12_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_12_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_13_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_13_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_14_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_14_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_15_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_15_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_16_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_16_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_17_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_17_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_18_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_18_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_21_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_21_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_22_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_22_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_31_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_31_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_32_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_32_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_34_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_34_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_41_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_41_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_42_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_42_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_44_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_44_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_45_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_45_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_51_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_51_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_52_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_52_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_53_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_53_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_54_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_54_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_61_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_61_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_63_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_63_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_64_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_64_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_65_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_65_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_66_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_66_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_67_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_67_good();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_68_good();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_68_good();


	/* END-AUTOGENERATED-C-GOOD-FUNCTION-CALLS */


#endif /* OMITGOOD */

#ifndef OMITBAD

	/* Calling C bad functions */
	/* BEGIN-AUTOGENERATED-C-BAD-FUNCTION-CALLS */
	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_01_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_01_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_02_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_02_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_03_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_03_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_04_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_04_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_05_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_05_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_06_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_06_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_07_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_07_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_08_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_08_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_09_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_09_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_10_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_10_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_11_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_11_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_12_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_12_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_13_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_13_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_14_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_14_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_15_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_15_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_16_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_16_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_17_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_17_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_18_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_18_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_21_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_21_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_22_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_22_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_31_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_31_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_32_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_32_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_34_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_34_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_41_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_41_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_42_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_42_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_44_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_44_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_45_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_45_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_51_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_51_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_52_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_52_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_53_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_53_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_54_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_54_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_61_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_61_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_63_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_63_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_64_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_64_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_65_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_65_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_66_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_66_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_67_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_67_bad();

	printLine("Calling CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_68_bad();");
	CWE122_Heap_Based_Buffer_Overflow__CWE131_memmove_68_bad();


	/* END-AUTOGENERATED-C-BAD-FUNCTION-CALLS */


#endif /* OMITBAD */

	return 0;

} 