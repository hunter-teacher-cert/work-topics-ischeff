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
The problem is that the program doesn't properly compute the final operation, in which the third input is subtracted from the sum of the first two. (In one test I ran, the first number was 10, the second was 10, and the third was 5; 10 and 10 were successfully added to make 20, but then the program subtracted 20 from 5, not 5 from 20, outputting -15 instead of 15.)

The problem, in essence, is that the "SUB 99" command is telling the computer to subtract whatever is stored in the 99th mailbox from the input in the accumulator, when it should instead be subtracting whatever is in the accumulator from whatever is in the 99th mailbox.

One way around this is to


2. Next, you’ll write your own LMC program.  *Hint*: Build your program up one step at a time, like any other coding task. Implement your program on an LMC simulator like this one.

*mild*: Write an LMC program that takes two inputs and produces the larger of the two values as an output
