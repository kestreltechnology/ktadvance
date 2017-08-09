## Quick Start

All steps are to be performed from this directory.

For help with any of the scripts or to find out their arguments type:
```
> python <name of script> --help
```

Set the PYTHONPATH:
```
> export PYTHONPATH=$HOME/ktadvance
```
or the appropriate path if this repository is in a different location.

Create a c program, e.g., cprogram1.c:
```
int main(int argc, char **argv) {

  int a[10];
  int i;

  for (i=0 ; i < 10; i++) {
    a[i] = i;
  }
}
```

Parse the c program:
```
> python chc_parse_file.py ~/cprogram1.c

BLOCKS___', '-D_DARWIN_C_SOURCE', '-D_FORTIFY_SOURCE=0', '-fno-inline', '-fno-builtin', '-E', '-g', '-m64', '-o', 'cprogram1.i', 'cprogram1.c']
Result: 0
Parse file: ['/Users/henny/gitrepo/ktadvance/advance/bin/binaries/parseFile_mac', '-projectpath', '/Users/henny', '-targetdirectory', '/Users/henny/semantics/ktadvance', '/Users/henny/cprogram1.i']
Parsing /Users/henny/cprogram1.i
[ ; Users ; henny ; semantics ; ktadvance]
[/Users ; /Users/henny ; /Users/henny/semantics ; /Users/henny/semantics/ktadvance]
Saving 1 function file(s) ... 
Trying mkdir /Users/henny/semantics/ktadvance/cprogram1
Executing mkdir /Users/henny/semantics/ktadvance/cprogram1 (exitvalue: 0)

Saving function file: /Users/henny/semantics/ktadvance/cprogram1/cprogram1_main_cfun.xml

Saving cfile file: /Users/henny/semantics/ktadvance/cprogram1_cfile.xml
cprogram1.c:8: Warning: Body of function main falls-through. Adding a return statement
```
(Output is shown for MacOSX; it will look somewhat different on Linux).

Analyze the program:
> python chc_analyze_file.py ~/ cprogram1.c

Creating primary proof obligations for cprogram1.c
['/Users/henny/repo/CodeHawk/CHC/cchcmdline/canalyzer', '-summaries', '/Users/henny/gitrepo/ktadvance/advance/summaries/cchsummaries.jar', '-command', 'primary', '-cfile', 'cprogram1.c', '-nolinkinfo', '/Users/henny/semantics/ktadvance']
Opening /Users/henny/gitrepo/ktadvance/advance/summaries/cchsummaries.jar

Result: 0
Generating invariants for cprogram1.c
Opening /Users/henny/gitrepo/ktadvance/advance/summaries/cchsummaries.jar

Processing xml file for: cprogram1.c
main                                    :       26 (  0.01 sec) (new    26)
================================================================================
cprogram1.c                             :       26 (  0.01 sec) (new    26)


Result: 0
Checking proof obligations for cprogram1.c
Opening /Users/henny/gitrepo/ktadvance/advance/summaries/cchsummaries.jar

Processing xml file: cprogram1.c
main                                    :        8 (out of      8, 100.0%) (   0,    0) (safe)
================================================================================
cprogram1.c                             :        8 (out of      8, 100.0%) (   0,    0)


Result: 0
main
Generating invariants for cprogram1.c
Opening /Users/henny/gitrepo/ktadvance/advance/summaries/cchsummaries.jar

Processing xml file for: cprogram1.c
main                                    :       29 (  0.01 sec) (new     3)
================================================================================
cprogram1.c                             :       29 (  0.01 sec) (new     3)


Result: 0
Checking proof obligations for cprogram1.c
Opening /Users/henny/gitrepo/ktadvance/advance/summaries/cchsummaries.jar

Processing xml file: cprogram1.c
main                                    :        8 (out of      8, 100.0%) (   0,    0) (safe)
================================================================================
cprogram1.c                             :        8 (out of      8, 100.0%) (   0,    0)


Result: 0
main
Generating invariants for cprogram1.c
Opening /Users/henny/gitrepo/ktadvance/advance/summaries/cchsummaries.jar

Processing xml file for: cprogram1.c
main                                    :       29 (  0.01 sec) (new     0)
================================================================================
cprogram1.c                             :       29 (  0.01 sec) (new     0)


Result: 0
Checking proof obligations for cprogram1.c
Opening /Users/henny/gitrepo/ktadvance/advance/summaries/cchsummaries.jar

Processing xml file: cprogram1.c
main                                    :        8 (out of      8, 100.0%) (   0,    0) (safe)
================================================================================
cprogram1.c                             :        8 (out of      8, 100.0%) (   0,    0)


Result: 0
main
Generating invariants for cprogram1.c
Opening /Users/henny/gitrepo/ktadvance/advance/summaries/cchsummaries.jar

Processing xml file for: cprogram1.c
main                                    :       29 (  0.01 sec) (new     0)
================================================================================
cprogram1.c                             :       29 (  0.01 sec) (new     0)


Result: 0
Checking proof obligations for cprogram1.c
Opening /Users/henny/gitrepo/ktadvance/advance/summaries/cchsummaries.jar

Processing xml file: cprogram1.c
main                                    :        8 (out of      8, 100.0%) (   0,    0) (safe)
================================================================================
cprogram1.c                             :        8 (out of      8, 100.0%) (   0,    0)


Result: 0
```

Print a summary of the analysis results:
```
> python chc_report_file.py ~/ cprogram1.c

Primary Proof Obligations
functions    stmt   local     api    post  global    open   total
---------------------------------------------------------------
main          1       7       0       0       0       0       8
---------------------------------------------------------------
total         1       7       0       0       0       0       8
percent   12.50   87.50    0.00    0.00    0.00    0.00


Proof Obligation Statistics for file cprogram1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Primary Proof Obligations
                             stmt   local     api    post  global    open   total
---------------------------------------------------------------------------------
index-lower-bound               0       1       0       0       0       0       1
index-upper-bound               0       1       0       0       0       0       1
initialized                     0       4       0       0       0       0       4
int-overflow                    0       1       0       0       0       0       1
int-underflow                   1       0       0       0       0       0       1
---------------------------------------------------------------------------------
total                           1       7       0       0       0       0       8
percent                     12.50   87.50    0.00    0.00    0.00    0.00
```

Print all proof obligations in relation to the code for function main:
```
> python chc_report_function.py ~/ cprogram1.c main

Reading file /Users/henny/semantics/sourcefiles/cprogram1.c

Primary Proof Obligations for main
--------------------------------------------------------------------------------
3  int main(int argc, char **argv) {
4
5    int a[10];
6    int i;
7
8    for (i=0 ; i < 10; i++) {
--------------------------------------------------------------------------------
 L     1      8  initialized(i)      
                  assignedAt#8
 L     6      8  initialized(i)      
                  assignedAt#8
 S     7      8  int-underflow(plusa,i,1):iint
                  add non-negative number: value is 1
 L     8      8  int-overflow(plusa,i,1):iint
                  result of addition is less than MAX: satisfies((9 + 1) < 32767)
--------------------------------------------------------------------------------
9      a[i] = i;
--------------------------------------------------------------------------------
 L     2      9  index-lower-bound(i)
                  lower bound of index value range is non-negative: 0
 L     3      9  index-upper-bound(i, bound:10)
                  upper bound of index value range (9) is less than length 10
 L     4      9  initialized(i)      
                  assignedAt#8
 L     5      9  initialized(i)      
                  assignedAt#8
```
The output shows that all proof obligations have been discharged and found safe,
hence the program is free of memory-related vulnerabilities.
