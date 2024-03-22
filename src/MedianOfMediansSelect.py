'''
Median-of-medians select

L'algoritmo è basato sulla suddivisione del vettore fornito in input in blocchi di dimensione limitata e sul calcolo della mediana delle mediane.
Più precisamente, l'algoritmo esegue le seguenti operazioni:
- divisione dell'array in blocchi di 5 elementi, escluso eventualmente l'ultimo blocco che potrà contenere meno di 5 elementi,
- ordinamento e calcolo della mediana di ciascun blocco,
- calcolo della mediana M delle mediane dei blocchi, attraverso chiamata ricorsiva allo stesso algoritmo
- partizionamento dell'intero array attorno alla mediana M, attraverso una variante della procedura "partition" dell'algoritmo "quick sort"
- chiamata ricorsiva nella parte di array che sta a sinistra o a destra della mediana M, in funzione del valore k fornito in input.
Il modo più semplice per implementare quest'algoritmo consiste nell'allocare, ad ogni chiamata ricorsiva, un nuovo vettore per memorizzare le mediane dei blocchi.
Esiste tuttavia un approccio più efficiente e "quasi in place",
che riutilizza lo spazio allocato per il vettore,
originariamente fornito in input (l'unico spazio aggiuntivo utilizzato è dato dalla pila dedicata alla gestione delle chiamate ricorsive).

Indipendentemente dalla variante implementata, nel caso pessimo l'algoritmo dovrà avere complessità, sia temporale che spaziale, pari a O(n).
'''

'''
PARTITION
La complessita' di Partition e' Theta(n), dove n = r - l + 1

SCOPO: Spostare gli elementi dell'intervallo, per fare in modo che quelli minori del pivot stiano alla sua sinistra e quelli maggiori a destra (Non ordina tutti gli elementi, ma partiziona)

PARAMETRI:
- arr: Lista di numeri (vettore)
- l: Intero (Intervallo sinistro)
- r: Intero (Intervallo destro)
- pivot: Intero (Perno iniziale)

RETURNS:
- Index: Intero (Indice del perno)
'''
def Partition(arr, l, r, pivot): 
    x = arr[pivot]
    Swap(arr, pivot, r) 
    index = l 
    for j in range(l, r):   
        if arr[j] <= x: 
            Swap(arr, index, j)
            index += 1       
    Swap(arr, index, r) 
    return index



'''
SWAP
La complessita' temporale di Swap e' costante, pari a O(1)

SCOPO: Scambiare due elementi di un vettore

PARAMETRI:
- arr: Lista di numeri (vettore)
- i: Intero (Indice del primo elemento)
- j: Intero (Indice del secondo elemento)

'''
def Swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i] 

'''
Median of Medians Select
---
. MISSION
. PARAMS
. 
.
.
---
'''

def MoMSelect(arr, left, right, k):
    if(k < 0 or k >= len(arr)):
        return None
    if(left == right):
        return arr[left]
    
    i=0
    
    mediani = []
    
    partizioni = (right - left + 1) // 5

    if((right - left + 1) % 5 != 0):
        partizioni = partizioni + 1
    
    while(i < partizioni):
        indice_sx_partizione = left + i * 5
        if(indice_sx_partizione + 4 < right):
            indice_dx_partizione = indice_sx_partizione + 4
        else:
            indice_dx_partizione = right
        indice_mediano = Partition(arr, indice_sx_partizione, indice_dx_partizione, (indice_sx_partizione + indice_dx_partizione) // 2)
        mediani.append(arr[indice_mediano])
        i = i + 1

    mediano_dei_mediani = MoMSelect(mediani, 0, len(mediani) - 1, len(mediani) // 2)
    indice_pivot = Partition(arr, left, right, arr.index(mediano_dei_mediani))

    if(k == indice_pivot):
        return arr[k]
    elif(k < indice_pivot):
        return MoMSelect(arr, left, indice_pivot - 1, k)
    else:
        return MoMSelect(arr, indice_pivot + 1, right, k)
    
if __name__ == "__main__":

    A = [55, 33, 11, 22, 44, 77, 99, 66, 88, 100]
    k=5

    print("\n")

    print("Elementi del vettore A:")
    print(A)

    print("\n")

    print("K-esimo elemento piu' piccolo di A: " + str(MoMSelect(A, 0, len(A) - 1, k)) + ", con k = " + str(k) + ".")

    print("\n")