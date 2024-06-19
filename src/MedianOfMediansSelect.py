# Median Of Medians Select

# L'algoritmo è basato sulla suddivisione del vettore fornito in input in blocchi di dimensione limitata e sul calcolo della mediana delle mediane. Più precisamente, l'algoritmo esegue le seguenti operazioni:
# - divisione dell'array in blocchi di 5 elementi, escluso eventualmente l'ultimo blocco che potrà contenere meno di 5 elementi,
# - ordinamento e calcolo della mediana di ciascun blocco,
# - calcolo della mediana M delle mediane dei blocchi, attraverso chiamata ricorsiva allo stesso algoritmo
# - partizionamento dell'intero array attorno alla mediana M, attraverso una variante della procedura "partition" dell'algoritmo "quick sort"
# - chiamata ricorsiva nella parte di array che sta a sinistra o a destra della mediana M, in funzione del valore k fornito in input.
# Il modo più semplice per implementare quest'algoritmo consiste nell'allocare, ad ogni chiamata ricorsiva, un nuovo vettore per memorizzare le mediane dei blocchi. 
# Esiste tuttavia un approccio più efficiente e "quasi in place" che riutilizza lo spazio allocato per il vettore originariamente fornito in input (l'unico spazio aggiuntivo utilizzato è dato dalla pila dedicata alla gestione delle chiamate ricorsive). 
# La valutazione del progetto terrà conto della variante implementata (quella "quasi in place", essendo più complicata ma anche più efficiente, sarà valutata con un punteggio più alto).
# Indipendentemente dalla variante implementata, nel caso pessimo l'algoritmo dovrà avere complessità, sia temporale che spaziale, pari a O(n).

def MedianOfMediansSelect(arr, k):
    return MoMSelect_alg(arr, 0, len(arr) - 1, k-1)

def MoMSelect_alg(arr, l, r, k):
    # Verifichiamo che k sia un parametro corretto, nel caso non lo fosse, restituiamo None
    if k < 0 or k >= len(arr):
        return None
    
    # Se l'intervallo ha un solo elemento, lo restituisco | (caso base)
    if l == r:
        return arr[l]
    
    # Inizializziamo l'indice i, la lista per i mediani e il numero di partizioni da 5 elementi con cui vogliamo dividere l'array
    i = 0
    mediani = []
    partizioni = (r - l + 1) // 5

    # Se il numero di elementi dell'array non e' un multiplo di 5, allora aggiungo l'ultima partizione, che conterra' meno di 5 elementi
    if (r - l + 1) % 5 != 0:
        partizioni += 1
    # Per ogni partizione, trovo il mediano e lo salvo nella lista apposita
    while i < partizioni:
        indice_sx_partizione = l + i * 5
        indice_dx_partizione = min(indice_sx_partizione + 4, r)
        mediani.append(mediano(arr, indice_sx_partizione, indice_dx_partizione))
        i += 1

    # Se mediani ha un solo elemento, ho finalmente trovato il mediano dei mediani
    if len(mediani) == 1:
        mediano_dei_mediani = mediani[0]
    else:
        mediano_dei_mediani = MoMSelect_alg(mediani, 0, len(mediani) - 1, len(mediani) // 2) # Altrimenti richiamo ricorsivamente median on medians select sulla lista dei mediani e continuo a cercare
    
    # Una volta trovato, partiziono l'array sul mediano dei mediani
    indice_pivot = partition_MoM(arr, l, r, arr.index(mediano_dei_mediani))

    # Come con QuickSelect, richiamo ricorsivamente la funzione fin quando il pivot corrisponde al k-esimo elemento piu piccolo dell'array
    if k == indice_pivot:
        return arr[k]
    elif k < indice_pivot:
        return MoMSelect_alg(arr, l, indice_pivot - 1, k)
    else:
        return MoMSelect_alg(arr, indice_pivot + 1, r, k)



def partition_MoM(arr, l, r, pivot):
    # Mi salvo l'elemento dell'array puntato dal pivot
    x = arr[pivot]
    # Swappo l'elemento con quello posto in fondo all'array
    swap(arr, pivot, r)
    index = l
    for j in range(l, r): # Swappo gli elementi uguali o minori del pivot alla sua sinistra
        if arr[j] <= x:
            swap(arr, index, j)
            index += 1
    swap(arr, index, r)
    return index

def QuickSelect(arr, l, r, k): 
        # Verifichiamo che k sia un parametro corretto, nel caso non lo fosse, restituiamo None
        if(k<0 or k > len(arr) - 1):
            return None
        # Se l'intervallo ha un solo elemento, lo restituisco | (caso base)
        if(l==r):
            return arr[l]
        # Partiziono gli elementi dell'array intorno all'ultimo elemento e mi salvo l'indice del pivot
        p_index = partition_QS(arr, l, r)

        # Richiamo ricorsivamente QuickSelect finche' il pivot corrispondera' al k-esimo elemento piu piccolo dell'array
        if (k == p_index): 
            return arr[p_index]
        
        elif (k < p_index):
            return QuickSelect(arr, l, p_index - 1, k)
         
        else:
            return QuickSelect(arr, p_index + 1, r, k)



def partition_QS(arr, l , r): # Partiziona l'array che passiamo in input attorno all'ultimo elemento, preso come pivot
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            swap(arr, i, j)
            i = i + 1
    swap(arr, i , r)
    return i


def swap(arr, i, j): # Swappa gli elementi in posizione i e j tra di loro
    arr[i], arr[j] = arr[j], arr[i]



def mediano(arr, l, r): # Uso QuickSelect per trovare il mediano della partizione (sotto-intervallo) di array passata in input
    n = r - l + 1
    mid = l + n // 2
    return QuickSelect(arr, l, r, mid)




def scanArray(): # Funzione per l'inserimento di array da riga di comando
    tokens = input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens



# Main

def main():
    arr = scanArray()
    k = int(input())
    print(MedianOfMediansSelect(arr, k))



if __name__ == "__main__":
    main()
