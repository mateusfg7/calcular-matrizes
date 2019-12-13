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


for numI in range(1, parametroLinhasI+1):
    for numJ in range(1, parametroColunasJ+1):
        print("{}x{}: {}".format(numI, numJ, calcular(numI, numJ)))