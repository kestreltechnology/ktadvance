# KT Advance: Juliet Test command scripts
Scripts to analyze, score, and report Juliet Tests with the KT Advance C Analyzer.

### quick start

If you have not yet checked out the repository:
```
> cd
> git clone https://github.com/kestreltechnology/ktadvance.git
```
Set the PYTHONPATH environment variable and check the configuration
(adapt for local location of the repository):
```
> export PYTHONPATH=$HOME/ktadvance
> cd ktadvance/advance/cmdline/juliet
> python chj_check_config.py
```
......  prints location of the C parser and analyzer, and a list of Juliet Tests present.
```
> python chc_analyze_juliettest.py CWE121/s01/CWE129_large
```
......  runs the analyzer on the 38 control and data-flow variants of CWE121/s01/CWE129_large.
```
> python chc_report_juliettest.py CWE121/s01/CWE129_large
```
......  prints a summary of the analysis results

[Example output](example_output/report_juliettest_output.txt)
```
> python  chc_score_juliettest.py CWE121/s01/CWE129_large
```
......  prints the results of comparing the analysis results with the scorekey for CWE121/s01/CWE129_large

[Example output](example_output/score_juliettest_output.txt)
```
> python  chc_juliet_dashboard.py
```
......  prints an overview of all Juliet Tests that have been analyzed and scored so far

[Example output](example_output/juliet_dashboard_output.txt)

For each CWE the output shows how the analysis results compare with the score key, e.g., for CWE123:
```
test                                             violations                     safe-controls
                                           V    S    D    U    O          S    D    X    U    O
-------------------------------------------------------------------------------------------------------
CWE123
connect_socket                            18    0    0   20    0   |     31    0    0   22    0
fgets                                     25    0    0   13    0   |     33    0    0   20    0
listen_socket                             18    0    0   20    0   |     33    0    0   20    0
-------------------------------------------------------------------------------------------------------
total                                     61    0    0   53    0   |     97    0    0   62    0
```
The headings of the columns under violations indicate the following:
V: corresponding ppo's reported as violations
S: corresponding ppo's reported as safe
D: corresponding ppo's reported as delegated, but no closed spo's
U: corresponding ppo's reported as open
O: other result

The headings of the columns under safe-controls indicate the following:
S: corresponding ppo's reported as safe
D: corresponding ppo's reported as delegated, but no closed spo's
X: corresponding ppo's reported as dead-code
U: corresponding ppo's reported as open
O: other result
