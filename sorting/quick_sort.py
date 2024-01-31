def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    less_than_pivot=[x for x in arr[1:] if x <= pivot]
    greater_than_pivot=[x for x in arr[1:] if x > pivot]
    return quick_sort(less_than_pivot)+[pivot]+quick_sort(greater_than_pivot)