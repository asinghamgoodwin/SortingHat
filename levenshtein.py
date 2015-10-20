# figuring out the Levenshtein distance between two strings
# you're allowed to insert, delete, and swap, and each costs 1


def levenshtein(string1, string2):
    # determine which string is the startString (shorter)
    # and which is the the targetString (longer)
    if len(string1) > len(string2):
        startString = string2
        targetString = string1
    else:
        startString = string1
        targetString = string2

    mappingsList = findMappings(startString, targetString)
    bestMapping = rankMappings(mappingsList)
    changesList = makeChanges(startString, targetString, bestMapping)

    lDistance = len(changesList)

    return lDistance


def findMappings(startString, targetString):
    # return mappingsList
    pass


def scoreMapping(mapping, startString, targetString):
    """Score mapping based on number of matches and subs.

    >>> scoreMapping({0:0, 1:1, 2:2}, "012", "0123")
    0

    >>> scoreMapping({0:1, 2:2}, "012", "0123")
    2

    >>> scoreMapping({0:1, 1:2}, "012", "012")
    2

    >>> scoreMapping({0:0, 2:2}, "012", "0123")
    1
    """

    score = 0
    missingNos = [i for i in range(len(startString)) if i not in mapping]
    for ind in missingNos:
        lowerInd = max([i for i in mapping if i < ind] + [-1])
        upperInd = min([i for i in mapping if i > ind] + [len(targetString)])
        lowerBound = mapping.get(lowerInd, -1)
        upperBound = mapping.get(upperInd, len(targetString))
        isSub = upperBound - lowerBound > 1

        if isSub:
            score += 1
            mapping.update({ind: lowerBound + 1})
        else:
            score += 2

    return score


def rankMappings(mappingsList):
    # return bestMapping
    pass


def makeChanges(startString, targetString, bestMapping):
    # return changesList
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()

