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

# Passaggi:
# New H1 da Arr
# New H2 (H2 ha un solo nodo inizialmente, cioe' H1.root)
#   Per i=0 a i<k:
#       MinHeapExtract(H2)
#       IF LEFT in heapsize
#           H2.MinHeapInsert(node_H1.left)
#       IF RIGHT in heapsize
#           H2.MinHeapInsert(node_H1.right)
# Return H2.root

'''
Metodi usati da libreria HEAPQ:
heappush
heappop
heapify
'''

def HeapSelect(A, k):

    if(k==0 or k > len(A)):
        return None
    
    H1 = A
    heapify(H1) # H1 ora e' una min heap

    H2 = []
    heappush(H2, H1[0])

    i = 0
    while(i<k):
        #Estraggo la root da H2
        heappop(H2)
        # Se ha figlio sinistro
        if(2*i < len(H1)):
            # Inseriscilo in H2
            heappush(H2, H1[2*i])
        # Se ha figlio destro
        if(2*i + 1 < len(H1)):
            #Inserisco il figlio destro in H2
            heappush(H2, H1[2*i+1])
        i = i + 1

    return H2[0] # Restituisco la root di H2, che ora e' il k-esimo elemento piu' piccolo di A | A non viene or


#  __    __     ______     __     __   __    
# /\ "-./  \   /\  __ \   /\ \   /\ "-.\ \   
# \ \ \-./\ \  \ \  __ \  \ \ \  \ \ \-.  \  
#  \ \_\ \ \_\  \ \_\ \_\  \ \_\  \ \_\\"\_\ 
#   \/_/  \/_/   \/_/\/_/   \/_/   \/_/ \/_/ 


if __name__ == "__main__":

    A = [55, 33, 11, 22, 44, 77, 99, 66, 88, 100]
    k=5

    print("\n")

    print("Elementi del vettore A:")
    print(A)

    print("\n")

    print("K-esimo elemento piu' piccolo di A: " + str(HeapSelect(A, k)) + ", con k = " + str(k) + ".")

    print("\n")

    # HeapSelect e' implementata per restituire le posizioni dei k-esimi elementi considerando che in posizione 1 di un vettore c'e' il primo elemento, in due il secondo, ecc... (gli indici partono da 1 e non da 0)
