# B = 1.07226722202
# A = 100
# A*B^i gives n
# i = 0 -> n = 100
# i = 99 -> n = 100000
import random

'''
Precondizione:
- 100 <= n <= 100000
'''

# Genero un vettore di n elementi, con valore randomico
def ArrGen(n):
    arr = [0] * n
    for i in range(0, n-1):
        arr[i] = random.randint(0, 1000000)
    return arr

# Genero la dimensione secondo A*B^i. Il valore di i va da 0 a 99 in modo incrementale
def SizeGen(A,B,i):
    n = A * pow(B, i)
    return int(n)

