# figuring out the Levenshtein distance between two strings
# you're allowed to insert, delete, and swap, and each costs 1

import itertools


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
    bestMappingInfo = rankMappings(mappingsList)
    changesList = makeChanges(startString, targetString, bestMappingInfo)

    lDistance = len(changesList)

    return lDistance


def findMappings(startString, targetString):
    # return mappingsList
    pass

def scoreMapping(mapping, startString, targetString):
    """Score mapping based on number of matches and subs.

    >>> scoreMapping({0:0, 1:1, 2:2}, "012", "0123")
    {'score': 0, 'mappingDict': {0: 0, 1: 1, 2: 2}, 'newMappingDict': {0: 0, 1: 1, 2: 2}}

    >>> scoreMapping({0:1, 2:2}, "012", "0123")
    {'score': 2, 'mappingDict': {0: 1, 2: 2}, 'newMappingDict': {0: 1, 2: 2}}

    >>> scoreMapping({0:1, 1:2}, "012", "012")
    {'score': 2, 'mappingDict': {0: 1, 1: 2}, 'newMappingDict': {0: 1, 1: 2}}

    >>> scoreMapping({0:0, 2:2}, "012", "0123")
    {'score': 1, 'mappingDict': {0: 0, 2: 2}, 'newMappingDict': {0: 0, 1: 1, 2: 2}}

    >>> scoreMapping({1:1}, "012", "0123")
    {'score': 2, 'mappingDict': {1: 1}, 'newMappingDict': {0: 0, 1: 1, 2: 2}}

    """
    newMappingDict = mapping.copy()

    score = 0
    missingNos = [i for i in range(len(startString)) if i not in newMappingDict]
    for ind in missingNos:
        lowerInd = max([i for i in newMappingDict if i < ind] + [-1])
        upperInd = min([i for i in newMappingDict if i > ind] + [len(targetString)])
        lowerBound = newMappingDict.get(lowerInd, -1)
        upperBound = newMappingDict.get(upperInd, len(targetString))
        isSub = upperBound - lowerBound > 1

        if isSub:
            score += 1
            newMappingDict.update({ind: lowerBound + 1})
        else:
            score += 2

    return {"score": score, "mappingDict": mapping, "newMappingDict": newMappingDict}


def rankMappings(mappingsList, startString, targetString):
    """pick the mapping with the lowest score (best match)

    >>> rankMappings([{0: 0, 1: 1, 2: 2}], "012", "0123")["mappingDict"]
    {0: 0, 1: 1, 2: 2}

    >>> rankMappings([{0:1, 2:2}, {0:0, 1:1, 2:2}], "012", "0123")["mappingDict"]
    {0: 0, 1: 1, 2: 2}

    >>> rankMappings([{0: 0, 2: 2}, {0: 1, 2: 2}, ], "012", "0123")["mappingDict"]
    {0: 0, 2: 2}

    """

    scoredMappings = [scoreMapping(mapping, startString, targetString)
                        for mapping in mappingsList]

    bestMapping = min(scoredMappings, key=lambda scoredMap: scoredMap["score"])

    return bestMapping


def makeChanges(startString, targetString, bestMapping):
    # return changesList
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()

