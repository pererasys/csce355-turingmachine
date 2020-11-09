'''

Written by Andrew Perera
Copyright 2020

'''

VALID = "Accepted"
INVALID = "Not Accepted"


class TuringMachine(object):

    def __init__(self, name="", head=1):
        self._head = head
        self._prefix = name
        self._start_state = f'{self._prefix}START'
        self._final_state = f'{self._prefix}FINAL'
        self._map = {}

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

        try:
            self._map[state].update({line_input: description})
        except:
            self._map.update({state: {line_input: description}})

    def describe(self, filename):
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

    def read_tape(self, tape):
        '''
        Parses the tape by recursively going through the steps until
        it reaches the end of the tape or is in a final state.
        @param tape - list(str)
        @param position - int
        @param state - str
        '''
        position = self._head
        state = self._start_state

        while not self._is_final(state):
            input_c = tape[position]
    
            try:
                path = self._map[state][input_c]
            except:
                return INVALID, tape

            direction = path['direction']
            next_path = path['next']
            tape[position] = path['write']

            if position <= len(tape) - 1 or direction == "LEFT":
                position += 1 if direction == 'RIGHT' else -1
                state = next_path
            else:
                return INVALID, tape

        return VALID, tape

    def execute(self, filename):
        '''
        Reads each line of an input file as individual
        tapes and passes it to the function described.
        @param file - str
        '''

        file = open(filename)
        tapes = file.readlines()
        for tape in tapes:
            stripped_tape = list(tape.strip())
            status, output = self.read_tape(stripped_tape)
            self._display_output(status=status, tape=tape, output=output)

    def _display_output(self, status, tape, output):
        print(f'Tape: {tape.strip()}\nStatus: {status}\nOutput: {"".join(output)}\n')