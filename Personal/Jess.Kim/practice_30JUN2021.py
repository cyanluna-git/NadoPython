Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> scores = [80, 75, 55]
>>> total = 0
>>> for var in scores:
	total = total + var

	
>>> avg = total/len()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    avg = total/len()
TypeError: len() takes exactly one argument (0 given)
>>> avg = total/len(scores)
>>> avg
70.0
>>> total
210
>>> total =0
>>> total
0
>>> avg
70.0
>>> avg=0
>>> avg
0
>>> total = sum(scores)
>>> avg = total/len(scores)
>>> toatl
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    toatl
NameError: name 'toatl' is not defined
>>> totla
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    totla
NameError: name 'totla' is not defined
>>> total
210
>>> avg
70.0
>>> add = 90
>>> score.extend(add)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    score.extend(add)
NameError: name 'score' is not defined
>>> scores.extend(add)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    scores.extend(add)
TypeError: 'int' object is not iterable
>>> number = 16
>>> %number
SyntaxError: invalid syntax
>>> number %2
0
>>> even = number%2
>>> even
0
>>> if even == 0
SyntaxError: invalid syntax
>>> if even ==0:
	print("even")

	
even
>>> jumin='900118-1235488'
>>> birth=jumin.split('-')
>>> birth
['900118', '1235488']
>>> birth[0]
'900118'
>>> birth[1]
'1235488'
>>> jumin.strip[0:6]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    jumin.strip[0:6]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> jumin[0:6]
'900118'
>>> gender=jumin[7]
>>> if gender == 1:
	print("male")

	
>>> 
>>> gender
'1'
>>> gender =0
>>> gender
0
>>> gender=jumin[7]
>>> gender
'1'
>>> if gender == 1:
	print("male")

	
>>> 
>>> a = [1,3,5,7,3,6,7]
>>> print(a)
[1, 3, 5, 7, 3, 6, 7]
>>> a.sort
<built-in method sort of list object at 0x00000243FCC1AD80>
>>> a.sort()
>>> a
[1, 3, 3, 5, 6, 7, 7]
>>> a.reverse
<built-in method reverse of list object at 0x00000243FCC1AD80>
>>> a.reverse()
>>> a
[7, 7, 6, 5, 3, 3, 1]
>>> sent = ['Life', 'is', 'short']
>>> sent
['Life', 'is', 'short']
>>> space = ' '
>>> space
' '
>>> b=space.join(a)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    b=space.join(a)
TypeError: sequence item 0: expected str instance, int found
>>> b=space.join(sent)
>>> b
'Life is short'
>>> list = [1,1,1,2,2,3,3,3,4,4,5]
>>> list
[1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
>>> set(list)
{1, 2, 3, 4, 5}
>>> a=b=[1,2,3]
>>> a
[1, 2, 3]
>>> b
[1, 2, 3]
>>> g=[1,4,6]=c
SyntaxError: cannot assign to literal
>>> 