Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> bin(25)
'0b11001'
>>> 0b11001
25
>>> oct(25)
'0o31'
>>> hex(25)
'0x19'
>>> hex(10)
'0xa'
>>> 0xa
10
>>> 4//3
1
>>> 8//2
4
>>> import math
>>> x= math.floor(6.9)
>>> x
6
>>> y=math.ceil(6.9)
>>> y
7
>>> z= math.pow(2,3)
>>> z
8.0
>>> print(math.ceil(z))
8
>>> print(math.floor(z))
8
>>> print(math.pi)
3.141592653589793
>>> print(math.e)
2.718281828459045
>>> import math as m
>>> m.sqrt(25)
5.0
>>> math.sqrt(25)
5.0
>>> from math import sqrt, pow
>>> pow(4,5)
1024.0
>>> sqrt(25)
5.0
>>> x=input("Enter your first name")
Enter your first nameMohit
>>> y=input("Enter your last name")
Enter your last nameJoshi
>>> print("Your name is",x+y)
Your name is MohitJoshi
>>> x=int(input("Enter 1st no"))
Enter 1st no2
>>> y=int(input("Enter 2nd number"))
Enter 2nd number3
>>> print(z=x+y)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(z=x+y)
TypeError: 'z' is an invalid keyword argument for print()
>>> print("z=", x + y)
z= 5
>>> ch=input("Enter a character")[0]
Enter a charactermohit
>>> ch
'm'
>>> import sys
>>> x=int(sys.argv[1])
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    x=int(sys.argv[1])
IndexError: list index out of range
>>> 
