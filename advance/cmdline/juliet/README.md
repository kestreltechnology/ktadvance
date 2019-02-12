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
> export PYTHONPATH=$HOME/ktadvannce
> cd ktadvance/advance/cmdline/juliet
> python chj_check_config.py
```
......  prints location of the C parser and analyzer, and a list of Juliet Tests present.
```
> python chj_analyze_juliettest.py CWE121/s01/CWE129_large
```
......  runs the analyzer on the 38 control and data-flow variants of CWE121/s01/CWE129_large.
```
> python chj_report_juliettest.py CWE121/s01/CWE129_large
```
......  prints a summary of the analysis results

[Example output](example_output/report_juliettest_output.txt)
```
> python  chj_score_juliettest.py CWE121/s01/CWE129_large
```
......  prints the results of comparing the analysis results with the scorekey for CWE121/s01/CWE129_large
[Example output](example_output/score_jjuliettest_output.txt)
