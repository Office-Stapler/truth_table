import pytest
import hypothesis

from Truth_Table import Truth_Table
from generate_numberinput import generate

def test_simple():
    funcs = ['a&b', 'a|b', 'a^b']
    for func in funcs:
        table = Truth_Table(func, 2)
        if '&' in func:
            assert table.output == [0,0,0,1]
        elif '|' in func:
            assert table.output == [0,1,1,1]
        else:
            assert table.output == [0,1,1,0]

