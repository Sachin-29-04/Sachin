
#dict
d={1:"python",2:"c++",3:"java",4:{1:"name",2:"surname"}}

print(d)
print(type(d))

print(d[1])
print(d[4][1])

dict={}
print(type(dict))
dict[0]="python"
dict[1]="c++"
dict[2]="java"
dict[3]={}
dict[3][1]="surname"
dict[3][2]="name"
print(dict)

print(dict.keys())
print(dict.get(2))
print(dict.values())
print(dict.pop(2))
print(dict)
print(dict.update(d))
print(dict)
print(dict.popitem())
print(dict)



#tuple 
l=(1,4,2,5,7)
print(l)
print(type(l))
print(l[0])
t=len(l)
print(t)

for x in range(t):
    print(x,l[x])

for x in l:
    print(x)

l1=(1,0,2,3,True)
l2=(4,5,7,3,False,None,"ff")

print(l1+l2)


l3=(l1,l2)
print(l3)

t=("xyx",)*3
print(t)

print(l1[1:4])
print(l1[:-1])
print(l1[::-1])

list=[1,2,4,5,7]
print(type(list))
l4=tuple(list)
print(type(l4))


print(max(l1))
print(sum(l1))
print(l1.count(1))
print(l2.index("ff"))


#set
set={"a","v","c" ,"c",1,"h",3,1}
print(type(set))
print(set)

set.add("r")
print(set)
set1={1,3,5,8,553,32}
s3=set.union(set1)
print(s3)
s4=set.intersection(set1)
print(s4)

set.clear()
print(set)
print(type(set))

