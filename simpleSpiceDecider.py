#!/usr/bin/env python

import tyrell.spec as Stuff
from tyrell.interpreter import PostOrderInterpreter
from tyrell.enumerator import SmtEnumerator, RelaxedRandomEnumerator
from tyrell.decider import Example, ExampleConstraintDecider, SimpleSpiceDecider, ExampleConstraintPruningDecider
from tyrell.synthesizer import Synthesizer
from tyrell.logger import get_logger
from skidl import *
from skidl.pyspice import *
logger = get_logger('tyrell')
class Circuitsv():
    def __init__(self):
        self.circuit = Circuit()
        self.vin = Net('VI')
        self.vout = Net('VO')
        self.ground = Net('GND')
        self.circuit += self.vin, self.vout, self.ground
    def reinit(self):
        self.circuit = Circuit()
        self.vin = Net('VI')
        self.vout = Net('VO')
        self.ground = Net('GND')
        self.circuit += self.vin, self.vout, self.ground

class ToyInterpreter(PostOrderInterpreter):
    def __init__(self, circuit):
        self.circuit = circuit
    def eval_get_Resistance(self, node, args):
        return int(args[0])

    def eval_get_outnet(self, node, args):
        return self.circuit.vout

    def eval_startCon(self, node, args):
        self.circuit.vin += args[0][1]
        return self.circuit

    def eval_Rout(self, node, args):
        with self.circuit.circuit:
            r = R(value = args[1])
            r[2]+=args[0]
        return r

    def eval_Nout(self, node, args):
        with self.circuit.circuit:
            n = Net()
            n += args[0][1]
        return n

    def eval_GR(self, node, args):
        self.circuit.ground += args[0][1]
        return self.circuit.ground

    #Abstract Interpreter
    def apply_vin(self, val):
        return val

    def apply_vout(self, val):
        return val

    def apply_ground(self, val):
        return val



def main():
    logger.info('Parsing Spec...')
    # TBD: parse the DSL definition file and store it to `spec`
    spec = Stuff.parse_file('example/try.tyrell')
    logger.info('Parsing succeeded')
    circ = Circuitsv()

    logger.info('Building synthesizer...')
    synthesizer = Synthesizer(
        enumerator=RelaxedRandomEnumerator(spec, max_depth=6, min_depth=0, seed=None),
        decider=SimpleSpiceDecider(
            spec=spec, # TBD: provide the spec here
            interpreter=ToyInterpreter(circ),
            examples=[Example(input=[circ],output=[0.,0.03333333, 0.06666667, 0.1 ,0.13333333, 0.16666667, 0.2 ,0.23333333,0.26666667,0.3,0.33333333])] # TBD: provide the example here
        )
    )
    logger.info('Synthesizing programs...')

    prog = synthesizer.synthesize()
    if prog is not None:
        logger.info('Solution found: {}'.format(prog))
    else:
        logger.info('Solution not found!')


if __name__ == '__main__':
    logger.setLevel('DEBUG')
    main()
