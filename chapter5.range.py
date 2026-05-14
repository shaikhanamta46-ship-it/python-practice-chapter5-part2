#range - range functions returns a sequence of numbers, starting from 0 by default, and increasing
#by 1 ( by default), and ends at a specified number.
#range syntax
#range(start,stop,step)

seq = range(5)
for i in seq:
    print(i)


print(seq[2])
print(seq[0])
print(seq[3])
print(seq[3])

#start and stop

for i in range(11): #range stop
    print(i)


for el in range(1,11): #range start and stop
    print(el)


for sen in range(2,10,2): #range( start,stop,step)
    print(sen)


for t in range(1,101,2):
    print(t)

#lets practice
#practice question1,2
for m in range(100,0,-1):
    print(m)

#practice question3
n = int(input("enter a number:"))
for s in range(1,11):
    print(n*s)


#pass statement - do nothing statement

for r in range(4):
   pass

print("some useful code")


#practice question 4 

n = 9

sum = 1
for u in range(1,n+1):
    sum += u
    print("total sum=",sum)

#by while loop
t = 9
p = 1
while(p <= t):
    p += 1
    sum += p
    print("total sum=", sum)

# practice question 5

n = 5 
fact = 1
for f in range(1,n+1):
    fact *= f
    print("factorial=",fact)

#while loop 

n = 6 
fact = 1
i = 1
while(i <= n):
    fact *= i
    i += 1
    print("factorial=",fact)
    