Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(1,2,3)
1 2 3
>>> print('Hello','Python')
Hello Python
>>> a=10
>>> b=20
>>> c=30
>>> print(a,b,c)
10 20 30
>>> print(1,2,3,sep=', ')
1, 2, 3
>>> print(4,5,6,sep=",")
4,5,6
>>> print('Hello','Python',sep='')
HelloPython
>>> Print(1920,1080,se='x')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    Print(1920,1080,se='x')
NameError: name 'Print' is not defined
>>> Print(1920,1080,sep='x')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    Print(1920,1080,sep='x')
NameError: name 'Print' is not defined
>>> print(1920,1080,sep='x')
1920x1080
>>> print(1,2,3,sep='\n')
1
2
3
>>> print('1\n2\n3')
1
2
3
>>> print(1,2,3,sep='\n')
1
2
3
>>> print(1,2,3,sep='\t')
1	2	3
>>> print(1,2,3,sep='\\')
1\2\3
>>> 