'''

Written by Andrew Perera
Copyright 2020

'''

import json


class TuringMachine(object):

    def __init__(self, prefix="", function=None):
        if not function:
            raise Exception("You must provide a function for the TM.")

        self._prefix = prefix
        self._map = {}

        self._describe_function(function)

    def _is_final(self, state):
        '''

        Returns whether or not the state provided is a final state

        @param state - str

        '''

        return state.split(self._prefix)[1] == "FINAL"

    def _describe_function(self, filename):
        '''

        Creates a mapping for the given file-based description

        @param filename - str

        '''

        file = open(filename)
        lines = file.readlines()
        for line in lines:
            steps = line.split()

            if len(steps) > 0:
                description = {
                    f'{steps[0]}<-{steps[1]}': {
                        "next": steps[2],
                        "write": steps[3],
                        "direction": steps[4]
                    }
                }
                self._map.update(description)

        file.close()

    def parse_tape(self, tape, position, state):
        '''

        Parses the tape by recursively going through the steps until
        it reaches the end of the tape or is in a final state.

        @param tape - list(str)
        @param position - int
        @param state - str

        '''

        if self._is_final(state):
            return "ACCEPTED", tape

        path = self._map[f'{state}<-{tape[position]}']

        direction = path['direction']
        next_path = path['next']
        tape[position] = str(path['write'])

        if (position <= len(tape) - 1 or direction == "LEFT"):
            position += 1 if direction == 'RIGHT' else -1
            return self.parse_tape(tape=tape, position=position, state=next_path)

        return "NOT ACCEPTED", tape

    def execute(self, file):
        file = open(file)
        tapes = file.readlines()
        for tape in tapes:
            tape = list(tape.strip())
            status, output = self.parse_tape(tape, position=1, state=f'{self._prefix}START')
            print(f"{status} - {''.join(output)}")
