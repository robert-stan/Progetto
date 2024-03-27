Il progetto richiede l'implementazione di tre algoritmi di selezione, che calcolano il k-esimo elemento più piccolo in un vettore non ordinato di interi. 
Insieme all'implementazione, è richiesta una stima e un'analisi dei tempi medi di esecuzione degli algoritmi in funzione della dimensione dell'input. 
I tre algoritmi di selezione, denominati rispettivamente "quick select", "heap select" e "median-of-medians select", dovranno avere le seguenti caratteristiche:

Quick select

Si tratta di una variante dell'algoritmo di ordinamento "quick sort", in cui ogni chiamata ricorsiva su un intervallo [i,j]
del vettore fornito in input termina restituendo il k-esimo elemento più piccolo del vettore qualora k−1∈[i,j], oppure un valore indefinito qualora k∉[i,j]. 
In particolare, nel secondo caso, una chiamata sull'intervallo [i,j] con k∉[i,j] può terminare in tempo costante senza dover eseguire la procedura partition. 
L'algoritmo dovrà avere quindi complessità temporale asintotica Θ(n^2) nel caso pessimo e O(n) nel caso medio, dove n è il numero di elementi del vettore.

Heap select

Questo algoritmo di selezione utilizza due min-heap, denominate H1 e H2. La prima heap H1 é costruita a partire dal vettore fornito in input in tempo lineare e non viene modificata. 
La seconda heap H2 contiene inizialmente un solo nodo, corrispondente alla radice di H1. All'i-esima iterazione, per i che va da 1 a k−1, l'algoritmo estrae la radice di H2, che corrisponde a un nodo x_i
in H1, e reinserisce in H2 i nodi successori (figli sinistro e destro) di x_i nella heap H1. Dopo k−1 iterazioni, la radice di H2 corrisponderà al k-esimo elemento più piccolo del vettore fornito in input.
L'algoritmo descritto ha complessità temporale O(n+klogk) sia nel caso pessimo che in quello medio. 
Per k sufficientemente piccolo, quindi, l'algoritmo "heap select" sarà preferibile, almeno nel caso pessimo, all'algoritmo "quick select". 
È possibile implementare una variante che utilizzi opportunamente min-heap o max-heap, a seconda del valore di k.

Median-of-medians select

L'algoritmo è basato sulla suddivisione del vettore fornito in input in blocchi di dimensione limitata e sul calcolo della mediana delle mediane. Più precisamente, l'algoritmo esegue le seguenti operazioni:
- divisione dell'array in blocchi di 5 elementi, escluso eventualmente l'ultimo blocco che potrà contenere meno di 5 elementi,
- ordinamento e calcolo della mediana di ciascun blocco,
- calcolo della mediana M delle mediane dei blocchi, attraverso chiamata ricorsiva allo stesso algoritmo
- partizionamento dell'intero array attorno alla mediana M, attraverso una variante della procedura "partition" dell'algoritmo "quick sort"
- chiamata ricorsiva nella parte di array che sta a sinistra o a destra della mediana M, in funzione del valore k fornito in input.
Il modo più semplice per implementare quest'algoritmo consiste nell'allocare, ad ogni chiamata ricorsiva, un nuovo vettore per memorizzare le mediane dei blocchi.
Esiste tuttavia un approccio più efficiente e "quasi in place" che riutilizza lo spazio allocato per il vettore originariamente fornito in input (l'unico spazio aggiuntivo utilizzato è dato dalla pila dedicata alla gestione delle chiamate ricorsive).
Indipendentemente dalla variante implementata, nel caso pessimo l'algoritmo dovrà avere complessità, sia temporale che spaziale, pari a O(n).
