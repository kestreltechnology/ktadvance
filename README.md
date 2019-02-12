# KT Advance
### C Source Code Analyzer for Memory Safety

The software in this repository is restricted to those explicitly
given access by Kestrel Technology.

IDENTIFICATION AND ASSERTION OF RESTRICTIONS ON THE GOVERNMENT’S USE,
RELEASE, OR DISCLOSURE OF TECHNICAL DATA AND COMPUTER SOFTWARE

Rights In Technical Data—Noncommercial Items

FAR Supplement: 252.227-7013

# Quick Start

### System Requirements
* **Platform**: macOS or Linux

  The KT Advance C Source Analyzer consists of two parts that are run separately and may be run on different platforms:
   * a front-end parser (```parseFile```); this program is an extension of the CIL parser-front end, developed by George Necula at UC Berkeley, and now maintained by INRIA, France;
   * the KT Advance Analyzer (```ktadvance```); this program generates the proof obligations, and performs invariant generation by abstract interpretation to discharge the proof obligations.

   Both programs are provided in executable form for macOS (suffix ```mac```) and Linux (suffix ```linux```). The correct version for your platform is set automatically in the ```bin/Config.py``` file.

* **Utility Program**: The front-end parser makes use of the utility ```bear``` to record and replay the actions performed by the makefile when compiling an application. This utility is usually available via a package manager.

* **Other Dependencies**: The analyzer and the Python scripts make use of JAR files, which require a working Java installation.


### Organization

This repository is organized as follows:
* **advance**: Python scripts and programs to run the analysis and view the results.
* **doc**: containing PDF files for the reference manual and the user manual.
* **tests***: regression tests and other test cases, several of which have been pre-parsed, which are provided to illustrate the use and functionality of the analyzer; each subdirectory has a ```README``` file that describes the origin and structure of the test cases in that directory.


### General Use Guidelines

The analysis consists of two phases that may be performed on different platforms:
1. **Parsing**: This phase takes as input the original source code, a Makefile (if there is more than
   one source file), and, in case of library includes, the library header files resident on the system.
   This phase produces as output a set of XML files that completely capture the semantics of the application, and are the sole input for the Analysis phase.

   Because of the dependency on the resident system library header files it is generally recommended to perform this phase of the analysis on a Linux system, because of its more standard library environment than macOS (the CIL parser also may have issues with some of the Darwin constructs on macOS).

2. **Analysis**: This phase takes as input the XML files produced by the parsing phase. As long as the source code is not modified, the analysis can be run several times without having to repeat the parsing step. The Analysis step can be run on either macOS or Linux, independently of where the parsing step was performed, as it operates solely on the XML files produced and is not dependent on any external programs or library headers.

For several of the test cases in ```tests/sard/kendra``` and for all of the test cases in ```tests/sard/juliet_v1.2```
the parsing step has already been performed (on Linux) and the results are checked in in files named
```semantics_linux.tar.gz```. These gzipped ```tar``` files contain all XML files necessary for the analysis, and thus to analyze these files the parsing phase can be skipped altogether.


### Getting Started

At this point all interactions with the KT Advance C Analyzer are
performed via Python scripts, from the command line. It is recommended
to use Python 2.7. (Most of the Python code is compatible with
Python 3.x, but some file system interactions may not be at this
point).

All scripts to interact with the analyzer are in the directory
```ktadvance/advance/cmdline```. This directory has a few subdirectories
with scripts dedicated to some of the test sets in the ```ktadvance/tests```
directory, as follows:

- **kendra**: scripts to analyze and report on the test cases in
     ```tests/sard/kendra```
- **zitser**: scripts to analyze and report on the test cases in
     ```tests/sard/zitser```
- **juliet**: scripts to analyze and report on sets of test cases in
     ```tests/sard/juliet-1.3``` ([quickstart instructions](advance/cmdline/juliet/README.md))

The remaining two subdirectories in the ```advance/cmdline``` directory
contain scripts that can be used to parse, analyze, and
report on new files and projects:

- **sfapp**: scripts to analyze an application that consists of a
     single C file that can be compiled directly with GCC (without a
     makefile). See the ```README.md``` file in this directory for a walk-through of the command scripts available.
- **mfapp**: scripts to analyze an application that comes with a
	makefile. It is expected that the makefile exists (that is,
	a configure script has already been run, if necessary).
