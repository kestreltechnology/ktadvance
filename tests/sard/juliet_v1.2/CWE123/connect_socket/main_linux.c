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
	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_01_good();");
	CWE123_Write_What_Where_Condition__connect_socket_01_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_02_good();");
	CWE123_Write_What_Where_Condition__connect_socket_02_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_03_good();");
	CWE123_Write_What_Where_Condition__connect_socket_03_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_04_good();");
	CWE123_Write_What_Where_Condition__connect_socket_04_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_05_good();");
	CWE123_Write_What_Where_Condition__connect_socket_05_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_06_good();");
	CWE123_Write_What_Where_Condition__connect_socket_06_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_07_good();");
	CWE123_Write_What_Where_Condition__connect_socket_07_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_08_good();");
	CWE123_Write_What_Where_Condition__connect_socket_08_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_09_good();");
	CWE123_Write_What_Where_Condition__connect_socket_09_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_10_good();");
	CWE123_Write_What_Where_Condition__connect_socket_10_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_11_good();");
	CWE123_Write_What_Where_Condition__connect_socket_11_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_12_good();");
	CWE123_Write_What_Where_Condition__connect_socket_12_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_13_good();");
	CWE123_Write_What_Where_Condition__connect_socket_13_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_14_good();");
	CWE123_Write_What_Where_Condition__connect_socket_14_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_15_good();");
	CWE123_Write_What_Where_Condition__connect_socket_15_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_16_good();");
	CWE123_Write_What_Where_Condition__connect_socket_16_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_17_good();");
	CWE123_Write_What_Where_Condition__connect_socket_17_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_18_good();");
	CWE123_Write_What_Where_Condition__connect_socket_18_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_21_good();");
	CWE123_Write_What_Where_Condition__connect_socket_21_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_22_good();");
	CWE123_Write_What_Where_Condition__connect_socket_22_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_31_good();");
	CWE123_Write_What_Where_Condition__connect_socket_31_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_32_good();");
	CWE123_Write_What_Where_Condition__connect_socket_32_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_34_good();");
	CWE123_Write_What_Where_Condition__connect_socket_34_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_41_good();");
	CWE123_Write_What_Where_Condition__connect_socket_41_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_42_good();");
	CWE123_Write_What_Where_Condition__connect_socket_42_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_44_good();");
	CWE123_Write_What_Where_Condition__connect_socket_44_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_45_good();");
	CWE123_Write_What_Where_Condition__connect_socket_45_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_51_good();");
	CWE123_Write_What_Where_Condition__connect_socket_51_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_52_good();");
	CWE123_Write_What_Where_Condition__connect_socket_52_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_53_good();");
	CWE123_Write_What_Where_Condition__connect_socket_53_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_54_good();");
	CWE123_Write_What_Where_Condition__connect_socket_54_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_61_good();");
	CWE123_Write_What_Where_Condition__connect_socket_61_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_63_good();");
	CWE123_Write_What_Where_Condition__connect_socket_63_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_64_good();");
	CWE123_Write_What_Where_Condition__connect_socket_64_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_65_good();");
	CWE123_Write_What_Where_Condition__connect_socket_65_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_66_good();");
	CWE123_Write_What_Where_Condition__connect_socket_66_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_67_good();");
	CWE123_Write_What_Where_Condition__connect_socket_67_good();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_68_good();");
	CWE123_Write_What_Where_Condition__connect_socket_68_good();

	/* END-AUTOGENERATED-C-GOOD-FUNCTION-CALLS */



#endif /* OMITGOOD */

#ifndef OMITBAD

	/* Calling C bad functions */
	/* BEGIN-AUTOGENERATED-C-BAD-FUNCTION-CALLS */
	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_01_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_01_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_02_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_02_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_03_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_03_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_04_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_04_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_05_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_05_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_06_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_06_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_07_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_07_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_08_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_08_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_09_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_09_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_10_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_10_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_11_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_11_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_12_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_12_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_13_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_13_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_14_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_14_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_15_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_15_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_16_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_16_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_17_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_17_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_18_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_18_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_21_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_21_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_22_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_22_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_31_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_31_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_32_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_32_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_34_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_34_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_41_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_41_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_42_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_42_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_44_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_44_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_45_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_45_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_51_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_51_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_52_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_52_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_53_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_53_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_54_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_54_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_61_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_61_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_63_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_63_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_64_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_64_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_65_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_65_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_66_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_66_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_67_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_67_bad();

	printLine("Calling CWE123_Write_What_Where_Condition__connect_socket_68_bad();");
	CWE123_Write_What_Where_Condition__connect_socket_68_bad();

	/* END-AUTOGENERATED-C-BAD-FUNCTION-CALLS */


#endif /* OMITBAD */

	return 0;

} 
