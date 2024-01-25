      #......................................... recursion.......................................................

def recursive_function(n):
    if n <= 1:
        return
    
    recursive_function(n - 1)
    print(n)
    recursive_function(n - 1)


# recursive_function(5)
    
#factorial of a number using recursion
    
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
        
result = factorial(5)
print(f"Factorial of 5 is: {result}")

#sum of digits using recursion

def sum_of_digit(n):
    if n<10:
        return n
    else:
        return n%10 + sum_of_digit(n//10)


print(f"sum of digit is: {sum_of_digit(12345)}")

#print fibinocci series using recursion

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) +fibonacci(n-2)
   
         
for i in range(10):
    print(fibonacci(i), end=" ")


