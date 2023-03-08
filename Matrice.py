
def multMat(matA, matB):
    if verFormat(matA, matB): return False
    matReturn = [[value for value in [column for column in range(len(matA[0]))]] for ligne in range(len(matA))]

    return matReturn

    'matA[value][ligne] * matB[column][value]'

    matRetour = []
    for i in range(len(matA)):
        matPassage = []
        for j in range(len(matA[0])):
            for index in range(len(matA[0])):
                sum += matA[index][i] * matB[j][index]
            matPassage += [sum]
        matRetour += [matPassage]

def verFormat(matA, matB):
    return True

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