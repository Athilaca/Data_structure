#find element in the list
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [1, 3, 5, 7, 9, 11, 13]
target_value = 7
result = linear_search(numbers, target_value)
print(f"Index of {target_value} using Linear Search: {result}")


#count occurences of the element
def count_occurences(arr,target):
    count=0
    for i in range(len(arr)):
        if arr[i]==target:
            count+=1
    return count

numbers=[1,2,3,5,2,6,2,7]   
target=2
result= count_occurences(numbers,target) 
print(f"the count of {target} in arr is:{result}")

#check if element exists
def element_exists(arr, target):
    for num in arr:
        if num == target:
            return True
    return False

numbers = [10, 20, 30, 40, 50]
target_value = 35
exists = element_exists(numbers, target_value)
print(f"the element that exists in the array is {exists}")

#find minimum element in array
def minimum_value(arr):
    min=arr[0]
    for num in range (len(arr)):
        if arr[num]<min:
          min=arr[num]

    return min      

numbers = [5, 3, 8, 2, 1, 7, 4]
print(f'the min num in array is :{minimum_value(numbers)}')
