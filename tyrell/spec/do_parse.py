from .parser import Lark_StandAlone
from .desugar import desugar
from ..logger import get_logger
logger = get_logger('tyrell.desugar')

# This has to be global since Lark_StandAlone() is not re-entrant.
# See https://github.com/lark-parser/lark/issues/299
parser = Lark_StandAlone()


def parse(input_str):
    '''
    Parse Tyrell spec from an input string.
    May raise either ``ParseError`` or ``ParseTreeProcessingError``.
    '''
    parse_tree = parser.parse(input_str)
    return desugar(parse_tree)


def parse_file(file_path):
    '''
    Parse Tyrell spec from an input file path.
    May raise either ``ParseError`` or ``ParseTreeProcessingError``.
    '''
    logger.info('Here')
    with open(file_path, 'r') as f:
        spec_str = f.read()
    logger.info('Complete')
    return parse(spec_str)
