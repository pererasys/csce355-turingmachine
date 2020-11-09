'''

Written by Andrew Perera
Copyright 2020

'''

import json


class TuringMachine(object):

    def __init__(self):
        self._position = 1
        self._topology = {}
        self._current_state = None

    def readTopology(self, file):
        file = open(file)
        lines = file.readlines()
        for line in lines:
            self._position = 1
            steps = line.split()

            if line == lines[0]:
                self._start_state = steps[0]
                self._current_state = steps[0]

            if len(steps) > 0:
                description = {
                    f'{steps[0]}<-{steps[1]}': {
                        "next": steps[2],
                        "write": steps[3],
                        "direction": steps[4]
                    }
                }
                self._topology.update(description)

        file.close()

    def parse_tape(self, tape):
        if self._position > len(tape) - 1 or "FINAL" in self._current_state:
            return tape

        path = None
        
        path = self._topology[f'{self._current_state}<-{tape[self._position]}']

        direction = path['direction']
        next_path = path['next']
        tape[self._position] = str(path['write'])

        if (self._position <= len(tape) - 1 or direction == "LEFT"):
            self._current_state = next_path
            if direction == 'LEFT':
                self._position -= 1
            else:
                self._position += 1

            return self.parse_tape(tape)

        return tape

    def execute(self, file):
        file = open(file)
        tapes = file.readlines()
        for tape in tapes:
            self._position = 1
            self._current_state = self._start_state
            tape = list(tape.strip())
            output = self.parse_tape(tape)
            print(''.join(output))
