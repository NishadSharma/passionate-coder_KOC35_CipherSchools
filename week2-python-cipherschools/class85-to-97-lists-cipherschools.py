list1 = [1,2,3,4,5]
list2 = ["Nishad","James","Machine"]
list3 = [1,2,3,"Mr.","Dang",2.3]
print(list3)



print(list1[2])
print(list2[:2])



# ADDING ITEM TO THE LIST
fruits = ["Apple","grapes"]
fruits.append("Mango")
print(fruits)



fruits = ["Jackfruit","Mango"]
fruits.insert(1,"Orange")
print(fruits)



fruits2 = ["Aam","Watermelon"]
fruits.extend(fruits2)
print(fruits)
fruits.append(fruits2)
print(fruits)



# REMOVE ELEMENTS FROM THE LIST
fruits.pop(5)
fruits.remove("Orange")
print(fruits)



if "Aam" in fruits:
    print("present")



print(fruits.count("Aam"))



numlist = [9,7,6,2,3,4,1]
numlist.sort()
print(numlist)



# .SPLIT METHOD AND .JOIN METHOD
name,age = "Nishad,18".split(",")
print(name)
print(age)



l1 = ["Mr.","Robot"]
print("".join(l1))



# Looping inside list
for fruit in fruits:
    print(fruit)



#LIST INSIDE LIST
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in matrix:
    print(i)



for i in matrix:
    for j in i:
        print(j)



lis = list(range(0,11))
print(lis)