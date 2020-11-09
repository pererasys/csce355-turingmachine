'''

Written by Andrew Perera
Copyright 2020

'''

import argparse

from turingmachine import TuringMachine

parser = argparse.ArgumentParser()

def main(topology, tape):
    tm = TuringMachine()
    tm.readTopology(topology)
    tm.execute(tape)


if __name__ == "__main__":
    parser.add_argument('-i', '--input', dest='input', help='File name of the input file.', required=True)
    parser.add_argument('-t', '--tape', dest='tape', help='File name of the tape.', required=True)
    options = parser.parse_args()

    main(topology=options.input, tape=options.tape)



