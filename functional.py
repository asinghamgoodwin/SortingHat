import sys


def indicator(a, b):
    """Test if last characters of two strings are different.

    Parameters
    ----------
    a : str
    b : str

    Returns
    -------
    1 if two strings end with different characters.
    0 otherwise.
    """
    # Bools are just integers
    return a[-1] != b[-1]


def lev(start, target, path=[]):
    """Get Levenshtein distance between two strings.

    Parameters
    ----------
    start: str
    target : str
    path : [str]

    Returns
    -------
    dist : int
        Levenshtein distance between two strings.
    path : [(str, str)]
        Tuples of strings passed through on way to finding the Levenshtein
        distance.
    """
    i = len(start)
    j = len(target)
    path = path[:] + [(start, target)]
    if min(i, j) == 0:
        return (max(i, j), path)
    else:
        ins = lev(start[:-1], target, path)
        deletion = lev(start, target[:-1], path)
        sub = lev(start[:-1], target[:-1], path)

        # add 1 to cost of ins and del
        ins_ = (ins[0] + 1, ins[1])
        deletion_ = (deletion[0] + 1, deletion[1])

        # add 1 to cost of sub if and only if last chars differ
        sub_ = (sub[0] + indicator(start, target), sub[1])

        # min of a list of tuples sorts on first elt of tuple
        return min(ins_, deletion_, sub_)

if __name__ == "__main__":
    start, target = sys.argv[1], sys.argv[2]
    print(lev(start, target))
