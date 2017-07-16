## Juliet Test Suite Test Cases
source: NIST Software Assurance Reference Dataset (samate.nist.gov)

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
> cd ktadvance/advance/bin/juliet
> python chc_analyze_juliet.py CWE121/s01/CWE129_randQ
```
This will create a semantics directory in the juliet_v1.2/CWE121/s01/CWE129_randQ
directory with all analysis results. These results can then be queried by python
reporting scripts:
```
> cd ../reporting/juliet
> python chc_report_juliettest.py CWE121/s01/CWE129_randQ
```
to see a summary of the results for all flow variants in the test case, or
```
> python chc_report_juliettest_file.py CWE121/s01/CWE129_randQ x01.c
```
to see detailed results for all proof obligations, relative to the source code,
for a single flow variant in the test case. All flow variants are named x[nn].c,
where, for conciseness, the original name is replaced by the single character x,
followed by the original index of the flow variant.

### Scoring
Some tests have a scorekey.json file that contain a specification of
the primary proof obligations involved in the tested vulnerability. To
evaluate the analysis results against this score key (in the reporting/juliet
directory):
```
> python chc_score_juliettest.py CWE121/s01/char_type_overrun_memcpyQ
```
This will create a report of the status of all listed proof
obligations in each file of the test and a summary for all tests in
the test case, e.g., for the above test case:
```

test              violations                    safe-controls
         V    S    D    U    O                S    L    D    X    U    O
--------------------------------------------------------------------------------
01       3    0    0    0    0       |        3    0    0    0    0    0
02       3    0    0    0    0       |        6    0    0    0    0    0
03       3    0    0    0    0       |        6    0    0    0    0    0
04       3    0    0    0    0       |        6    0    0    0    0    0
05       3    0    0    0    0       |        6    0    0    0    0    0
06       3    0    0    0    0       |        6    0    0    0    0    0
07       3    0    0    0    0       |        6    0    0    0    0    0
08       3    0    0    0    0       |        6    0    0    0    0    0
09       3    0    0    0    0       |        6    0    0    0    0    0
10       3    0    0    0    0       |        6    0    0    0    0    0
11       3    0    0    0    0       |        6    0    0    0    0    0
12       3    0    0    0    0       |        6    0    0    0    0    0
13       3    0    0    0    0       |        6    0    0    0    0    0
14       3    0    0    0    0       |        6    0    0    0    0    0
15       3    0    0    0    0       |        6    0    0    0    0    0
16       3    0    0    0    0       |        3    0    0    0    0    0
17       3    0    0    0    0       |        3    0    0    0    0    0
18       3    0    0    0    0       |        3    0    0    0    0    0
--------------------------------------------------------------------------------
total   54    0    0    0    0       |       96    0    0    0    0    0
```
where the column headers stand for the following
- (violations): V:violation, S:found-safe, D:delegated, U:unknown,
O:other
- (safe-controls): S:stmt-safe, L:safe(invariants), D:delegated,
    X:dead-code, U:unknown, O:other

### Test Case Creation
To create a new test case:
- collect the source files for all C flow variants for a single functional variant
     in a file [functionalvariant-name]_src.tar.gz
- edit the file main_linux.c to only include calls to the flow variants included

To (re)create the semantics_linux.tar.gz file:
- extract [functionalvariant-name]_src.tar.gz
- (from advance/bin) run
```
> python chc_prepare_juliettest.py [relative-directory-name]
```
   This will rename the source files to their x[nn].c equivalents
- copy the following files from the testcasesupport directory into the test directory:
```
   > cp ../../../testsupport/io.c .
   > cp ../../../std_thread.c .
   > cp ../../../Makefile_ctests Makefile
```
- (from advance/bin/juliet), on a **linux platform**, run
```
   > python chc_parse_juliettest.py [relative-directory-name] --savesemantics
```
This will create the semantics_linux.tar.gz file, providing all information
necessary to perform analysis.
