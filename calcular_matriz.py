import sys

try:
    parametroLinhasI = int(sys.argv[1])
    parametroColunasJ = int(sys.argv[2])
except ValueError:
    print("Parâmetros ausentes ou não são valores válidos inteiros!")
    print("use: main.py [i] [j]\n i  Número de linhas\n j  Número de colunas")
    exit()


def calcular(i, j):
    
    ## EQUAÇÃO ##
    return (i + j)

matriz = []

for n in range(0, parametroLinhasI):
    matriz.append([])

for numJ in range(1, parametroColunasJ+1):
    valorI = 1
    valorJ = numJ
    for numI in range(0, parametroLinhasI):
        valorTotal = calcular(valorI, valorJ)
        valorI += 1
        matriz[numI].append(valorTotal)


for n in range(0, parametroLinhasI):
    print(matriz[n]) 
