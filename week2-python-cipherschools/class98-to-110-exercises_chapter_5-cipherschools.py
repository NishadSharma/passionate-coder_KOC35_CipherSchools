#EXERCISE 1
def square(l):
    sq = []
    for i in l:
        sq.append(i**2)
    return sq
l1 = list(range(0,11))
square(l1)



#EXERCISE 2
def revlist(l):
    l.reverse()
    return l
l1 = [1,2,3,4,5]
revlist(l1)



#EXERCISE 3
def revwords(l):
    revlist = []
    for i in l:
        revlist.append(i[::-1])
    return revlist
strl = ["You","Dog","Last"]
revwords(strl)



#EXERCISE 4
def oddevenl(l):
    oddnums = []
    evennums = []
    for i in l:
        if i%2 == 0:
            evennums.append(i)
        else:
            oddnums.append(i)
    output = [oddnums,evennums]
    return output
l1 = [1,2,3,4,5,6,7]
oddevenl(l1)



#EXERCISE 5
def iscommon(l1,l2):
    common = []
    for i in l1:
        if i in l2:
            common.append(i)
    return common
l1 = [1,2,3,4,8,9,10]
l2 = [5,6,2,3,4]
iscommon(l1,l2)



#EXERCISE 6
def listcounter(l1):
    count = 0
    for i in l1:
        if type(i) == list:
            count += 1 
    return count
l1 = [1,2,3,[1,2,3],[3,5,6],[789]]
listcounter(l1)
