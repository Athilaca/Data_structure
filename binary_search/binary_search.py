def binary_search(arr,target):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1 
    return -1
arr=[1,3,4,6,7,9]
print(binary_search(arr,8))



