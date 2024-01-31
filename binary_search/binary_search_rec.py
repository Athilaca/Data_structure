def recursion_using_binary(arr,target,low,high):
    if low>high:
        return -1
    mid=(high+low)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
       return recursion_using_binary(arr,target,low,mid-1)
    else:
       return recursion_using_binary(arr,target,mid+1,high)

arr=[1,2,3,4,5,6,7]
target=-1
print( recursion_using_binary(arr,target,0,len(arr)-1))