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

def Swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def QuickSelect(arr, left, right, k):
    if left == right:
        return arr[left]
    
    pivot_index = (left + right) // 2
    pivot_index = Partition(arr, left, right, pivot_index)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return QuickSelect(arr, left, pivot_index - 1, k)
    else:
        return QuickSelect(arr, pivot_index + 1, right, k)

def FindMedian(arr, left, right):
    n = right - left + 1
    mid = left + n // 2
    return QuickSelect(arr, left, right, mid)

def MoMSelect(arr, left, right, k):
    if k < 0 or k >= len(arr):
        return None
    if left == right:
        return arr[left]
    
    i = 0
    mediani = []
    partizioni = (right - left + 1) // 5

    if (right - left + 1) % 5 != 0:
        partizioni += 1
    
    while i < partizioni:
        indice_sx_partizione = left + i * 5
        indice_dx_partizione = min(indice_sx_partizione + 4, right)
        mediani.append(FindMedian(arr, indice_sx_partizione, indice_dx_partizione))
        i += 1

    if len(mediani) == 1:
        mediano_dei_mediani = mediani[0]
    else:
        mediano_dei_mediani = MoMSelect(mediani, 0, len(mediani) - 1, len(mediani) // 2)
    
    indice_pivot = Partition(arr, left, right, arr.index(mediano_dei_mediani))

    if k == indice_pivot:
        return arr[k]
    elif k < indice_pivot:
        return MoMSelect(arr, left, indice_pivot - 1, k)
    else:
        return MoMSelect(arr, indice_pivot + 1, right, k)

def scanArray():
    tokens = input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens

if __name__ == "__main__":

    arr = scanArray()
    k = int(input())

    print(MoMSelect(arr, 0, len(arr) - 1, k-1))
