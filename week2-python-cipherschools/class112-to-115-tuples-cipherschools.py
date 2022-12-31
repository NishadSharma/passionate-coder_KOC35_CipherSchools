# TUPLES ARE IMMUTABLE

example = ("one","two","three")
mixed = (1,2,3,4,5)
for i in mixed:
    print(i)



tup = (1,)
tup2 = (1)
print(type(tup))
print(type(tup2))


print(sum(mixed))



# Function returning two values

def func(a,b):
    add = a+b
    multi = a*b
    return add,multi



print(func(3,2))



nums = tuple(range(1,11))
print(nums)



# we can convert tuple to string or tuple to list