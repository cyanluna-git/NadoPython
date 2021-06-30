# 5.1 Integer Calculation
#Integer / integer = float ( In Python 3)
a = 9 / 3
print(a)
print(type(a))

#Integer // integer = int ( In Python 3)
a = 10//3
print('value : {0}, type : {1}'.format(str(a), type(a)))

#float // integer = int ( In Python 3)
a = 10.0//3
print('value : {0}, type : {1}'.format(str(a), type(a)))

a = 10 % 4
print('value : {0}, type : {1}'.format(str(a), type(a)))

# int function
a = int(9/2)
print('value : {0}, type : {1}'.format(str(a), type(a)))
a = int('8')
print('value : {0}, type : {1}'.format(str(a), type(a)))
# Error is string argument is not integer
# a = int('3.3')
# print('value : {0}, type : {1}'.format(str(a), type(a)))
# int , // removes remainder
# sometime might need round function
a = round(3.6)
print('value : {0}, type : {1}'.format(str(a), type(a)))

# the result of the function divmod is 'tutple'
quotient, remainder = divmod(5, 2)
print(quotient, remainder)

_, remainder = divmod(10, 2)
print(quotient, remainder)

a = (3, 2, 1 , 'apple')
print(type(a))

a = 0b1111
print('value : {0}, type : {1}'.format(str(a), type(a)))
print(a == 15)
a = 0o0101
print('value : {0}, type : {1}'.format(str(a), type(a)))
a = 0x0000133
print('value : {0}, type : {1}'.format(str(a), type(a)))