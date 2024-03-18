'''
Quick select

Si tratta di una variante dell'algoritmo di ordinamento "quick sort", 
in cui ogni chiamata ricorsiva su un intervallo [i,j] del vettore fornito in input termina restituendo 
il k-esimo elemento più piccolo del vettore qualora k-1 ∈ [i,j], oppure un valore indefinito qualora k ∉ [i,j]. 
In particolare, nel secondo caso, una chiamata sull'intervallo [i,j] con k ∉ [i,j] 
può terminare in tempo costante senza dover eseguire la procedura partition. 
L'algoritmo dovrà avere quindi complessità temporale asintotica Θ(n^2) nel caso pessimo 
e O(n) nel caso medio, dove n è il numero di elementi del vettore.

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
QUICKSELECT
La complessita' di QuickSelect e' O(n) nel caso medio, con n la dimensione dell'array;
Nel caso medio il Pivot bilancia bene l'array.
La complessita' nel caso pessimo, ovvero quando l'array e' gia ordinato e' O(n^2)

SCOPO: Restituire il k-esimo elemento piu' piccolo del vettore

PARAMETRI:
- arr: Lista di numeri (vettore)
- l: Intero (Intervallo sinistro)
- r: Intero (Intervallo destro)
- k: Intero (Indice dell'elemento piu' piccolo da restituire)

RETURNS:
- Intero (Elemento piu' piccolo in posizione k del vettore)
'''
def QuickSelect(arr, l, r, k): 
        # Se k è minore di 0 o maggiore della lunghezza dell'array, restituisco None
        if(k<0 or k > len(arr)-1):
            return None
        
        # Se la dimensione dell'intervallo è 1, restituisco l'elemento
        if(l==r):
            return arr[l]
          
        # Partiziona gli elementi e restituisci il pivot
        p_index = Partition(arr, l, r, len(arr)//2) 
  
        # Se il pivot ha la stesso valore di k, restituisco l'elemento in quella posizione, rispetto all'indice
        if (k == p_index): 
            return arr[p_index]
        
        # Se il pivot è troppo grande, richiamo la funzione e mi sposto verso sinistra nell'array
        elif (k < p_index):
            return QuickSelect(arr, l, p_index - 1, k)
         
        else:
            # Altrimenti in modo analogo, ma verso destra e aggiorno k per il nuovo intervallo
            return QuickSelect(arr, p_index + 1, r, k)  



#  __    __     ______     __     __   __    
# /\ "-./  \   /\  __ \   /\ \   /\ "-.\ \   
# \ \ \-./\ \  \ \  __ \  \ \ \  \ \ \-.  \  
#  \ \_\ \ \_\  \ \_\ \_\  \ \_\  \ \_\\"\_\ 
#   \/_/  \/_/   \/_/\/_/   \/_/   \/_/ \/_/ 
 

 
def main():
    # Test: L'elemento che andra in quinta posizione è 43 -> [12, 21, 23, 29, 43, 45, 72, 75, 98, 123]
    arr = [43, 45, 23, 123, 75, 98, 21, 29, 12, 72] 
    k = 5
    n = len(arr)

    print(QuickSelect(arr, 0, n - 1, k-1))


if __name__ == "__main__":
    main()
