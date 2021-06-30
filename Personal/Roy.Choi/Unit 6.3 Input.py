import sys

# a = input('Say something Please')
# print('value : {0}, type : {1}, size : {2} bytes'.format(str(a), type(a), sys.getsizeof(a)))

# a, b= input('Please enter two things').split(',')
# print(a, b)

# a, b= map(int, input('Please enter two things').split(','))
# print(a + b)


a, b, c = map(int, ('1', '2', '3'))
print('value : {0}, type : {1}, size : {2} bytes'.format(str(a), type(a), sys.getsizeof(a)))
