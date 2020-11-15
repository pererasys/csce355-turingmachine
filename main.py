'''

Written by Andrew Perera
Copyright 2020

'''

import argparse
import time

from turingmachine import TuringMachine

parser = argparse.ArgumentParser()


if __name__ == "__main__":
    parser.add_argument('-f', '--function',
                        dest='function',
                        help='The name of the function, also defines the prefix for all states.',
                        required=True)
    parser.add_argument('-t', '--tape', dest='tape',
                        help='File name of the tape.', required=True)

    options = parser.parse_args()

    # start timer
    t_start = time.perf_counter()

    tm = TuringMachine(function=options.function)
    tm.describe(f'tm_{options.function}.txt')
    tm.read(options.tape)

    # end timer
    t_end = time.perf_counter()

    print(f"Completed in {t_end - t_start} seconds.")
