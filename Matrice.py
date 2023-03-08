
def multMat(matA, matB):
    if verFormat(matA, matB): return False
    return [[sum([i for i in [matA[value][ligne] * matB[column][value] for column in range(len(matA[0]))]]) for value in range(len(matA[0]))] for ligne in range(len(matA))]

def verFormat(matA, matB):
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

print(multMat(matA, matB))