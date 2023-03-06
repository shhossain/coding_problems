from typing import List
import numpy as np
INFINITY = 2**31 + 5

def setZeros(matrix: List[List[int]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0 or matrix[i][j] - INFINITY == 0:

                for k in range(len(matrix[i])):
                    if matrix[i][k] < INFINITY:
                        matrix[i][k] += INFINITY


                for l in range(len(matrix)):
                    if matrix[l][j] < INFINITY:
                        matrix[l][j] += INFINITY
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] >= INFINITY:
                matrix[i][j] = 0

    return matrix
    
            
                
    
            
for _ in range(int(input())):
    n,m = map(int, input().split())
    matrix = []
    for i in range(n):
        a = list(map(int, input().split()))
        matrix.append(a)

    z = setZeros(matrix)
    for i in z:
        for k in i:
            print(k,end=" ")
        print()
    # print()