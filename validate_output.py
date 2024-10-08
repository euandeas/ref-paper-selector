from collections import defaultdict

def GetAuthorsList(mList):
    finalDic = defaultdict(int)
    for x in mList:
        finalDic[x[0]] = 0  
    return finalDic

def Validate(inList, outList, maxPerAuthor, verbose):
    authors = GetAuthorsList(inList)
    numOfPapers = len(outList)

    listOfPapers = []
    duplicatePapers = []
    
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

    for n in outList:
        if n[0] in listOfPapers:
            duplicatePapers.append(n[0])
        else:
            listOfPapers.append(n[0])

    for a in authors:
        if authors[a] > 1:
            authorsWithMultiplePapers.append(a)
    
    numberNoPapers = len(authorsWithNoPapers)
    numberTooManyPapers = len(authorsWithTooManyPapers)
    numberMultiplePapers = len(authorsWithMultiplePapers)

    if verbose == True:
        print()
        print(f"Papers Tested: {numOfPapers}")
        print(f"Valid results?: {meetsReq}")
        print(f"Total errors: {numberNoPapers + numberTooManyPapers + len(duplicatePapers)}")
        print(f"Authors with no papers: {authorsWithNoPapers}")
        print(f"Total number of authors with no papers: {numberNoPapers}")
        print(f"Authors with too many papers: {authorsWithTooManyPapers}")
        print(f"Total number of authors with too many papers: {numberTooManyPapers}")
        print(f"Authors with multiple papers: {authorsWithMultiplePapers}")
        print(f"Total number of authors with multiple papers: {numberMultiplePapers}")
        print(f"Total duplicated papers: {len(duplicatePapers)}")
        print(f"Duplicated papers: {duplicatePapers}")
    else:
        print()
        print(f"Papers Tested: {numOfPapers}")
        print(f"Valid results?: {meetsReq}")
        print(f"Total errors: {numberNoPapers + numberTooManyPapers + len(duplicatePapers)}")
        print(f"Total number of authors with no papers: {numberNoPapers}")
        print(f"Total number of authors with too many papers: {numberTooManyPapers}")
        print(f"Total duplicated papers: {len(duplicatePapers)}")
