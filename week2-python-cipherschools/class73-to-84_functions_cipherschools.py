# Functions
def add(a,b):
    return a+b
a = int(input())
b = int(input())
print(add(a,b))



first = input("Name: ")
last = input("Last: ")
print(add(first,last))


#FUNCTIONS PRACTICE
def odd_even(num):
    if(num%2 == 0):
        print("Even")
    else:
        print("Odd")
        
num = int(input())
odd_even(num)



#GREATEST
def greatest(a,b,c):
    if(a > b and a > c):
        return a
    elif(b > c and b > a):
        return b
    else:
        return c
    
a = int(input("Enter num 1: "))
b = int(input("Enter num 2: "))
c = int(input("Enter num 3: "))

print(greatest(a,b,c),":Is the greatest")



# USING ONE FUNCTION IN ANOTHER FUNCTION
def grater(a,b):
    if(a>b):
        return a
    else:
        return b

def greatest2(a,c):
    if a>c:
        print("A great")
    else:
        print("C Great")

a = 10
b = 30
c = 40
greatest = greatest2(grater(a,b),c)



#EXERCISE 2
def is_palindrome(string):
    revstr = string[::-1]
    
    if(string == revstr):
        return True
    return False
    
word = "Horse"
print(is_palindrome(word))



#FIBONACCI SERIES
def fibonacci(num):
    firstnum = 0
    secondnum = 1
    if(num == 1):
        print(firstnum)
    elif(num == 2):
        print(firstnum,secondnum)
    else:
        print(firstnum,secondnum,end=" ")
        for i in range(n-2):
            total = firstnum+secondnum
            firstnum = secondnum
            secondnum = total
            print(total,end=" ")
n = int(input("Number: "))
fibonacci(n)



#DEFAULT PARAMETERS
def userdetail(name,surname,age = 20):
    print(name + surname + " is " + str(age) + " years old")
    
name = input("Name:")
surname = input("Surname:")
age = 15
userdetail(name,surname,age)
userdetail(name,surname)