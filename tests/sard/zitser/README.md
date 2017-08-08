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
```
-  S  statement valid (valid based solely on the statement itself and declarations)
-  L  function-valid (valid relative to function invariants)
- <A> delegated to the API (with the help of function invariants)
- <?> open
```
The first number denotes the primary proof obligation identification number and the second
number is the line number in the file.

To see a summary for all zitser test cases:
```
python chc_zitser_dashboard.py
```
which, at the time of writing this, outputs:
```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Zitser test cases: id1283 - id1310
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Primary proof obligations

zitser testcase              stmt   local     api    post  global    open   total
---------------------------------------------------------------------------------
id1283                        735     356      49       0       0     345    1485
id1284                        620     267      42       0       0     280    1209
id1285                        860     201      19       0       2     395    1477
id1286                       1176     270      17       1       2     466    1932
id1287                        411     109      20       0       0     121     661
id1288                        370     114      20       0       0     120     624
id1289                        400     242      19      12       6     346    1025
id1290                        364     236      21      12       6     299     938
id1291                       1197     881      65      69       0     550    2762
id1292                       1198     893      62      75       0     537    2765
id1293                        790     472      19       4       0     622    1907
id1294                        905     472      19       4       0     689    2089
id1295                        293     150      49      15       0      86     593
id1296                        302     151      50      15       0      87     605
id1297                        334     300      35       2       6     405    1082
id1298                        702     636      33       2       6     681    2060
id1299                        382     175      48       3       0     483    1091
id1300                        479     172      52       3       0     501    1207
id1301                        417     202      55       0       0     135     809
id1302                        252     181      27       0       0      84     544
id1303                        248     158      10       0       0     229     645
id1304                        275     173      10       0       0     238     696
id1305                        422     184      27       1      21     133     788
id1306                        464     187      39       1      21     136     848
id1307                        127      42       3       0      17     112     301
id1308                        129      42       3       0      21     108     303
id1309                        715     509      33      16      17     795    2085
id1310                        727     513      33      16      17     803    2109
---------------------------------------------------------------------------------
total                       15294    8288     879     251     142    9786   34640
percent                     44.15   23.93    2.54    0.72    0.41   28.25

Secondary proof obligations

zitser testcase              stmt   local     api    post  global    open   total
---------------------------------------------------------------------------------
id1283                         13       2       3       0       0       0      18
id1284                         13       2       3       0       0       0      18
id1285                          0       0       1       0       0       6       7
id1286                         29       0       0       0       0       3      32
id1287                          2       3       1       0       0       6      12
id1288                          2       6       1       0       0       7      16
id1289                          2       4       0       0      11      26      43
id1290                          2       4       0       2      11      23      42
id1291                         14       0       3       3       0      19      39
id1292                         15       0       3       3       0      18      39
id1293                          0       1       3       0       0      21      25
id1294                          0       1       3       0       0      25      29
id1295                          0       0       0       0       0      19      19
id1296                          0       0       0       0       0      19      19
id1297                          2       0       0       0       0       0       2
id1298                          2       0       0       0       0       0       2
id1299                          1       0       0       0       0      15      16
id1300                          0       0       0       0       0      31      31
id1301                          0       0       0       0       0      11      11
id1302                          2       2       0       0       0       2       6
id1303                          1       1       0       0       0       0       2
id1304                          1       1       0       0       0       0       2
id1305                          4       2       2       0       0       1       9
id1306                          7       2       2       0       0       1      12
id1307                          0       0       0       0       1       0       1
id1308                          0       0       0       0       1       0       1
id1309                         18       0       0       0       0      54      72
id1310                         19       0       0       0       0      54      73
---------------------------------------------------------------------------------
total                         149      31      25       8      24     361     598
percent                     24.92    5.18    4.18    1.34    4.01   60.37

Proof obligation types

Primary proof obligations
                             stmt   local     api    post  global    open   total
---------------------------------------------------------------------------------
allocation-base                 0       0       4       0       0      10      14
cast                         1364      84      46      29       0     356    1879
common-base                     0      19       0       0       0      82     101
common-base-type                0      19       0       0       0      82     101
f-pre                           0       0       0       0       0      14      14
format-string                 593       0       0       0       0       2     595
global-mem                     87      16       8       6       0      14     131
index-lower-bound              93      12       0       0       0       2     107
index-upper-bound              83      12       0       0       0      12     107
initialized                   966    4285       7       6       6    1089    6359
initialized-range             769       0       0       0      12     526    1307
int-overflow                  218      13       0       7       0     151     389
int-underflow                 278      11       6       2       4      88     389
lower-bound                  1644    1166      20       4       2     732    3568
no-overlap                    106       0      22       2       2      42     174
non-negative                  179       0       0       0       0       0     179
not-null                     1138    1086     630      32      28    1083    3997
not-zero                        2       0       0       0       0       0       2
null-terminated               792       0       0       0      10     532    1334
pointer-cast                 1860       0       2       8       0      30    1900
ptr-lower-bound               720      11      18       6       2     140     897
ptr-upper-bound               804       6      27       6      14     637    1494
ptr-upper-bound-deref         122       8      50      96       2     598     876
signed-to-unsigned-cast       165      17       6      11       4      72     275
unsigned-to-signed-cast        12       0      12      36       0     205     265
upper-bound                  1558     823      21       0      18     996    3416
valid-mem                    1562     700       0       0      38    2291    4591
width-overflow                179       0       0       0       0       0     179
---------------------------------------------------------------------------------
total                       15294    8288     879     251     142    9786   34640
percent                     44.15   23.93    2.54    0.72    0.41   28.25

Secondary proof obligations
                             stmt   local     api    post  global    open   total
---------------------------------------------------------------------------------
allocation-base                 0       0       0       0       0      52      52
cast                           31       1       0       6       0      84     122
global-mem                     38       6       0       0       0       4      48
initialized                     0       0       0       0       4       7      11
int-underflow                   0       2       0       0       0       2       4
lower-bound                     0       0       0       0       0       6       6
no-overlap                      4       0       4       0       0      12      20
not-null                       28      18      13       1      20     105     185
pointer-cast                    0       0       0       0       0       4       4
ptr-upper-bound                11       3       2       0       0      39      55
ptr-upper-bound-deref           8       1       6       1       0      21      37
signed-to-unsigned-cast        29       0       0       0       0       4      33
unsigned-to-signed-cast         0       0       0       0       0       5       5
upper-bound                     0       0       0       0       0       7       7
value-constraint                0       0       0       0       0       9       9
---------------------------------------------------------------------------------
total                         149      31      25       8      24     361     598
percent                     24.92    5.18    4.18    1.34    4.01   60.37
```
