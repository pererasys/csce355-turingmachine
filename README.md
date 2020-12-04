# CSCE355 Turing Machine

## Function Descriptions

Function descriptions must adhere to this format

```
eg. A turing machine to increment a binary integer

INCREMENTSTART 0 INCREMENTTRANSITION 1 LEFT
INCREMENTSTART 1 INCREMENTSTART 0 RIGHT
INCREMENTSTART b INCREMENTTRANSITION 1 LEFT

INCREMENTTRANSITION 1 INCREMENTTRANSITION 1 LEFT
INCREMENTTRANSITION 0 INCREMENTTRANSITION 0 LEFT
INCREMENTTRANSITION b INCREMENTFINAL b RIGHT
```

## Tape format

Tapes (-t TAPE) must be of the format

```
b1001000bbbbbbbbbbbbbb
b0000bbbbbbbbbbbbbb
b111010100110000bbbbbbbbbbbbbb
...
```

Notice the leading 'b', this signifies a blank on the tape. The Turing Machine will automatically position itself over the starting position, the leftmost non-blank. Although traditional turing machines can have an arbitrary number of blanks to the left, in accordance with the guidelines of this project, all input strings must have exactly one leading blank, 'b'.

## How it works

When describing the function, we map the states and their inputs to a Python dict. This allows us to transition through the table quickly.

```
Map for the increment function shown above.

{
    "INCREMENTSTART": {
        "0": {
            "next": "INCREMENTTRANSITION",
            "write": "1",
            "direction": "LEFT"
        },
        "1": {
            "next": "INCREMENTSTART",
            "write": "0",
            "direction": "RIGHT"
        },
        "b": {
            "next": "INCREMENTTRANSITION",
            "write": "1",
            "direction": "LEFT"
        }
    },
    "INCREMENTTRANSITION": {
        "1": {
            "next": "INCREMENTTRANSITION",
            "write": "1",
            "direction": "LEFT"
        },
        "0": {
            "next": "INCREMENTTRANSITION",
            "write": "0",
            "direction": "LEFT"
        },
        "b": {
            "next": "INCREMENTFINAL",
            "write": "b",
            "direction": "RIGHT"
        }
    }
}
```

## Provided Functions

### Recognizing Palindromes

**Description**

The input string of 0 and 1 symbols is tested
to see if it is a palindrome. If it is, the TM halts and accepts. If it is
not, the TM halts without accepting.

**Command**

```
python3 main.py -f PALINDROME -t $1
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
python3 main.py -f COMPLEMENT -t $1
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
python3 main.py -f INCREMENT -t $1
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
python3 main.py -f DECREMENT -t $1
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
python3 main.py -f DIVBYTHREE -t $1
```

### Zero Counter

**Description**

A Turing Machine that will read its input tape as a binary number
n and write on that tape the binary number that is the number of zeros on
the input tape.

**Command**

```
python3 main.py -f ZEROCOUNT -t $1
```

## Other Information

### Arguments

```
python3 main.py [-h] -f FUNCTION -t TAPE

optional arguments:
  -h, --help                        Help.
  -f FUNCTION, --function FUNCTION  The name of the function, also defines the prefix for all states.
  -t TAPE, --tape TAPE              File name of the tape.
```

### Linter Output

```
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```
