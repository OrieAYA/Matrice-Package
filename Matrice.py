
def multMat(matA, matB):
    if verFormat(matA, matB) or len(matA[0]) != len(matB): return False
    return [[sum([i for i in [matA[value][ligne] * matB[column][value] for column in range(len(matA[0]))]]) for value in range(len(matA[0]))] for ligne in range(len(matA))]

def mutlScalMat(matA, k):
    if verFormatMatUnit(matA): return False
    return [[matA[ligne][column] * k for column in range(len(matA[0]))] for ligne in range(len(matA))]

def addMat(matA, matB):
    if verFormat(matA, matB) or len(matA[0]) != len(matB[0]) or len(matA) != len(matB): return False
    return [[matA[ligne][column] + matB[ligne][column] for column in range(len(matA[0]))] for ligne in range(len(matA))]

def soustMat(matA, matB):
    if verFormat(matA, matB) or len(matA[0]) != len(matB[0]) or len(matA) != len(matB): return False
    return [[matA[ligne][column] - matB[ligne][column] for column in range(len(matA[0]))] for ligne in range(len(matA))]

def verFormat(matA, matB):
    return False

def verFormatMatUnit(matA):
    return False

matA = [
    [1,1,1],
    [1,1,1],
    [1,1,1],
]

matB = [
    [1,1,1],
    [1,1,1],
    [1,1,1],
]