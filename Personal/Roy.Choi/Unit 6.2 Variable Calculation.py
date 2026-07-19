import sys

a = 10
a = a + 20
print('value : {0}, type : {1}, size : {2} bytes'.format(str(a), type(a), sys.getsizeof(a)))
a = 10
a += 20
print('value : {0}, type : {1}, size : {2} bytes'.format(str(a), type(a), sys.getsizeof(a)))

# b is not defined
# b += 5
# print('value : {0}, type : {1}, size : {2} bytes'.format(str(b), type(b), sys.getsizeof(b)))