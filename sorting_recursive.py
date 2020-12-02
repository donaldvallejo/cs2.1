def merge(items1, items2):
    if items1 and items2:
        if items1[0] > items2[0]:
            items1, items2 = items2, items1
        return [items1[0]] + merge(items1[1:], items2)
    return items1 + items2

def merge_sort(items):
    if len(items) <= 1:
        return items
    middle = len(items) // 2
    left = items[:middle]
    right = items[middle:]
    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            items[k] = left[i]
            i += 1
        else:
            items[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        items[k] = left[i]
        i += 1
        k+= 1
    while j < len(right):
        items[k] = right[j]
        j += 1
        k += 1
    return items
        
print(merge_sort([6,8,7,1]))


def partition(items, low, high):
    i = low - 1
    pivot = items[high]
    for j in range(low, high):
        if items[j] < pivot:
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[high] = items[high], items[i + 1]
    return (i + 1)
            

def quick_sort(items, low=None, high=None):
    length = len(items)
    if length <= 1:
        return items
    else:
        pivot = items.pop()
    low = []
    high = []
    
    for item in items:
        if item > pivot:
            high.append(item)
        else:
            low.append(item)
    return quick_sort(low) + [pivot] + quick_sort(high)

items = [2,3,6,3,7,5,8,9,7,6]    
print(quick_sort(items, 0, 9))