from collections import defaultdict

def GetAuthorsList(mList):
    finalDic = defaultdict(int)
    for x in mList:
        finalDic[x[0]] = 0  
    return finalDic

def Validate(inList, outList, maxPerAuthor, verbose):
    authors = GetAuthorsList(inList)
    numOfPapers = len(outList)
    
    meetsReq = True
    authorsWithNoPapers = []
    authorsWithTooManyPapers = []
    authorsWithMultiplePapers = []
    
    for x in outList:
        authors[x[1]] += 1

    for y in authors:
        if authors[y] == 0:
            meetsReq = False
            authorsWithNoPapers.append(y)
        if authors[y] > maxPerAuthor:
            meetsReq = False
            authorsWithTooManyPapers.append(y)

    for a in authors:
        if authors[a] > 1:
            authorsWithMultiplePapers.append(a)
    
    numberOfAuthorsWithNoPapers = len(authorsWithNoPapers)
    numberOfAuthorsWithTooManyPapers = len(authorsWithTooManyPapers)
    numberOfAuthorsWithMultiplePapers = len(authorsWithMultiplePapers)

    if verbose == True:
        print()
        print(f"Papers Tested: {numOfPapers}")
        print(f"Valid results?: {meetsReq}")
        print(f"Total errors: {numberOfAuthorsWithNoPapers + numberOfAuthorsWithTooManyPapers}")
        print(f"Authors with no papers: {authorsWithNoPapers}")
        print(f"Total number of authors with no papers: {numberOfAuthorsWithNoPapers}")
        print(f"Authors with too many papers: {authorsWithTooManyPapers}")
        print(f"Total number of authors with too many papers: {numberOfAuthorsWithTooManyPapers}")
        print(f"Authors with multiple papers: {authorsWithMultiplePapers}")
        print(f"Total number of authors with multiple papers: {numberOfAuthorsWithMultiplePapers}")
    else:
        print()
        print(f"Papers Tested: {numOfPapers}")
        print(f"Valid results?: {meetsReq}")
        print(f"Total errors: {numberOfAuthorsWithNoPapers + numberOfAuthorsWithTooManyPapers}")
        print(f"Total number of authors with no papers: {numberOfAuthorsWithNoPapers}")
        print(f"Total number of authors with too many papers: {numberOfAuthorsWithTooManyPapers}")