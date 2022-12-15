Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello)
	  
SyntaxError: EOL while scanning string literal
>>> print("hello")
	  
hello
>>> a=10
	  
>>> print(type(a))
	  
<class 'int'>
>>> a=9
	  
>>> print(bin(a))
	  
0b1001
>>> import keyword
	  
>>> keyword.kwlist
	  
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> print(oct(9))
	  
0o11
>>> print(oct(0b11))
	  
0o3
>>> print(oct(0x9))
	  
0o11
>>> print(hex(9))
	  
0x9
>>> print(hex(0b11))
	  
0x3
>>> print(hex(0o7))
	  
0x7
>>> f=12.34
	  
>>> print(type(f))
	  
<class 'float'>
>>> print(int(f))
	  
12
>>> c=0b11+5j
	  
>>> print(type(C))
	  
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(type(C))
NameError: name 'C' is not defined
>>> c=0b11+5j
	  
>>> print(type(c))
	  
<class 'complex'>
>>> a=10
	  
>>> b=3
	  
>>> c=a<b
	  
>>> print(C)
	  
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(C)
NameError: name 'C' is not defined
>>> print(c)
	  
False
>>> a='sunitha'
	  
>>> print(type(a))
	  
<class 'str'>
>>> print(a[0:4])
	  
suni
>>> print(float(true))
	  
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(float(true))
NameError: name 'true' is not defined
>>> print(float(True))
	  
1.0
>>> print(complex(True))
	  
(1+0j)
>>> g=12e3
	  
>>> print(g)
	  
12000.0
>>> b=True
	  
>>> print(type(p))
	  
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(type(p))
NameError: name 'p' is not defined
>>> print(type(p))
	  
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(type(p))
NameError: name 'p' is not defined
>>> print(type(b))
	  
<class 'bool'>
>>> 
