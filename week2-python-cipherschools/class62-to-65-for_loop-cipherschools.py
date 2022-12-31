# For Loops with range function
for i in range(10):
    print("Hello World")


# For Loops with range function
for i in range(10):
    print(f"Hello World {i}")


#Example 1
n = int(input("Enter the number"))
total = 0
for i in range(0,n+1):
    total += i
    
print("Sum of total numbers in range:",total)


#Example 2
n = input("Enter the number:")
total = 0
for i in n:
    total += int(i)
    
print("Total of digits:",total)


#Example 3
name = input()
temp = ""

for i in range(len(name)):
    if(name[i] not in temp):
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]



#Break and Continue
for i in range(0,11):
    if i == 5:
        break
    else:
        print(i)



for i in range(0,11):
    if i == 5:
        continue
    else:
        print(i)