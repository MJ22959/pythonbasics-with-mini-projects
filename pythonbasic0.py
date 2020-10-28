x=5
y=6
z=x+y
print(z)
print(x)
print(y)

print(type(3/1))
print(type(3/2))
print(type(3/3))
b=int(3/1)
print(type(b))
print(type(3/1))

a="Think positive"
print(a.replace('positive','negative'))


print(a[0:7])
print(a[0:5])

a = "David"
b = "name"
c = "is"
d = "my"
e = d + b + c + a
print(e)

f = "My name is {}".format(a)
print(f)

x="david"
print(f"My name is {x}")
y=["david","joshi",21]
print(f"{y[0]} age is {y[2]}")

print(dir(list))

x=[12,22,33,11,34,55,331,554,314,567,5776,643,767]
print(x[-2])
print(x[-1])
print(len(x))
print(x.pop())
print(x)
print(x.append(999))
print(x)

#del x
#print(x)

x = {"name":"David joshi", "Age":21, "Gender":"Male"}
print(x)
print(x["name"])
print(x["Age"])
print(x["Gender"])

x={"profession": "student"}
print(x)

print(4>5)

print(5//4)
print(4**2)
print(5%4)

x=4
x**=2
print(x)
x//=3
print(x)
x%=2
print(x)

print(3>2 and 4<5)
print(3>2 or 4<5)
print(not 3>2)

x=["ram", "shyam", "david"]
print("ram" in x)
print("mohit" in x)
print("mohit" not in x)

x=3
y=4
if(x==y):
    print("x is equal to y")
elif(x>y):
    print("x is greater than y")
else:
    print("x is less than y")


a = [0,1,2,3,4,5,6,7,8,9]
for i in a:
    a[i] = input("Enter the name")
print(a) 

i=0
while i<9:
    print(i)
    i+=1

x="David Joshi"
for i in x:
    print(i)

x=[0,1,2,3,4,5,6,7,8,9]
for i in x:
    print(i)
    if i==6:
     break

x=[0,1,2,3,4,5,6,7,8,9]
for i in x:
    if i==6:
      continue
    print(i)

for x in range(10,100,10):
    print(x)

x=["Mohit","Ankit","Rohit","David","Anuj"]
y=["Joshi","K.c","Sharma","Karki","Pandey"]
a=0
b=0
for i in x:
    for j in y:
        print(x[a],y[b])
        b+=1
    a+=1
    b=0


import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%c"))

file = open("python_part1.py", "r")
x = file.read()
print(x)

