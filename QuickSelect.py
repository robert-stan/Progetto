'''
Quick select

Si tratta di una variante dell'algoritmo di ordinamento "quick sort", 
in cui ogni chiamata ricorsiva su un intervallo [i,j] del vettore fornito in input termina restituendo 
il k-esimo elemento più piccolo del vettore qualora k−1 ∈ [i,j], oppure un valore indefinito qualora k ∉ [i,j]. 
In particolare, nel secondo caso, una chiamata sull'intervallo [i,j] con k ∉ [i,j] 
può terminare in tempo costante senza dover eseguire la procedura partition. 
L'algoritmo dovrà avere quindi complessità temporale asintotica Θ(n^2) nel caso pessimo 
e O(n) nel caso medio, dove n è il numero di elementi del vettore.

'''

def partition(arr, l, r, pivot): 
      
    x = arr[pivot]
    Swap(arr, pivot, r) 
    index = l 
    for j in range(l, r): 
          
        if arr[j] <= x: 
            Swap(arr, index, j)
            index += 1
              
    Swap(arr, index, r) 
    return index

def Swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i] 
  
def QuickSelect(arr, l, r, k): 
        if(k<0 or k > len(arr)-1):
            return None
        if(l==r):
            return arr[l]   
        # Partiziona gli elementi e restituisci il pivot
        p_index = partition(arr, l, r, len(arr)//2) 
  
        # Se il pivot ha la stesso valore di k, restituisco l'elemento in quella posizione, rispetto all'indice
        if (k == p_index): 
            return arr[p_index] 
        # Se il pivot è troppo grande, richiamo la funzione e mi sposto verso sinistra nell'array
        elif (k < p_index):
            return QuickSelect(arr, l, p_index - 1, k) 
        else:
            # Altrimenti in modo analogo, ma verso destra e aggiorno k per il nuovo intervallo
            return QuickSelect(arr, p_index + 1, r, k)  



# Test: L'elemento che andra in quinta posizione è 43 -> [12, 21, 23, 29, 43, 45, 72, 75, 98, 123]
arr = [43, 45, 23, 123, 75, 98, 21, 29, 12, 72] 
k = 10
n = len(arr)

print(QuickSelect(arr, 0, n - 1, k-1))