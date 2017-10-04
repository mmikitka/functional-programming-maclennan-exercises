# Chapter 6: Higher-order Functions
from . import core

def mapf(f, S):
    """ Implementation of 'map f' (equation 6.7) """
    if not S:
        return []
    else:
        return core.prefix(f(core.first(S)), mapf(f, core.rest(S)))
