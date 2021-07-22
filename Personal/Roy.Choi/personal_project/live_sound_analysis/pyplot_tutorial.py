import matplotlib.pyplot as plt
import numpy as np

# if not specified, x axis is generated automatically
# plt.plot ([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()

# the third argument is optional string which defines format of the line, default is b-
# plt.plot ([10, 20, 30, 100], [1, 2, 3, 4], 'ro')
# plt.xlabel('time')
# plt.ylabel('some numbers')
# plt.show()

# plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
# # define the display area
# plt.axis([0, 10, 0, 10])
# plt.show()

# # can draw multiple lines and also can use numpy
# t = np.arange(0, 5, 0.2)
# plt.figure(figsize = (10, 5))
# plt.plot(t, t, 'r--', t , t**2, 'bs', t, t**3, 'g^')
# plt.show()

# names = ['a', 'b', 'c']
# values = [1, 10, 100]
# # set size of overall screen size
# plt.figure(figsize = (9, 3))
# plt.subplot(131)
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
# plt.show()

# # Controlling line properties
# x = [1, 2, 3]
# y = [1, 4, 9]
# line, = plt.plot(x, y, linewidth = 5.0)
# line.set_linestyle('--')
# line.set_linewidth(2)
# line.set_xdata([1, 4, 9])
# line.set_ydata([1, 16, 81])
# plt.axis([0, 100, 0 ,100])
# plt.show()

# control many figures and subplot
x = [1, 2, 3]
y = [2, 4, 6]
plt.figure(1)
plt.subplot(121)
plt.plot(x, y, 'ro')
plt.subplot(122)
plt.plot(x, y, 'g-')
plt.subplot(121)
plt.axis([0, 10, 0 ,10])

plt.figure(2)
plt.plot(x, y, 'y-')
plt.figure(1)
plt.subplot(122)
plt.ylabel('Added title')
plt.show()
