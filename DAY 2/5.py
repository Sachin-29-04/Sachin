# (5) smallest number in a list

l=[2,2,1,4,6,53]

mini=l[0]

for x in l:
    if(x<mini):
        mini=x


print("min element is",mini)

#max number in a list

l=[2,2,1,4,6,53]

max=l[0]

for x in l:
    if(x>max):
        max=x


print("max element is",max)

#smallest second number in a list

l=[7,3,1,2,6,53]

mini1=l[0]
mini2=l[0]

for x in l:
    if(x<mini1):
        mini1=x

for x in l :
    if(x<mini2 and x!= mini1) :
        mini2=x


print("second min element is",mini2)

#max second number in a list

l=[7,9,1,2,6,53]

max1=l[0]
max2=l[0]

for x in l:
    if(x>mini1):
        max1=x

for x in l :
    if(x>max2 and x!= max1) :
        max2=x


print("second max element is",max2)
