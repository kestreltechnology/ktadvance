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
	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_01_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_01_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_02_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_02_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_03_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_03_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_04_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_04_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_05_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_05_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_06_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_06_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_07_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_07_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_08_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_08_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_09_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_09_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_10_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_10_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_11_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_11_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_12_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_12_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_13_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_13_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_14_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_14_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_15_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_15_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_16_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_16_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_17_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_17_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_18_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_18_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_21_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_21_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_22_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_22_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_31_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_31_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_32_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_32_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_34_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_34_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_41_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_41_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_42_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_42_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_44_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_44_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_45_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_45_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_51_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_51_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_52_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_52_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_53_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_53_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_54_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_54_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_61_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_61_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_63_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_63_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_64_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_64_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_65_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_65_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_66_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_66_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_67_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_67_good();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_68_good();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_68_good();

#endif /* OMITGOOD */

#ifndef OMITBAD

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_01_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_01_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_02_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_02_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_03_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_03_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_04_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_04_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_05_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_05_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_06_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_06_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_07_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_07_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_08_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_08_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_09_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_09_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_10_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_10_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_11_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_11_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_12_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_12_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_13_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_13_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_14_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_14_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_15_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_15_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_16_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_16_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_17_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_17_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_18_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_18_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_21_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_21_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_22_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_22_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_31_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_31_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_32_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_32_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_34_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_34_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_41_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_41_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_42_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_42_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_44_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_44_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_45_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_45_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_51_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_51_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_52_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_52_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_53_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_53_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_54_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_54_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_61_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_61_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_63_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_63_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_64_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_64_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_65_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_65_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_66_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_66_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_67_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_67_bad();

	printLine("Calling CWE121_Stack_Based_Buffer_Overflow__CWE129_large_68_bad();");
	CWE121_Stack_Based_Buffer_Overflow__CWE129_large_68_bad();

#endif /* OMITBAD */

	return 0;

} 

