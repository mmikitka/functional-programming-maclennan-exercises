from . import core
import math

def elt(S, i):
    """ Retrieve the ith element of S (Section 3.1) """
    if i == 0:
        return core.first(S)
    else:
        return elt(core.rest(S), i - 1)

def cat(S, T):
    """ Catenate sequence S with sequence T (Section 3.2) """
    if not S:
        return T
    elif not T:
        return S
    else:
        return core.prefix(core.first(S), cat(core.rest(S), T))

def trans2(S, T):
    """ Join two sequences together, paired by the elements in the same position.
        It is assumed the length(S) == length(T) (Exercise 3.23) """
    if not S:
        return []
    else:
        return core.prefix([core.first(S), core.first(T)], trans2(core.rest(S), core.rest(T)))

def indsubst(x, i, S):
    """ The indexed substition of x for the ith element of S (Exercise 3.23) """
    if not S:
        return [x]
    elif i == 0:
        return core.prefix(x, core.rest(S))
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
    """ Replace all occurences of y in S with the elements of sequence T (Exercise 3.31) """
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
    """ Sum all elements of a sequence (Exercise 3.33) """
    if not S:
        return 0
    else:
        return core.first(S) + add(core.rest(S))

def prod(S):
    """ Multiply all elements of a sequence (Exercise 3.34) """
    if not S:
        return 1
    else:
        return core.first(S) * prod(core.rest(S))

def append(S):
    """ Cat reduction of a sequence of sequences (Exercise 3.36) """
    if not S:
        return []
    else:
        return cat(core.first(S), append(core.rest(S)))

def seqand(S):
    """ Return nil upon encountering the first nil in the sequence. Return the last element if all previous values are nil. (Exercise 3.37) """
    if not S:
        return []
    else:
        if not core.first(S):
            return []
        else:
            if len(S) == 1:
                return core.first(S)
            else:
                return seqand(core.rest(S))

def seqor(S):
    """ Return nil if all elements are nil. Return the first element that is not nil. (Exercise 3.38) """
    if not S:
        return []
    else:
        if core.first(S):
            return core.first(S)
        else:
            if len(S) == 1:
                return core.first(S)
            else:
                return seqor(core.rest(S))

def seqdif(S):
    """ Return the difference reduction of a sequence (Exercise 3.39) """
    if not S:
        return 0
    elif core.second(S):
        return core.first(S) - core.second(S) + seqdif(core.rest(core.rest(S)))
    else:
        return core.first(S)

def seqmin(S):
    """ Return the minimum value of a sequence (Exercise 3.40) """
    if not S:
        return None
    else:
        if len(S) == 1:
            return core.first(S)
        else:
            if core.first(S) < core.first(core.rest(S)):
                return seqmin(core.prefix(core.first(S), core.rest(core.rest(S))))
            else:
                return seqmin(core.rest(S))

def sublis(P, S):
    """ Perform the substition pairs of sequence P on sequence S (Exercise 3.41) """
    if not S or not P:
        return S
    else:
        return sublis(core.rest(P), subst(core.second(core.first(P)), core.first(core.first(P)), S))

def subpair(X, Y, S):
    """ Perform pair-wise substition of positional keys in X with positional values in Y on sequence S (Exercise 3.42) """
    if not X or not Y or not S:
        return S
    else:
        return subpair(core.rest(X), core.rest(Y), subst(core.first(Y), core.first(X), S))

def map_sin(S):
    """ Calculate the sine of every value in a sequence (Exercise 3.43) """
    if not S:
        return S
    else:
        return core.prefix(math.sin(core.first(S)), map_sin(core.rest(S)))

def map_prod(S):
    """ Calculate the product of every sequence in a sequence (Exercise 3.50) """
    if not S:
        return S
    else:
        return core.prefix(prod(core.first(S)), map_prod(core.rest(S)))

def vector_prod(S, T):
    """ Calculate the element-wise product of two sequences of the same length (Exercise 3.51) """
    if not S:
        return []
    else:
        return map_prod(trans2(S, T))

def map_dif(S):
    """ Calculate the difference mapping of a sequence (Exercise 3.54) """
    if not S:
        return []
    else:
        return core.prefix(seqdif(core.first(S)), map_dif(core.rest(S)))

def vector_dif(S, T):
    """ Calculate the element-wise difference of two sequences (Exercise 3.55) """
    if not S:
        return []
    else:
        return map_dif(trans2(S, T))

def seqinterval(m, n):
    """ Generate a sequence of numbers from m ... n - 1 (Section 3.6) """
    if m == n:
        return []
    elif m > n:
        return core.prefix(m - 1, seqinterval(m - 1, n))
    else:
        return core.prefix(m, seqinterval(m + 1, n))

def subseq(S, m, n):
    """ Return a sub-sequence of S from elements m to n (Exercise 3.63) """
    if m < 0:
        return subseq(S, len(S) + m, n)
    elif n < 0:
        return subseq(S, m, len(S) + n)
    elif m > len(S):
        return subseq(S, m - len(S), n)
    elif n > len(S):
        return subseq(S, m, n - len(S))

    if m == n:
        return []
    elif m > n:
        if n == 0:
            return cat(subseq(core.rest(S), m - 1, 0), [core.first(S)])
        else:
            return subseq(core.rest(S), m - 1, n - 1)
    elif m < n:
        if m == 0:
            return core.prefix(core.first(S), subseq(core.rest(S), 0, n - 1))
        else:
            return subseq(core.rest(S), m - 1, n - 1)
