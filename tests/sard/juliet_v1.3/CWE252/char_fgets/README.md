
## CWE252_Unchecked_Return_Value__char_fgets

Not checking the return value does not in itself lead to undefined
behavior. An error during reading, however, may leave the values in
the receiving array indeterminate, which can be considered equivalent
to an uninitialized memory region. Hence we associate the proof obligation
uninitialized-range with the statement that reads the memory region.

** Note **
The C Standard omits specifying the case where n=1: In this case no
bytes get written, so it is not guaranteed that the null-terminating
byte gets written in this case.  Given that this case is omitted from
the specification it may be considered undefined behavior.

### Reference

** C11: 7.21.7.2 The fgets function Synopsis **
```
     #include <stdio.h>
     char *fgets(char * restrict s, int n,
     FILE * restrict stream);
```	 
** Description **
The fgets function reads at most one less than the number of characters
specified by n from the stream pointed to by stream into the array pointed
to by s. No additional characters are read after a new-line character
(which is retained) or after end-of-file. A null character is written
immediately after the last character read into the array.

** Returns **
The fgets function returns s if successful. If end-of-file is encountered
and no characters have been read into the array, the contents of the array
remain unchanged and a null pointer is returned. If a read error occurs
during the operation, the array contents are indeterminate and a null
pointer is returned.


** C99: 7.19.7.2 Thefgetsfunction Synopsis **
```
     #include <stdio.h>
     char *fgets(char * restrict s, int n,
     FILE * restrict stream);
```	 
** Description **
The fgets function reads at most one less than the number of characters specified
by n from the stream pointed to by stream into the array pointed to by s. No
additional characters are read after a new-line character (which is retained) or
after end-of-file. A null character is written immediately after the last
character read into the array.

** Returns **
The fgets function returns s if successful. If end-of-file is encountered and no
characters have been read into the array, the contents of the array remain
unchanged and a null pointer is returned. If a read error occurs during the
operation, the array contents are indeterminate and a null pointer is returned.



