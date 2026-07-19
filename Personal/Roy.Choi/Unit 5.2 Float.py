a = 3.5 + 2.1
print('value : {0}, type : {1}'.format(str(a), type(a)))
# Unexpected result
a = 4.3 - 2.7
print('value : {0}, type : {1}'.format(str(a), type(a)))

# float + integer = float
a = 9.0 + 5
print('value : {0}, type : {1}'.format(str(a), type(a)))

a = 5
print('value : {0}, type : {1}'.format(str(a), type(a)))
a = float(a)
print('value : {0}, type : {1}'.format(str(a), type(a)))
a = float('5')
print('value : {0}, type : {1}'.format(str(a), type(a)))
a = float('5.3')
print('value : {0}, type : {1}'.format(str(a), type(a)))

a = 3 + 1.5j
print('value : {0}, type : {1}'.format(str(a), type(a)))

a = complex(3, 1.5)
print('value : {0}, type : {1}'.format(str(a), type(a)))

