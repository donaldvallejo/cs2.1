def is_sorted(items):
    """Return a boolean indicating whether items are sorted.
    TODO: Time Complexity: O(1)
    TODO: Space Complexity: O(1)"""
    # if (all(items[i] < items[i+1] for i in range(len(items)-1))):
    #     return True
    # return False
    copy = items[:]
    copy.sort()
    return copy == items

def bubble_sort(items):
    """Sort items by swapping items next to each other, this is iterated over until the list is in order.
    TODO: Time Complexity: Best: O(n) Average: O(n^2) Worst: O(n^2) 
    TODO: Space Complexity: O(1)        """
    is_sorted = True
    counter = 0
    while(is_sorted):
        is_sorted = False
        for i in range(len(items) - counter - 1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                is_sorted = True
        counter += 1

def selection_sort(items):
    """Sort by finding minimum number, swapping it with the first unsorted number, iterate until list is sorted. 
    TODO: Time Complexity:  Best: O(n^2) Average: O(n^2) Worst: O(n^2)
    TODO: Space Complexity: O(1)
    """
    items_length = range(0, len(items)-1)
    for i in items_length:
        min_value = i

        for j in range(i+1, len(items)):
            if items[j] < items[min_value]:
                min_value = j
        
        items[min_value], items[i] = items[i], items[min_value]
    return items


def insertion_sort(items):
    """Sort by taking first item, inserting it to front of list,iterate until all items are in order.
    TODO: Time Complexity: Best: O(n) Average:O(n^2) Worst O(n^2)
    TODO: Space Complexity: O(1)"""
    item_length = range(1, len(items))
    for i in item_length:
        unsorted_value = items[i]

        while items[i-1] > unsorted_value and i > 0:
            items[i], items[i-1] = items[i-1], items[i]
            i -= 1
    return items