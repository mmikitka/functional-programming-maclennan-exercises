def prefix(x, S):
    if S:
        return [x] + S
    else:
        return [x]

def rest(S):
    if len(S) > 1:
        return S[1:]
    return []

def first(S):
    if S:
        return S[0]
    else:
        return []

def second(S):
    return first(rest(S))
