import sys
a = 10
# Actual size of integer is 4 bytes
# Remember integer is also class so consumes more memory
print('value : {0}, type : {1}, size : {2} bytes'.format(str(a), type(a), sys.getsizeof(a)))
a = a == 10
print('value : {0}, type : {1}, size : {2} bytes'.format(str(a), type(a), sys.getsizeof(a)))
a = 'Hi'
print('value : {0}, type : {1}, size : {2} bytes'.format(str(a), type(a), sys.getsizeof(a)))
# Sting : Base 49 Bytes + 1 Byte per a charactor
a = 'Hello'
print('value : {0}, type : {1}, size : {2} bytes'.format(str(a), type(a), sys.getsizeof(a)))

x, y, z = 10, 20, 30
print(x, y, z)
k = 3
_, j, m = 10, 20, 30
print(k, j, m)

x = y = z = k = j = m = 0
print(x, y, z, k, j, m)

x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)

x = 10
# del(x)
# x is not defined
print(x)

a = None
print('value : {0}, type : {1}, size : {2} bytes'.format(str(a), type(a), sys.getsizeof(a)))
a = 3
print('value : {0}, type : {1}, size : {2} bytes'.format(str(a), type(a), sys.getsizeof(a)))