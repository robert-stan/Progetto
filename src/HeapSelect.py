'''
Heap select

Questo algoritmo di selezione utilizza due min-heap, denominate H1 e H2. La prima heap H1 é costruita a partire dal vettore fornito in input in tempo lineare e non viene modificata. 
La seconda heap H2 contiene inizialmente un solo nodo, corrispondente alla radice di H1.

All'i-esima iterazione, per i che va da 1 a k-1, 

l'algoritmo estrae la radice di H2, che corrisponde a un nodo x_i in H1, 

e reinserisce in H2 i nodi successori (figli sinistro e destro) di x_i nella heap H1. 

Dopo k-1 iterazioni, la radice di H2 corrisponderà al k-esimo elemento più piccolo del vettore fornito in input.
L'algoritmo descritto ha complessità temporale O(n+klogk) sia nel caso pessimo che in quello medio. 
Per k sufficientemente piccolo, quindi, l'algoritmo "heap select" sarà preferibile, almeno nel caso pessimo, all'algoritmo "quick select". 
È possibile implementare una variante che utilizzi opportunamente min-heap o max-heap, a seconda del valore di k.

'''
from heapq import heappush, heappop, heapify


def HeapSelect(A, k):

    if(k==0 or k > len(A)):
        return None
    
    H1 = A
    heapify(H1) # H1 ora e' una min heap

    H2 = []
    heappush(H2, (H1[0], 0))

    i = 0
    while(i<k):
        # Estraggo la root di H2
        element, indice = heappop(H2)

        # Figlio sinistro 
        indice_figlio_sx = 2 * indice + 1

        # Inserisco il figlio sinistro se c'e'
        if(indice_figlio_sx < len(H1)):
            heappush(H2, (H1[indice_figlio_sx], indice_figlio_sx))

        # Figlio destro
        indice_figlio_dx = 2 * indice + 2

        # Inserisco il figlio destro se c'e'
        if(indice_figlio_dx < len(H1)):
            heappush(H2, (H1[indice_figlio_dx], indice_figlio_dx))

        i = i + 1
    
    return element # Restituisco il k-esimo elemento piu' piccolo di A

def scanArray():
    tokens = input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens

if __name__ == "__main__":

    arr = scanArray()
    k = int(input())

    print(HeapSelect(arr, k))


