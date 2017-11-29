## Samate Small Test Cases
source: NIST Software Assurance Reference Dataset (samate.nist.gov)

A subset of the collection of test cases developed by Kendra Kratkiewicz
(described in Kendra Kratkiewicz, Richard Lippmann, A Taxonomy of Buffer Overflows
for Evaluating Static and Dynamic Software Testing Tools, 2004), obtained
from the NIST Software Assurance Reference Dataset (samate.nist.gov)

#### Organization
The test cases are organized in groups of four related test cases, where the
first three test cases have a given vulnerability with varying magnitude of
overflow and in the fourth case that vulnerability is fixed (or absent). The
names of the tests refer to the sequence numbers in the SARD repository, and
the name of the group refers to the sequence number of the first test. For
example, the test group id115Q contains the test cases id115.c, id116.c,
id116.c, and id117.c . 

#### Quick Start
Set the PYTHONPATH:
```
> export PYTHONPATH=$HOME/ktadvance
```
or adapt for different location of the ktadvance directory.

To see a list of the test sets currently provided:
```
> cd ktadvance/advance/cmdline/kendra
> python chc_list_kendratests.py
```
To run the analysis of a test set:
```
> cd ktadvance/advance/cmdline/kendra
> python chc_test_kendra_set.py id115Q
```
or to run the analysis of all test sets:
```
> python chc_test_kendra_sets.py
```
To see the proof obligations and analysis results of a particular
test:
```
> python chc_report_kendratest_file.py id115.c
```
To see a summary of the results for all tests:
```
> python chc_kendra_dashboard.py
```
or, to see the predicates of proof obligations involved in the
targeted violation:
```
> python chc_kendra_dashboard.py --predicates
```

Some of the kendra directories show sample output for the file report
and some discussion on the approach used in that particular example,
or the reason for remaining open proof obligations:
* **id115Q**: First example
* **id151Q**: Library function postconditions and macros
* **id167Q**: Supporting proof obligations
* **id263Q**: Postconditions
* **id295Q**: Open proof obligations

