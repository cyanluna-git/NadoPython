Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1+1
2
>>> 1-2
-1
>>> 2*2
4
>>> 5/2
2.5
>>> 4/2
2.0
>>> 5//2
2
>>> 4//2
2
>>> 5.5//2
2.0
>>> 4//2.0
2.0
>>> 4.1//2.1
1.0
>>> 5/2
2.5
>>> 5//2
2
>>> 5%2
1
>>> 2**
  File "<stdin>", line 1
    2**
       ^
SyntaxError: invalid syntax
>>> 2**3
8
>>> 2**10
1024
>>> int(3.3)
3
>>> int(5/2
...
... int(5/2)
  File "<stdin>", line 3
    int(5/2)
    ^
SyntaxError: invalid syntax
>>> int(5/2)
2
>>> int('10')
10
>>> int('10.3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '10.3'
>>> int(-8.3)
-8
>>> type(10)
<class 'int'>
>>> divmod(5,2)
(2, 1)
>>>  a,b=divmod(5,2)
  File "<stdin>", line 1
    a,b=divmod(5,2)
IndentationError: unexpected indent
>>> a,b=divmod(5,2)
>>> print(1,b)
1 1
>>> print(a,b)
2 1
>>> 0b110
6
>>> 0o10
8
>>> 0xf
15
	
SyntaxError: multiple statements found while compiling a single statement
>>> 1+1
2
>>> 3.5+2.1
5.6
>>> 4.3-2.7
1.5999999999999996
>>> 5.5/3.1
1.7741935483870968
>>> float(5)
5.0
>>> float(1+2)
3.0
>>> float(5.3)
5.3
>>> float('5.3)
      
SyntaxError: EOL while scanning string literal
>>> float('5.3')
5.3
>>> type(3.5)
<class 'float'>
>>> 1.2+1.3j
(1.2+1.3j)
>>> complex(1.2,1.3)
(1.2+1.3j)
>>> 1+1
2
>>> print(1+1)
2
>>> 7+(10-5)*2
17
>>> print(0.2467*12+4.159)
7.1194
>>> int(0.2467*12+4.159)
7
>>> print(102*0.6+225)
286.2
>>> x=10
>>> x
10
>>> y='Hello,world!'
>>> y
'Hello,world!'
>>> type(x)
<class 'int'>
>>> type(y)
<class 'str'>
>>> x,y,z=10,20,30
>>> x
10
>>> y
20
>>> z
30
>>> x=y=x=10
>>> x
10
>>> y
10
>>> z
30
>>> x=y=z=10
>>> x
10
>>> y
10
z
>>> 
>>> z
10
>>> x,y=10,20
>>> x,y=y,z
>>> x
20
>>> y
10
>>> del z
>>> del x
>>> x
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> del y
>>> y
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> x=none
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    x=none
NameError: name 'none' is not defined
>>> x=None
>>> x
>>> print(x)
None
>>> x
>>> x
>>> a=10
>>> b=20
>>> c=a+b
>>> c
30
>>> a+20
30
>>> a
10
>>> a=a+20
>>> a
30
>>>  a+=20
 
SyntaxError: unexpected indent
>>> a+=20
>>> a
50
>>> a=10
>>> a+=20
>>> a
30
>>>  x=-10
 
SyntaxError: unexpected indent
>>> x=-10
>>> x-
SyntaxError: invalid syntax
>>> +x
-10
>>> -x
10
>>> input()
Hello, World!
'Hello, World!'
>>> input()
good job
'good job'
>>> x=input()
Hello, World!
>>> x
'Hello, World!'
>>> x=input(Hello,World!)
SyntaxError: invalid syntax
>>> x=input('Hello, World!')
Hello, World!x
>>> x
'x'
>>> x
'x'
>>> x=input(Hello, world!)
SyntaxError: invalid syntax
>>> x=input('Hello, world!')
Hello, world!
>>> x
''
>>> x=input('문자열을 입력하세요:')
문자열을 입력하세요:Hello, World!
>>> x
'Hello, World!'
>>>  a=input('첫 번째 숫자를 입력하세요:')
 
SyntaxError: unexpected indent
>>> a=input('첫 번째 숫자를 입력하세요:')
첫 번째 숫자를 입력하세요:10
>>> b=input('두 번째 숫자를 입력하세요:')
두 번째 숫자를 입력하세요:20
>>> print(a+b)
1020
>>> type(a)
<class 'str'>
>>> type(b)
<class 'str'>
>>> a,b=input('문자열 두 개를 입력하세요:'), Split()
문자열 두 개를 입력하세요:print(a)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a,b=input('문자열 두 개를 입력하세요:'), Split()
NameError: name 'Split' is not defined
>>> print(a)
10
>>> a,b=input('문자열 두 개를 입력하세요:'). Split()
문자열 두 개를 입력하세요:
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    a,b=input('문자열 두 개를 입력하세요:'). Split()
AttributeError: 'str' object has no attribute 'Split'
>>> a,b=input('문자열 두 개를 입력하세요:'),Split()
문자열 두 개를 입력하세요:
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a,b=input('문자열 두 개를 입력하세요:'),Split()
NameError: name 'Split' is not defined
>>> a,b=input('문자열 두 개를 입력하세요:').Split()
문자열 두 개를 입력하세요:
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a,b=input('문자열 두 개를 입력하세요:').Split()
AttributeError: 'str' object has no attribute 'Split'
>>> a,b=input('문자열 두 개를 입력하세요:').split()
문자열 두 개를 입력하세요:
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a,b=input('문자열 두 개를 입력하세요:').split()
ValueError: not enough values to unpack (expected 2, got 0)
>>> a,b=input('문자열 두 개를 입력하세요:').split()
문자열 두 개를 입력하세요:
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    a,b=input('문자열 두 개를 입력하세요:').split()
ValueError: not enough values to unpack (expected 2, got 0)
>>> a,b=input('문자열 두 개를 입력하세요:').split( )
문자열 두 개를 입력하세요:
========= RESTART: C:/Users/yoonsy/Desktop/Python/input_split_string.py ========
================================ RESTART: Shell ================================
>>> 
문자열 두 개를 입려하세요:Hello Python
Hello
Python
>>> 
========= RESTART: C:/Users/yoonsy/Desktop/Python/input_split_string.py ========
숫자 두 개를 입력하세요:10 20
1020
>>> 
========= RESTART: C:/Users/yoonsy/Desktop/Python/input_split_string.py ========
숫자 두 개를 입력하세요:10 20
>>> 
========= RESTART: C:/Users/yoonsy/Desktop/Python/input_split_string.py ========
숫자 두 개를 입력하세요:10 20
30
>>> 
========= RESTART: C:/Users/yoonsy/Desktop/Python/input_split_string.py ========
숫자 두 개를 입력하세요:10 20
30
>>> 
========= RESTART: C:/Users/yoonsy/Desktop/Python/input_split_string.py ========
숫자 두 개를 입력하세요:10,20
30
>>> a,b,c=map(int,input().split())
a=-10
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a,b,c=map(int,input().split())
ValueError: invalid literal for int() with base 10: 'a=-10'
>>> a=-10
>>> b=20
>>> c=30
>>> 
========= RESTART: C:/Users/yoonsy/Desktop/Python/input_split_string.py ========
-10 20 30
40
>>> 
========= RESTART: C:/Users/yoonsy/Desktop/Python/input_split_string.py ========
50 100 None
50
100
Traceback (most recent call last):
  File "C:/Users/yoonsy/Desktop/Python/input_split_string.py", line 4, in <module>
    pring(c)
NameError: name 'pring' is not defined
>>> 
========= RESTART: C:/Users/yoonsy/Desktop/Python/input_split_string.py ========
50 100 None
50
100
None
>>> a,b,c=50,100,None
>>> a
50
>>> b
100
>>> c
>>> 
========= RESTART: C:/Users/yoonsy/Desktop/Python/input_split_string.py ========
32 53 22 95
Traceback (most recent call last):
  File "C:/Users/yoonsy/Desktop/Python/input_split_string.py", line 1, in <module>
    a,b,c,d=map(input().split())
TypeError: map() must have at least two arguments.
>>> 
========= RESTART: C:/Users/yoonsy/Desktop/Python/input_split_string.py ========
32 53 22 95
Traceback (most recent call last):
  File "C:/Users/yoonsy/Desktop/Python/input_split_string.py", line 5, in <module>
    a,b,c,d=map(input().split())
TypeError: map() must have at least two arguments.
>>> 
========= RESTART: C:/Users/yoonsy/Desktop/Python/input_split_string.py ========
32 53 22 95
50.5
>>> 
========= RESTART: C:/Users/yoonsy/Desktop/Python/input_split_string.py ========
32 53 22 95
50
>>> 