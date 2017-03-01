# -*- coding: utf-8 -*-

from .types import Environment, DiyLangError, Closure, String
from .ast import is_boolean, is_atom, is_symbol, is_list, is_closure, is_integer, is_string
from .parser import unparse

"""
This is the Evaluator module. The `evaluate` function below is the heart
of your language, and the focus for most of parts 2 through 6.

A score of useful functions is provided for you, as per the above imports,
making your work a bit easier. (We're supposed to get through this thing
in a day, after all.)
"""

def evaluate(ast, env):
    """Evaluate an Abstract Syntax Tree in the specified environment."""

    ops = ["+","-","/","*","mod",">","<"]

    if type(ast) is list:
        if ast[0] == "quote":
            return ast[1]
        elif ast[0] == "atom":
            rhs = evaluate(ast[1], env)
            return type(rhs) is not list
        elif ast[0] == "eq":
            param1 = evaluate(ast[1], env)
            if type(param1) is list:
                return False
            param2 = evaluate(ast[2], env)
            return param1 == param2
        elif len(ast) == 3:
            if ast[0] in ops:
                try:
                    operator = ast[0].replace("mod", "%")
                    arg1 = evaluate(ast[1], env)
                    arg2 = evaluate(ast[2], env)
                
                    to_eval = str(arg1) + " " + operator + " " + str(arg2)
                    return eval(to_eval)
                except:
                    raise DiyLangError

    return ast
