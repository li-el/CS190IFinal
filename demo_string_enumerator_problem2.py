#!/usr/bin/env python
import tyrell.spec as S
from tyrell.interpreter import PostOrderInterpreter
from tyrell.enumerator import SmtEnumerator, RelaxedRandomEnumerator
from tyrell.decider import Example, ExampleConstraintDecider, HighOrderConstraintDecider, ExampleConstraintPruningDecider
from tyrell.synthesizer import Synthesizer
from tyrell.logger import get_logger

logger = get_logger('tyrell')

class ToyInterpreter(PostOrderInterpreter):

    def eval_get_delimiter(self, node, args):
        return args[0]

    def eval_get_token(self, node, args):
        return args[0]

    def eval_get_int(self, node, args):
        return int(args[0])

    def eval_concat(self, node, args):
        return args[0] + args[1]

    def eval_substr(self, node, args):
        arg_str = args[0]
        arg_pos0 = args[1]
        arg_pos1 = args[2]
        return arg_str[arg_pos0:arg_pos1]

    def eval_reverse(self, node, args):
        arg_str = args[0]
        return arg_str[::-1]

    def eval_sort(self, node, args):
        arg_str = args[0]
        return "".join(sorted(list(arg_str)))

    def eval_tolower(self, node, args):
        arg_str = args[0]
        return arg_str.lower()

    def eval_toupper(self, node, args):
        arg_str = args[0]
        return arg_str.upper()

    def eval_split(self, node, args):
        # TBD: implement the split function
        arg_str = args[0]
        arg_delim = args[1]
        return arg_str.split(arg_delim)

    def eval_join(self, node, args):
        # TBD: implement the join function
        arg_list = args[0]
        arg_str = args[1]
        return arg_str.join(arg_list)


def main():
    logger.info('Parsing Spec...')
    # TBD: parse the DSL definition file and store it to `spec`
    spec = S.parse_file('example/simplestring2.tyrell')
    logger.info('Parsing succeeded')
    logger.info(spec)

    logger.info('Building synthesizer...')
    synthesizer = Synthesizer(
        enumerator=RelaxedRandomEnumerator(spec, max_depth=3, min_depth=0, seed=None),
        decider=ExampleConstraintDecider(
            spec=spec, # TBD: provide the spec here
            interpreter=ToyInterpreter(), # Question Hole
            examples=[
                # Example(input=["a", "b"], output="ab"), # plus(@param0, @param1)
                # Example(input=["b", "a"], output="ab"), # plus(@param1, @param0)
                Example(input=[["Resident", "Evil", "Village"]], output="Resident*Evil*Village")
            ] # TBD: provide the example here
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
