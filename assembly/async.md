### Week 7 Async Assignment:
Assembly and machine languages

*Please answer the questions below in the async channel!*

1. The following LMC program is supposed to add two input numbers, add them, subtract the third input from the sum, and output the result, i.e. OUT = IN1 + IN2 -- IN3.
  *numeric code*
  ```
  901
  399
  901
  199
  399
  901
  299
  902
  000
  ```
Your task:
Convert from numeric into mnemonic code. A helpful guide the the LMC instruction set can be found HERE.
The program doesn’t work as intended.  Identify what’s wrong with the program as is.
Modify the program so that it works correctly. Include your code

---
In mnemonic code, the above is:
  ```
  INP
  STA 99
  INP
  ADD 99
  STA 99
  INP
  SUB 99
  OUT
  HLT
  ```




2. Next, you’ll write your own LMC program.  *Hint*: Build your program up one step at a time, like any other coding task. Implement your program on an LMC simulator like this one.

*mild*: Write an LMC program that takes two inputs and produces the larger of the two values as an output
