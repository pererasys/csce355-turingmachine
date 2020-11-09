'''

Written by Andrew Perera
Copyright 2020

'''


class TuringMachine(object):

    def __init__(self, name="", function=None):
        if not function:
            raise Exception("You must provide a function for the TM.")

        self._prefix = name
        self._map = {}

        self._describe_function(function)

    def _is_final(self, state):
        '''
        Returns whether or not the tape is in a final state.
        @param state - str
        '''

        return state.split(self._prefix)[1] == "FINAL"

    def _build_description(self, vals):
        '''
        Builds a description for the given condition values.
        @param vals - list(str)
        '''

        state = vals[0]
        line_input = vals[1]

        description = {
            "next": vals[2],
            "write": vals[3],
            "direction": vals[4]
        }

        if state in self._map.keys():
            self._map[state].update({line_input: description})
        else:
            self._map.update({state: {line_input: description}})


    def _describe_function(self, filename):
        '''
        Creates a mapping for the given function description.
        @param filename - str
        '''

        file = open(filename)
        conditions = file.readlines()
        for line in [condition for condition in conditions if condition.strip()]:
            '''
            split the line into an array of strings
            Eg. [STATE] [INPUT] [NEXT] [DIR] -> [STATE, INPUT, NEXT, DIR]
            '''
            vals = line.split()

            self._build_description(vals)
        file.close()

    def read_tape(self, tape, position, state):
        '''
        Parses the tape by recursively going through the steps until
        it reaches the end of the tape or is in a final state.
        @param tape - list(str)
        @param position - int
        @param state - str
        '''

        if self._is_final(state):
            return "ACCEPTED", tape

        input_c = tape[position]
        path = self._map[state][input_c]

        direction = path['direction']
        next_path = path['next']
        tape[position] = path['write']

        if (position <= len(tape) - 1 or direction == "LEFT"):
            position += 1 if direction == 'RIGHT' else -1
            return self.read_tape(tape=tape, position=position, state=next_path)

        return "NOT ACCEPTED", tape

    def execute(self, filename):
        '''
        Reads each line of an input file as individual
        tapes and passes it to the function described.
        @param file - str
        '''

        file = open(filename)
        tapes = file.readlines()
        for tape in tapes:
            tape = list(tape.strip())
            status, output = self.read_tape(
                tape, position=1, state=f'{self._prefix}START')
            print(f"{status} - {''.join(output)}")
