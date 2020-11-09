'''

Written by Andrew Perera
Copyright 2020

'''

VALID = "Accepted"
INVALID = "Not Accepted"


def display_output(status, tape, output):
    '''
    Formats and prints the output for a tape reading.
    '''

    print(
        f'Input: {tape.strip()}\nStatus: {status}\nOutput: {"".join(output)}\n')


class TuringMachine():
    '''
    Maps a function description in a dict, and performs said function
    on a given tape. Will also determine if the given language
    will accept the string.
    '''

    def __init__(self, name="", head=1):
        self._head = head
        self._prefix = name
        self._start_state = f'{self._prefix}START'
        self._final_state = f'{self._prefix}FINAL'
        self._map = {}

    def _is_final(self, state):
        '''Returns whether or not the tape is in a final state.'''

        return state.split(self._prefix)[1] == "FINAL"

    def _build_description(self, vals):
        '''Builds a description for the given condition values.'''

        state = vals[0]
        line_input = vals[1]

        description = {
            "next": vals[2],
            "write": vals[3],
            "direction": vals[4]
        }

        try:
            self._map[state].update({line_input: description})
        except KeyError:
            self._map.update({state: {line_input: description}})

    def describe(self, filename):
        '''Creates a mapping for the given function description.'''

        file = open(filename)
        conditions = file.readlines()
        for line in [condition for condition in conditions if condition.strip()]:
            vals = line.split()
            self._build_description(vals)
        file.close()

    def read_tape(self, tape):
        '''
        Parses the tape by recursively going through the steps until
        it reaches the end of the tape or is in a final state.
        '''
        position = self._head
        state = self._start_state

        while not self._is_final(state):
            input_c = tape[position]

            try:
                path = self._map[state][input_c]
            except KeyError:
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
        '''
        print(f"Program: {self._prefix}\n")
        file = open(filename)
        tapes = file.readlines()
        for i, tape in enumerate(tapes):
            stripped_tape = list(tape.strip())
            print(f"Reading tape {i + 1}...\n")
            status, output = self.read_tape(stripped_tape)
            display_output(status=status, tape=tapes[i], output=output)
