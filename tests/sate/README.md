## Test Applications from the NIST SATE competitions

Static Analysis Tool Exposition (SATE) has been organized at regular intervals by NIST
over the past decade to advance research in and improvement of static analysis tools
([https://samate.nist.gov/SATE.html]).

This directory contains a few pre-parsed applications from the c track of the first
few occurences of this competition:

- **2008**
  - lighttpd-1.4.18
  - nagios-2.10/base
  - naim-0.11.8.3.1


### Current results (last updated 2017-08-08)

```
                      stmt   local     api    post  global    open   total
---------------------------------------------------------------------------------
nagios/base          80355   52157    2815     642    3086   35232  174287
naim                 79606   37182    5273    1264   12816   32377  168518


                       stmt   local     api    post  global    open
---------------------------------------------------------------------------------
nagios/base           46.10   29.93    1.62    0.37    1.77   20.21
naim                  47.24   22.06    3.13    0.75    7.61   19.21
```
