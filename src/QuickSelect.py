def Partition(arr, l , r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            Swap(arr, i, j)
            i = i + 1
    Swap(arr, i , r)
    return i

def Swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i] 


def QuickSelect(arr, l, r, k): 
        # Se k è minore di 0 o maggiore della lunghezza dell'array, restituisco None
        if(k<0 or k > len(arr) - 1):
            return None
        
        # Se la dimensione dell'intervallo è 1, restituisco l'elemento
        if(l==r):
            return arr[l]
          
        # Partiziona gli elementi e restituisci il pivot
        p_index = Partition(arr, l, r) 
  
        # Se il pivot ha la stesso valore di k, restituisco l'elemento in quella posizione, rispetto all'indice
        if (k == p_index): 
            return arr[p_index]
        
        # Se il pivot è troppo grande, richiamo la funzione e mi sposto verso sinistra nell'array
        elif (k < p_index):
            return QuickSelect(arr, l, p_index - 1, k)
         
        else:
            # Altrimenti in modo analogo, ma verso destra e aggiorno k per il nuovo intervallo
            return QuickSelect(arr, p_index + 1, r, k)  

def scanArray():
    tokens = input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens

def main():
    # Test: L'elemento che andra in quinta posizione è 43 -> [12, 21, 23, 29, 43, 45, 72, 75, 98, 123]
    arr = scanArray()
    k = int(input())
    n = len(arr)

    print(QuickSelect(arr, 0, n-1, k-1))


if __name__ == "__main__":
    main()