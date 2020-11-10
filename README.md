# CSCE355 Turing Machine

## Functions

### Recognizing Palindromes

**Description**

The input string of 0 and 1 symbols is tested
to see if it is a palindrome. If it is, the TM halts and accepts. If it is
not, the TM halts without accepting.

**Command**

```
python3 main.py -n PALINDROME -f tm_PALINDROME.txt -t xinputPALINDROME.txt
```

### Ones Complement

**Description**

The input string of 0 and 1 symbols is treated as a
binary number. The TM should write the ones’ complement in place
of the number presented as input on the TM tape. Since this is a core
subprogram to be used for other arithmetic, the TM should not finish
and accept until the tape head is positioned once again on the leftmost
non-blank character of the input string

**Command**

```
python3 main.py -n COMPLEMENT -f tm_COMPLEMENT.txt -t xinputCOMPLEMENT.txt
```

### Incrementing

**Description**

The input string of 0 and 1 symbols is treated as a binary
number n in backwards order from the usual way in which numbers
are written. That is, the number is to be read left to right instead of
right to left. The TM should increment the number by 1 so that it is
now the binary number that is n + 1. Since this is a core subprogram
to be used for other arithmetic, the TM should not finish and accept
until the tape head is positioned once again on the leftmost non-blank
character of the input string.

**Command**

```
python3 main.py -n INCREMENT -f tm_INCREMENT.txt -t xinputINCREMENT.txt
```

### Decrementing

**Description**

The input string of 0 and 1 symbols is treated as a binary
number n in backwards order from the usual way in which numbers
are written. That is, the number is to be read left to right instead of
right to left. The TM should decrement the number by 1 so that it is
now the binary number that is n − 1. Note that decrementing, that is,
subtracting 1, can be done by doing a ones’ complement, an increment,
and a ones’ complement. Since this is a core subprogram to be used for
other arithmetic, the TM should not finish and accept until the tape
head is positioned once again on the leftmost non-blank character of
the input string

**Command**

```
python3 main.py -n DECREMENT -f tm_DECREMENT.txt -t xinputDECREMENT.txt
```

### Divisible by 3

**Description**

The input string of 0 and 1 symbols is treated as a binary
number n, written in left-to-right order. The TM should determine if n
is a multiple of 3. If so, it should halt and accept. If not, it should halt
without accepting. Note that this can be done by subtracting 3 (binary 11) from the input number, moving right to left and subtracting if the
bit is a 1. If this process results in 0, then n is divisible by 3. If it does
not result in 0, then n is not divisible by 3

**Command**

```
python3 main.py -n DIVBYTHREE -f tm_DIVBYTHREE.txt -t xinputDIVBYTHREE.txt
```

### Zero Counter

**Description**

A Turing Machine that will read its input tape as a binary number
n and write on that tape the binary number that is the number of zeros on
the input tape.

**Command**

```
python3 main.py -n ZEROCOUNTER -f tm_ZEROCOUNTER.txt -t xinputZEROCOUNTER.txt
```

## Other Information

### Arguments

```
python3 main.py [-h] -n NAME -f FUNCTION -t TAPE

optional arguments:
  -h, --help                        Help.
  -n NAME, --name NAME              The name of the function, also defines the prefix for all states.
  -f FUNCTION, --function FUNCTION  File name of the input file.
  -t TAPE, --tape TAPE              File name of the tape.
```

### Linter Output

```
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```
