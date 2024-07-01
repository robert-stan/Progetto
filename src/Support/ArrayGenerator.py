# B = 1.07226722202
# A = 100
# A*B^i gives n
# i = 0 -> n = 100
# i = 99 -> n = 100000
import random

# Genero un array di n elementi, con valore randomico
def ArrGen(n):
    print("Genero array generico per caso medio...")
    arr = [0] * n
    for i in range(n):
        arr[i] = random.randint(1, 1000001)
    print("Fine generazione array generico.")
    return arr

# Genero un array e un valore di k, a seconda del tipo di algoritmo su cui vogliamo eseguirli, per garantire il caso peggiore
def GeneraCasiPeggiori(arr, k, n, name):
    if (name == 'QuickSelect'): # Caso peggiore di QuickSelect, array ordinato in ordine decrescente
        print("Genero caso peggiore per QuickSelect...")
        arr.sort(reverse=True)
        print("Fine generazione array per QuickSelect.")

    elif (name == 'HeapSelect'): # Il caso peggiore per heapselect e' un array alternato di valori minori e maggiori
        print("Genero caso peggiore per HeapSelect...")
        arr = []
        valori_minori = random.sample(range(1, 500001), n // 2)
        valori_maggiori = random.sample(range(500001, 1000001), n // 2)
        if n % 2 != 0:
            valori_minori.append(random.randint(1, 500000))
        
        for i in range(n):
            if i % 2 == 0:
                arr.append(valori_minori.pop())
            else:
                arr.append(valori_maggiori.pop())
        k = n
        print("Fine generazione array per HeapSelect.")

    elif (name == 'Median of Medians'): # Il caso peggiore di Median e' un array di valori ripetuti.
        print("Genero caso peggiore per Median of Medians Select...")
        arr = [i for i in range(n//2) for _ in range(2)]
        k = n // 2
        print("Fine generazione array per Median of medians select.")
    return k, arr
    
# Genero la dimensione secondo A*B^i. Il valore di i va da 0 a 99 in modo incrementale
def SizeGen(A,B,i):
    n = A * pow(B, i)
    return int(n)

