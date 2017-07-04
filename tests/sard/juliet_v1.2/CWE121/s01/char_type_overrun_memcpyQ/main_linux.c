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
	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_01_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_01_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_02_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_02_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_03_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_03_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_04_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_04_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_05_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_05_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_06_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_06_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_07_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_07_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_08_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_08_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_09_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_09_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_10_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_10_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_11_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_11_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_12_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_12_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_13_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_13_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_14_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_14_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_15_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_15_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_16_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_16_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_17_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_17_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_18_good();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_18_good();

	/* END-AUTOGENERATED-C-GOOD-FUNCTION-CALLS */

#endif /* OMITGOOD */

#ifndef OMITBAD

	/* Calling C bad functions */
	/* BEGIN-AUTOGENERATED-C-BAD-FUNCTION-CALLS */
	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_01_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_01_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_02_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_02_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_03_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_03_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_04_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_04_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_05_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_05_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_06_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_06_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_07_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_07_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_08_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_08_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_09_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_09_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_10_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_10_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_11_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_11_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_12_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_12_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_13_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_13_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_14_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_14_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_15_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_15_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_16_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_16_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_17_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_17_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_18_bad();");
	CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_18_bad();

	/* END-AUTOGENERATED-C-BAD-FUNCTION-CALLS */




	

#endif /* OMITBAD */

	return 0;

} 
