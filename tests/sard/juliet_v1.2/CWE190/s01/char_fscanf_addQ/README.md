## CWE190_Integer_overflow__char_fscanf_add

#### Intended Flaw
```
char data,result;
fscanf(stdin, "%c", &data)
result = data + 1
```


