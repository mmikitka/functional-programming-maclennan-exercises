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
    if S and len(S):
        return S[0]
    else:
        return None
