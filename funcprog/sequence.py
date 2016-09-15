from . import core

def elt(S, i):
    """ Retrieve the ith element of S (Section 3.1) """
    if i == 0:
        return core.first(S)
    else:
        return elt(core.rest(S), i - 1)

def cat(S, T):
    """ Catenate sequence S with sequence T (Section 3.2) """
    if not S or not len(S):
        return T
    elif not T or not len(T):
        return S
    else:
        return core.prefix(core.first(S), cat(core.rest(S), T))

def indsubst(x, i, S):
    """ The indexed substition of x for the ith element of S (Exercise 3.23) """
    if not len(S) or i == 0:
        if S:
            return core.prefix(x, core.rest(S))
        else:
            return [x]
    elif i > 0:
        return core.prefix(core.first(S), indsubst(x, i - 1, core.rest(S)))

def subst1st(x, y, S):
    """ The first indexed substition of the value y with x in sequence S (Exercise 3.28) """
    if core.first(S) == y:
        return indsubst(x, 0, S)
    else:
        return core.prefix(core.first(S), subst1st(x, y, core.rest(S)))

def subst(x, y, S):
    """ Replace all occurrences of y with x (Exercise 3.29) """
    if core.first(S) == y:
        if len(S) > 1:
            return core.prefix(x, subst(x, y, core.rest(S)))
        else:
            return [x]
    else:
        if len(S) > 1:
            return core.prefix(core.first(S), subst(x, y, core.rest(S)))
        else:
            return S

def lsubst(T, y, S):
    """ Replace all occurences of y in S with the elements of sequence T """
    if core.first(S) == y:
        if len(S) > 1:
            return cat(T, lsubst(T, y, core.rest(S)))
        else:
            return T
    else:
        if len(S) > 1:
            return core.prefix(core.first(S), lsubst(T, y, core.rest(S)))
        else:
            return S

def add(S):
    """ Sum all elements of a sequence (Section 3.4) """
    if not S or not len(S):
        return 0
    else:
        return core.first(S) + add(core.rest(S))

def prod(S):
    """ Multiply all elements of a sequence (Exercise 3.34) """
    if not S or not len(S):
        return 1
    else:
        return core.first(S) * prod(core.rest(S))
