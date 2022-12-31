user = {"name":"Nishad","age":18}
print(user)
print(type(user))



user2 = dict(name = "nishad",age = 25)
print(user["age"])



userinfo = {
    "name" : "Subhajeet",
    "age" : 24,
    "fav_movies" : ["top gun","Ice age"],
    "fav_tunes" : ["breathing","Cold"] 
}
print(userinfo["fav_movies"])



# Dictionaries values can be changed

if 'name' in userinfo:
    print("Present")


if 'Subhajeet' in userinfo.values():
    print("Present")


userinfov = userinfo.values()
print(userinfo)

for i in userinfo:
    print(i)



for i in userinfo:
    print(userinfo[i])



userinfo['fav_tunes']= ['song1','song2']
print(userinfo)


userinfo.pop('fav_tunes')
print(userinfo)


moreinfo = {"state":"Odisha","Hobbies":["Coding","Sports"]}
userinfo.update(moreinfo)

print(userinfo)


# From keys
# Get method
# Claer
# Get
d = {'name':"unknown",'age':'unknown'}
f = dict.fromkeys(['name','age','height'],'unknown')
print(f)


if f.get('name'):
    print('Present')


f1 = f.copy()
f1.pop('age')
print(f1)
print(f)
print(f1 is f)
print(f1 == f)


#EXERCISE 1
def cube(n):
    cubes = {}
    for i in range(1,n+1):
        cubes[i] = i**3
    return cubes
print(cube(5))


#Word Counter
def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count
print(word_counter("Nishad"))



#EXERCISE 2
user5 = {}
name = input("What is your name : ")
age = int(input("Enter your age : "))
movies = input("Enter the name of your fav mvoies separated by ,:").split(",")
songs = input("Enter the name of your fav songs separated by ,:").split(",")
user5['name'] = name
user5['age'] = age
user5['movies'] = movies
user5['songs'] = songs
print(user5)