## Samate Medium Test Cases
source: NIST Software Assurance Reference Dataset (samate.nist.gov)

Test cases number 1283 through 1310 from the NIST Software Assurance Reference
Dataset (samate.nist.gov). These test cases were contributed by Misha Zitser,
and are described in the paper "Testing Static Analysis Tools Using
Exploitable Overflows From Open Source Code", Misha Zitser, Richard Lippmann,
and Tim Leek, Proceedings of the 12th ACM SIGSOFT twelfth international symposium
on Foundations of software engineering, pages 97-106.

All test cases have been pre-parsed and are ready for analysis.

#### Quick Start
Set the PYTHONPATH:
```
> export PYTHONPATH=$HOME/ktadvance
```
or adapt for different location of the ktadvance directory.

To run the analysis on a test case (e.g., id1283):
```
> cd ktadvance/advance/cmdline/zitser
> python chc_analyze_zitser.py id1283
```
or to the run the analysis of all 28 test cases (id1283-1310):
```
> python chc_analyze_zitser_set.py
```
To see a summary of the analysis results:
```
> python chc_report_zitser.py id1283
```
or some more detailed results for a single c file:
```
> python chc_report_zitser_file.py id1283 realpath-bad.c
```
or all proof obligations displayed within the code for a single
function:
```
> python chc_report_zitser_function.py id1283 realpath-bad.c fb_realpath
```
which will output something like the following (partial output):
```
--------------------------------------------------------------------------------
477        if ((strlen(resolved)+1) > MAXPATHLEN)
--------------------------------------------------------------------------------
<A>  999    477  not-null(resolved)  --api--
                  delegating proof obligation to function api
<?> 1000    477  null-terminated(resolved)
                  --
<?> 1001    477  ptr-upper-bound(op:pluspi, exp1:resolved, exp2:null-terminator-pos(resolved), tgttype:char)
                  --
<?> 1002    477  initialized-range(resolved,null-terminator-pos(resolved))
                  --
 S  1003    477  pointer-cast(resolved, from:char,to:char)
                  source and target type are the same
 S  1004    477  initialized(resolved)
                  resolved is a function parameter
<?> 1005    477  valid-mem(resolved) 
                  --
 L  1006    477  lower-bound(resolved)
                  non-negative offset from base value: resolved
 L  1007    477  upper-bound(resolved)
                  externally provided address; dereferencability is checked as part of precondition
 L  1008    477  initialized(tmp___44)
                  assignedAt#477
 S  1009    477  int-underflow(plusa,tmp___44,1):iulong
                  underflow is well defined for unsigned types
 S  1010    477  int-overflow(plusa,tmp___44,1):iulong
                  overflow is well defined for unsigned types
```
where the symbols at the beginning of the line of each proof obligation denote the following:
-  S  statement valid (valid based solely on the statement itself and declarations)
-  L  function-valid (valid relative to function invariants)
- <A> delegated to the API (with the help of function invariants)
- <?> open
