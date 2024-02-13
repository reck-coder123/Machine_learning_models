# a=input("Enter your first number: ")
# opt=input("choose oprator (+,-,*,/): ")
# b=input("Enter your second number: ")

# ans=0

# if opt=='+':
#     ans=int(a)+int(b)
# elif opt=='-':
#     ans=int(a)-int(b)
# elif opt=='*':
#     ans=int(a)*int(b)
# else:
#     ans=int(a)/int(b)

# print("Your ans is: ",ans)
apple='He said, " I want to eat an apple"'
# for i in apple:
#     print(i)
# print(apple)
length=len(apple)
print(length)
print(apple[:5])
nm="Harry"
print(nm[-4:-2])
#strings are immutable, whenever we apply any change to the string, we get new string
print(nm.upper())
print(nm.lower())
#to strip later same string characters not leading
a="harry##%##&"
print(a.rstrip("#"))
# to change all the occurance of a char array in string to something else using replace
print(a.replace("harry","Ayush"))
test="let's##see###this"
print(test.find("##7"))

#list
lst=[3,4,5,6,7]
print(lst.index(8)) #Error
#slicing similar to string

newlst=[i for i in range(10)]
# print(newlst)
newlst.append(67)
tst=newlst.copy()
tst[0]=5
print(tst[0])
tst.insert(3,78)
tst.sort()

#tuple
tup=(9,8,3,5, 4, 5 ,3, 5)
print(tup.index(3,3,7))
print(len(tup))
ttol=list(tup)
ttol.append(78)
tup=tuple(ttol)
print(tup)

#Recursion
def addtion(n):
    if n<=1:
        return 1
    
    return n*addtion(n-1)
print(addtion(4))

#Sets
st={9,8,7}
st.add(8)
st.remove(7)

has=set() #an empty set, not this has={} --> this is a dictionary
has.add(5)
has.add(98)
has.add(8)
print(st.intersection(has))
print(st,has)
has.remove(90) # error as 90 is not there
has.discard(90) # no error


#Dictionary
dic={
    23:"Ayush",
    55:"Neha",
    67:"89"
}
if 23 in dic:
    print(1)
for key, value in dic.items():
    print({key},{value})

ep={122: 45, 123:89, 145: 78}
ep2={222:67, 556:90}
ep.update(ep2)
ep.pop(227) #error
print(ep)

#for loop with else
for i in []:
    print(i)
else:
    print("no")

i=0

while i<7:
    print(i)
    i=i+1
else :
    print("nice")

#Expection Handling
import math
print(dir(math))