'''
Heap select

Questo algoritmo di selezione utilizza due min-heap, denominate H1 e H2. La prima heap H1 é costruita a partire dal vettore fornito in input in tempo lineare e non viene modificata. 
La seconda heap H2 contiene inizialmente un solo nodo, corrispondente alla radice di H1. All'i-esima iterazione, per i che va da 1 a k-1, l'algoritmo estrae la radice di H2, che corrisponde a un nodo x_i
in H1, e reinserisce in H2 i nodi successori (figli sinistro e destro) di x_i nella heap H1. Dopo k-1 iterazioni, la radice di H2 corrisponderà al k-esimo elemento più piccolo del vettore fornito in input.
L'algoritmo descritto ha complessità temporale O(n+klogk) sia nel caso pessimo che in quello medio. 
Per k sufficientemente piccolo, quindi, l'algoritmo "heap select" sarà preferibile, almeno nel caso pessimo, all'algoritmo "quick select". 
È possibile implementare una variante che utilizzi opportunamente min-heap o max-heap, a seconda del valore di k.

'''

# Passaggi:
# New H1 da Arr
# New H2 (H2 ha un solo nodo, cioe' H1.root)
# Per i=1 a i<k
#   extracted_node = MinHeapExtract(H2)
#   node_H1 = MinHeapSearch(node)
#   H2.MinHeapInsert(node_H1.left)
#   H2.MinHeapInsert(node_H1.right)


