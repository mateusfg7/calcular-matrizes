import sys 
import math as mt

i = int(sys.argv[1])
j = int(sys.argv[2])

#print("1º: {}\n2º: {}".format(type(i), type(j)))


for numI in range(1, i+1):
    for numJ in range(1, j+1):
        print("{}x{}".format(numI, numJ))