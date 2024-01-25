#check if the given string is palidrome  

def palidrome(string):
    cleaned_str=''.join(char.strip(",") for char in string)
    print(cleaned_str)
    if cleaned_str==cleaned_str[::-1]:
        return True
    return False
print(f'is the string a palidrome ? {palidrome("A man, a plan, a canal, Panama!")}')
#joining
words = ['This', 'is', 'a', 'sample', 'sentence.']
joined_sentence = ' '.join(words)
print(joined_sentence)



# function to replace each alphabet in the given string with another alphabet occurring at the n-th position from each of them.

def replace_alphabets(input_str, n):
    result = ""
    for char in input_str:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr(((ord(char) - base) + n) % 26 + base)
         
           
        else:
            result += char
    return result

original_text = "Hello, World!"
n_value = 3
modified_text = replace_alphabets(original_text, n_value)
print(f"Original Text: {original_text}")
print(f"Modified Text (n={n_value}): {modified_text}")



def count_vowels(str):
    vowels="aeiou"
    count=0
    for i in str:
        if i in vowels:
            count+=1
    return count

print(f'vowels ={count_vowels("happybirthday")}')

#check if two strings are anagrams

def are_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    return sorted(str1)==sorted(str2)

print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False

# to reverse words in a given sentence

def reverse_words(sentence):
    words = sentence.split()  
    reversed_sentence = ' '.join(reversed(words)) 
    return reversed_sentence

# Test the function
print(reverse_words("Hello World")) 
print(reverse_words("Python is fun"))  



arr=[1,0,2,3,0,4,5,0]
n=len(arr)
i=0
while i<n:
    if arr[i]==0:
        arr.insert(i,0)
        arr.pop()
        i+=1
    i+=1    
print(arr)        


str="hello"
sum=0
for i in str:
    sum+=ord(i)
print(sum)    

a="HeLlO"
count=0
for i in a:
    if i.isupper():
        count+=1
print(count)        


array=[[1,2],[3,4],[6,5]]
array_1=[]
for row in array:
    for element in row:
        array_1.append(element)
print(array_1)       



