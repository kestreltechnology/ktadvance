## CWE190_Integer_overflow__char_fscanf_add

### Intended Flaw
```
void CWE190_Integer_Overflow__char_fscanf_add_01_bad()
{
    char data;
    data = ' ';
    /* POTENTIAL FLAW: Use a value input from the console */
    fscanf (stdin, "%c", &data);
    {
        /* POTENTIAL FLAW: Adding 1 to data could cause an overflow */
        char result = data + 1;
        printHexCharLine(result);
    }
}
```

### Actual Flaw

The intended flaw is described as an integer-over problem. There is,
however, no integer overflow. According to the C standard (6.3.1.8),
the operands in the expression are converted to **int** before
evaluating the expression (integer promotions are applied) and the
result is then cast back to the result type. Since the maximum value
of **data** is the maximum value of a **char**, adding 1 to that
value, represented as an **int**, does not result in overflow.

The subsequent conversion back to a **char**, instead, will result
in a different value, which is implementation-defined (6.3.1.3).
Below, as an example, we show the documentation for the GCC C
compiler.



### Reference

**C Standard, 6.3.1.1, paragraph 2**:

If an int can represent all values of the original type, the value is converted
to an int; otherwise, it is converted to an unsigned int. These are called the
integer promotions) All other types are unchanged by the integer promotions.


**C Standard, 6.3.1.3**:

1. When a value with integer type is converted to another integer type other than _Bool,
   if the value can be represented by the new type, it is unchanged.
2. Otherwise, if the new type is unsigned, the value is converted by repeatedly adding
   or subtracting one more than the maximum value that can be represented in the new
   type until the value is in the range of the new type.49)
3. Otherwise, the new type is signed and the value cannot be represented in it; either
   the result is implementation-defined or an implementation-defined signal is raised.

**C Standard, 6.3.1.8 Usual Arithmetic Conversions**:

This pattern is called the usual arithmetic conversions:

* First, if the corresponding real type of either operand is long double, the
  other operand is converted, without change of type domain, to a type whose
  corresponding real type is long double.

* Otherwise, if the corresponding real type of either operand is double, the
  other operand is converted, without change of type domain, to a type whose
  corresponding real type is double.

* Otherwise, if the corresponding real type of either operand is float, the
  other operand is converted, without change of type domain, to a type whose
  corresponding real type is float)
  
* Otherwise, the integer promotions are performed on both operands


**GNU C Compiler: implementation-defined behavior**:

*The result of, or the signal raised by, converting an integer to a signed integer type when the value cannot be represented in an object of that type (C90 6.2.1.2, C99 and C11 6.3.1.3).*
```
For conversion to a type of width N, the value is reduced modulo 2^N to be
within range of the type; no signal is raised.
```
[https://gcc.gnu.org/onlinedocs/gcc/Integers-implementation.html#Integers-implementation]
