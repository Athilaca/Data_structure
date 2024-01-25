def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]  
    return arr 


def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    less_than_pivot=[x for x in arr[1:] if x <= pivot]
    greater_than_pivot=[x for x in arr[1:] if x > pivot]
    return quick_sort(less_than_pivot)+[pivot]+quick_sort(greater_than_pivot)
     
def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left_half=arr[:mid]
        right_half=arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i=j=k=0
        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                arr[k]=left_half[i]
                i+=1
            else:
                arr[k]=right_half[j]
                j+=1
            k+=1

        while i<len(left_half) :
            arr[k]=left_half[i]
            i+=1
            k+=1

        while j<len(right_half):
            arr[k]=right_half[j] 
            j+=1
            k+=1               
    return arr

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr  



def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key <arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key    
    return arr
       

array=[2,8,6,5,4,9,1]
print(insertion_sort(array)) 