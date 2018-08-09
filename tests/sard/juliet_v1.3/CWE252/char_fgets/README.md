
From the C11 standard:
```
7.21.7.2 The fgets function Synopsis
     #include <stdio.h>
     char *fgets(char * restrict s, int n,
          FILE * restrict stream);
Description
The fgets function reads at most one less than the number of characters specified by n from the stream pointed to by stream into the array pointed to by s. No additional characters are read after a new-line character (which is retained) or after end-of-file. A null character is written immediately after the last character read into the array.
Returns
The fgets function returns s if successful. If end-of-file is encountered and no characters have been read into the array, the contents of the array remain unchanged and a null pointer is returned. If a read error occurs during the operation, the array contents are indeterminate and a null pointer is returned.
```

From the C99 standard:
```
7.19.7.2 Thefgetsfunction Synopsis
     #include <stdio.h>
     char *fgets(char * restrict s, int n,
          FILE * restrict stream);
Description
The fgets function reads at most one less than the number of characters specified by n from the stream pointed to by stream into the array pointed to by s. No additional characters are read after a new-line character (which is retained) or after end-of-file. A null character is written immediately after the last character read into the array.
Returns
The fgets function returns s if successful. If end-of-file is encountered and no characters have been read into the array, the contents of the array remain unchanged and a null pointer is returned. If a read error occurs during the operation, the array contents are indeterminate and a null pointer is returned.
```


