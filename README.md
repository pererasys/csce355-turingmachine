# CSCE355 Turing Machine

## Functions

### Recognizing Palindromes

**Description**

The input string of 0 and 1 symbols is tested
to see if it is a palindrome. If it is, the TM halts and accepts. If it is
not, the TM halts without accepting.

**Command**

```
python3 main.py -n PALINDROME -f tm_PALINDROME.txt -t xinput.txt
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
python3 main.py -n COMPLEMENT -f tm_COMPLEMENT.txt -t xinput.txt
```

## Other Information

### Linter Output

```
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```
