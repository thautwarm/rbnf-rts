"""
LOAD_FAST
STORE_FAST
BUILD_TUPLE
CALL_FUNCTION
RETURN_VALUE
MAKE_FUNCTION

match a of
| Int(x) -> y
| Str(y) -> x

"""

from astpretty import pprint
from ast import parse
import dis
