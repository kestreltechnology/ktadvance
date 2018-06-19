## Juliet Test Suite Test Cases
source: NIST Software Assurance Reference Dataset (samate.nist.gov)

A subset of the collection of test cases, developed by the NSA Center for
Assured Software, as provided in the NIST SARD repository, samate.nist.gov.

#### Organization
The test cases are organized in a similar way as the original Test Suite,
except that the file hierarchy is extended by one level to create separate
directories for each functional variant that solely contain the flow (control flow/dataflow)
variants for that functional variant. Furthermore, C++ variants have been
removed.

Each functional variant directory contains the following files:
- **[name]_src.tar.gz**: the original c source files
- **semantics_linux.tar.gz**: the result of preprocessing and parsing the
     source files (on a linux platform) into KT Advance Analyzer input
     format
- **scorekey.json**: json file that identifies the type and locations
  of the vulnerabilities
     
These files provide all necessary information for the analysis; the analysis
can be run on any platform; all platform dependencies are included in the files.

### Quick Start
Set the PYTHONPATH:
```
> export PYTHONPATH=$HOME/ktadvance
```
or adapt for different location of the ktadvance directory.

To list the Juliet test cases currently provided in the tests
directory:
```
> cd ktadvance/advance/cmdline/juliet
> python chc_list_juliettests.py
```

To run the analysis of a Juliet Test Case select one of the paths listed
in the output of chc_list_juliettests and run (for example):
```
> python chc_analyze_juliet.py CWE121/s01/CWE129_rand
```
or, if you have multiple processors available,
```
> python chc_analyze_juliet.py CWE121/s01/CWE129_rand --maxprocesses 8
```
or any other number, dependent on your system.

This will create a semantics directory in the juliet_v1.2/CWE121/s01/CWE129_rand
directory with all analysis results. These results can then be queried by python
reporting scripts:
```
> python chc_report_juliettest.py CWE121/s01/CWE129_rand
```
to see a summary of the results for all flow variants in the test case, or
```
> python chc_report_juliettest_file.py CWE121/s01/CWE129_rand x01.c
```
to see detailed results for all proof obligations, relative to the source code,
for a single flow variant in the test case. Add the option --showcode
to see all proof obligations within the context of the program itself.

All flow variants are named x[nn].c,
where, for conciseness, the original name is replaced by the single character x,
followed by the original index of the flow variant.

### Scoring
Some tests have a scorekey.json file that contain a specification of
the primary proof obligations involved in the tested vulnerability. To
evaluate the analysis results against this score key:

```
> python chc_score_juliettest.py CWE121/s01/CWE129_rand
```
This will create a report of the status of all listed proof
obligations in each file of the test and a summary for all tests in
the test case, e.g., for the above test case:
```
test              violations                    safe-controls
         V    S    D    U    O                S    D    X    U    O
--------------------------------------------------------------------------------
01       0    0    0    1    0       |        2    0    0    0    0
02       0    0    0    1    0       |        3    0    0    0    0
03       0    0    0    1    0       |        3    0    0    0    0
04       0    0    0    1    0       |        4    0    0    0    0
05       0    0    0    1    0       |        4    0    0    0    0
06       0    0    0    1    0       |        4    0    0    0    0
07       0    0    0    1    0       |        4    0    0    0    0
08       0    0    0    1    0       |        4    0    0    0    0
09       0    0    0    1    0       |        4    0    0    0    0
10       0    0    0    1    0       |        4    0    0    0    0
11       0    0    0    1    0       |        4    0    0    0    0
12       0    0    0    1    0       |        5    0    0    0    0
13       0    0    0    1    0       |        4    0    0    0    0
14       0    0    0    1    0       |        4    0    0    0    0
15       0    0    0    1    0       |        4    0    0    0    0
16       0    0    0    1    0       |        2    0    0    0    0
17       0    0    0    1    0       |        2    0    0    0    0
18       0    0    0    1    0       |        2    0    0    0    0
21       0    0    1    0    0       |        3    0    0    0    0
22       0    0    1    0    0       |        3    0    0    0    0
31       0    0    0    1    0       |        2    0    0    0    0
32       0    0    0    1    0       |        1    0    0    1    0
34       0    0    0    1    0       |        1    0    0    1    0
41       0    0    1    0    0       |        2    0    0    0    0
42       1    0    0    0    0       |        2    0    0    0    0
44       0    0    1    0    0       |        2    0    0    0    0
45       0    0    0    1    0       |        2    0    0    0    0
51       0    0    1    0    0       |        2    0    0    0    0
52       0    0    1    0    0       |        2    0    0    0    0
53       0    0    1    0    0       |        2    0    0    0    0
54       0    0    1    0    0       |        2    0    0    0    0
61       1    0    0    0    0       |        2    0    0    0    0
63       0    0    1    0    0       |        2    0    0    0    0
64       0    0    0    1    0       |        1    0    0    1    0
65       0    0    1    0    0       |        2    0    0    0    0
66       0    0    0    1    0       |        1    0    0    1    0
67       0    0    0    1    0       |        1    0    0    1    0
68       0    0    0    1    0       |        2    0    0    0    0
--------------------------------------------------------------------------------
total    2    0   10   26    0       |      100    0    0    5    0
```
where the column headers stand for the following
- (violations): V:violation, S:found-safe, D:delegated, U:unknown, O:other
- (safe-controls): S:safe, D:delegated, X:dead-code, U:unknown,
O:other

For the violations block,
something is wrong with the analyzer if a proof obligation for a violation is proven
safe (i.e., if any of the numbers in the S column under violations is
non-zero). Analysis is incomplete if a proof obligation for a
violation is deferred to the caller, but the caller does not identify
it as a violation (column D), or if the proof obligation is still open
(column U).

Similarly for the safe-controls block, something is wrong if a
violation is indicated (i.e., if any of the numbers in the O column is
non-zero).

### Dashboard

To see a summary of the results of all test cases:
```
> python chc_juliet_dashboard.py
```
or a summary for the results of a particular control flow/dataflow
variant, say 01, the baseline variant:
```
> python chc_juliet_dashboard_variant.py 01
```
which will show the results for all x01.c files in all test cases.

Each of these will show an overall summary for all test cases, e.g.,
```
                            violation      safe-control     total
--------------------------------------------------------------------------------
ppos                           4907           9176          14083
reported                       2428           6305           8733
percent reported               49.5           68.7           62.0
--------------------------------------------------------------------------------
```
which gives the percentage of all proof obligations related to vulnerabilities
that were reported, and the percentage of all proof obligations related to the
fixed vulnerabilities.
