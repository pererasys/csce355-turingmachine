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
