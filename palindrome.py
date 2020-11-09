'''

Written by Andrew Perera
Copyright 2020

'''

import argparse
import time

from turingmachine import TuringMachine

parser = argparse.ArgumentParser()


if __name__ == "__main__":
    # Start timer
    t_start = time.perf_counter()

    parser.add_argument('-n', '--name', dest='name',
                        help='The name of the function, also defines the prefix for all states.', required=True)
    parser.add_argument('-f', '--function', dest='function',
                        help='File name of the input file.', required=True)
    parser.add_argument('-t', '--tape', dest='tape',
                        help='File name of the tape.', required=True)
    options = parser.parse_args()

    tm = TuringMachine(name=options.name, function=options.function)
    tm.execute(options.tape)

    # End timer
    t_end = time.perf_counter()
    print(f"Completed in {t_end - t_start} seconds.")
