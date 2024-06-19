# QuickSelect

# Si tratta di una variante dell'algoritmo di ordinamento "quick sort", in cui ogni chiamata ricorsiva su un intervallo [i,j] del vettore fornito in input termina restituendo il k-esimo elemento più piccolo del vettore qualora k−1∈[i,j],
# oppure un valore indefinito qualora k∉[i,j]. In particolare, nel secondo caso, una chiamata sull'intervallo [i,j] con k∉[i,j] può terminare in tempo costante senza dover eseguire la procedura partition.
# L'algoritmo dovrà avere quindi complessità temporale asintotica Θ(n2) nel caso pessimo e O(n) nel caso medio, dove n è il numero di elementi del vettore.

def QuickSelect(arr, k):
    n = len(arr)
    return QuickSelect_alg(arr, 0, n-1, k-1)

def QuickSelect_alg(arr, l, r, k): 
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
            return QuickSelect_alg(arr, l, p_index - 1, k)
         
        else:
            return QuickSelect_alg(arr, p_index + 1, r, k)
        
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




def scanArray(): # Funzione per l'inserimento di array da riga di comando
    tokens = input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens


# Main

def main():
    arr = scanArray()
    k = int(input())
    n = len(arr)
    print(QuickSelect(arr, 0, n-1, k-1))





if __name__ == "__main__":
    main()