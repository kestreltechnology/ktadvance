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

To run the analysis of a test set:
```
> cd ktadvance/advance/bin
> python chc_test_kendra_set.py id115Q
```
or to run the analysis of all test sets:
```
> python chc_test_kendra_sets.py
```
To see the proof obligations and analysis results of a particular
test:
```
> cd ../reporting
> python chc_report_kendra_ppos.py id115.c
```
or, to see a summary of the results for all tests:
```
> python chc_dashboard_kendra.py
```
or, to see the predicates of proof obligations involved in the
targeted violation:
```
> python chc_dashboard_kendra.py --predicates
```
