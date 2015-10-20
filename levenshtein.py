## figuring out the Levenshtein distance between two strings
## you're allowed to insert, delete, and swap, and each costs 1


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
    return mappingsList

def scoreMapping(mapping, targetString):
    maxLen = len(targetString)
    return score

def rankMappings(mappingsList):
    return bestMapping

def makeChanges(startString, targetString, bestMapping):
    return changesList


if __name__ = '__main__':
    import doctest
    doctest.testmod()


