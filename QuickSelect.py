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

def partition(arr, l, r): 
      
    x = arr[r] 
    i = l 
    for j in range(l, r): 
          
        if arr[j] <= x: 
            arr[i], arr[j] = arr[j], arr[i] 
            i += 1
              
    arr[i], arr[r] = arr[r], arr[i] 
    return i 
  
def QuickSelect(arr, l, r, k): 
  
    # Se k è minore del numero di elementi nell' array
    # e maggiore di zero
    if (k > 0 and k <= r - l + 1): 
  
        # Partiziona gli elementi e ritorna il pivot  
        index = partition(arr, l, r) 
  
        # Se il pivot ha la stessa posizione di k, restituisco l'elemento in quella posizione
        if (index - l == k - 1): 
            return arr[index] 

        # Se il pivot è troppo grande, mi sposto verso sinistra nell'array
        if (index - l > k - 1): 
            return QuickSelect(arr, l, index - 1, k) 
  
        # Altrimenti in modo analogo verso destra e aggiorno k per il nuovo intervallo
        return QuickSelect(arr, index + 1, r,  
                            k - index + l - 1)  



# Test case: L'elemento che andra in quinta posizione è 43 -> [12, 21, 23, 29, 43, 45, 72, 75, 98, 123]
arr = [43, 45, 23, 123, 75, 98, 21, 29, 12, 72] 
n = len(arr)
k = 5
print(QuickSelect(arr, 0, n - 1, k))