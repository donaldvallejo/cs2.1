def selection_sort():
    arr = [23, 4, 1, 2, 5, 10, 12]
    for i in range(len(arr) - 1):
        smallest = i 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j 
        arr[j] = arr[smallest]
        return arr
        
selection_sort()
