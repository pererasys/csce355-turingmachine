'''

Written by Andrew Perera
Copyright 2020

'''

import argparse

from turingmachine import TuringMachine

parser = argparse.ArgumentParser()


def main(which, topology, tape):
    tm = TuringMachine(which, function=topology)
    tm.execute(tape)


if __name__ == "__main__":
    parser.add_argument('-w', '--which', dest='which',
                        help='Prefix for all states.', required=True)
    parser.add_argument('-i', '--input', dest='input',
                        help='File name of the input file.', required=True)
    parser.add_argument('-t', '--tape', dest='tape',
                        help='File name of the tape.', required=True)
    options = parser.parse_args()

    main(which=options.which, topology=options.input, tape=options.tape)
