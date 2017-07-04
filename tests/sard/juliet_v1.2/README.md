## Juliet Test Suite Test Cases

A subset of the collection of test cases, developed by the NSA Center for
Assured Software, as provided in the NIST SARD repository, samate.nist.gov.

#### Organization
The test cases are organized in a similar way as the original Test Suite,
except that the file hierarchy is extended by one level to create separate
directories for each functional variant, that solely contain the flow
variants for that functional variant. Furthermore, C++ variants have been
removed.

Each functional variant directory contains the following files:
- **[name]_src.tar.gz**: the original c source files
- **main_linux.c**: a reduced version of the original main_linux.c file with
     only calls to the flow variants included in this directory
- **semantics_linux.tar.gz**: the result of preprocessing and parsing the
     source files (on a linux platform) into KT Advance Analyzer input format
     
These files provide all necessary information for the analysis; the analysis
can be run on any platforms; all platform dependencies are included in the files.

### Quick Start
Set the PYTHONPATH:
```
> export PYTHONPATH=$HOME/ktadvance
```
or adapt for different location of the ktadvance directory.

To run the analysis of a Juliet Test Case:
```
> cd ktadvance/advance/bin
> python chc_analyze_juliet.py CWE121/s01/CWE129_randQ
```
This will create a semantics directory in the juliet_v1.2/CWE121/s01/CWE129_randQ
directory with all analysis results. These results can then be queried by python
reporting scripts:
```
> cd ../reporting
> python chc_report_juliet.py CWE121/s01/CWE129_randQ
```
to see a summary of the results for all flow variants in the test case, or
```
> python chc_report_juliet_file.py CWE121/s01/CWE129_randQ x01.c
```
to see detailed results for all proof obligations, relative to the source code,
for a single flow variant in the test case. All flow variants are named x[nn].c,
where, for conciseness, the original name is replaced by the single character x,
followed by the original index of the flow variant.

### Test Case Creation
To create a new test case:
- collect the source files for all C flow variants for a single functional variant
     in a file [functionalvariant-name]_src.tar.gz
- edit the file main_linux.c to only include calls to the flow variants included

To (re)create the semantics_linux.tar.gz file:
- extract [functionalvariant-name]_src.tar.gz
- (from advance/bin) run
```
> python chc_prepare_juliet.py [relative-directory-name]
```
   This will rename the source files to their x[nn].c equivalents
- copy the following files from the testcasesupport directory into the test directory:
```
   > cp ../../../testsupport/io.c .
   > cp ../../../std_thread.c .
   > cp ../../../Makefile_ctests Makefile
```
- (from advance/bin), on a **linux platform**, run
```
   > python chc_parse_juliet.py [relative-directory-name] --savesemantics
```
This will create the semantics_linux.tar.gz file, providing all information
necessary to perform analysis.
