'''

Written by Andrew Perera
Copyright 2020

'''

VALID = "Accepted"
INVALID = "Not Accepted"


def display_output(status, tape, output):
    '''Formats and prints the output for a tape reading.'''

    print(
        f'Input: {tape.strip()}\nStatus: {status}\nOutput: {"".join(output)}\n')


class TuringMachine():
    '''
    Maps a function description in a dict, and performs said function
    on a provided tape. Will also determine if the given language
    accepts the string.
    '''

    def __init__(self, function="", head=1):
        print(f"Initializing function: {function}\n")

        self._head = head
        self._prefix = function
        self._start_state = f'{self._prefix}START'
        self._final_state = f'{self._prefix}FINAL'
        self._map = {}

    def _is_final(self, state):
        '''Returns whether or not the tape is in a final state.'''

        return state == self._final_state

    def _build_description(self, vals):
        '''Builds a description for the given conditions.'''

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

    def _read_tape(self, tape):
        '''
        Parses the tape by looping through the steps until
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
            next_state = path['next']
            tape[position] = path['write']

            if position <= len(tape) - 1 or direction == "LEFT":
                position += 1 if direction == 'RIGHT' else -1
                state = next_state
            else:
                return INVALID, tape

        return VALID, tape

    def read(self, filename):
        '''
        Reads each line of an input file as individual
        tapes and passes it to the function described.
        '''

        file = open(filename)
        tapes = file.readlines()
        for i, tape in enumerate(tapes):
            stripped_tape = list(tape.strip())
            print(f"Reading tape {i + 1}...\n")
            status, output = self._read_tape(stripped_tape)
            display_output(status=status, tape=tapes[i], output=output)

    def describe(self, filename):
        '''Creates a mapping for the given function description.'''

        try:
            file = open(filename)
        except FileNotFoundError as file_e:
            raise FileNotFoundError(
                'Could not find a description of the function provided.') from file_e

        conditions = file.readlines()
        for line in [condition for condition in conditions if condition.strip()]:
            vals = line.split()
            self._build_description(vals)
        file.close()
