#!/usr/bin/env python3

import pylab as plt

my_samples = []
my_linear = []
my_quadratic = []
my_cubic = []
my_exponential = []

for i in range(30):
    my_samples.append(i)
    my_linear.append(i)
    my_quadratic.append(i ** 2)
    my_cubic.append(i ** 3)
    my_exponential.append(1.5 ** i)

# plt.plot(my_samples, my_linear)
# plt.plot(my_samples, my_quadratic)
# plt.plot(my_samples, my_cubic)
# plt.plot(my_samples, my_exponential)
# plt.show()

# plt.figure('lin')
# plt.title('Linear')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.ylim(0, 1000)
# plt.plot(my_samples, my_linear)
# plt.plot(my_samples, my_quadratic)
# plt.show()  # after every show() i have to close the separate window
#
# plt.figure('quad')
# plt.title('Quadratic')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.ylim(0, 1000)
# plt.plot(my_samples, my_quadratic)
# plt.plot(my_samples, my_cubic)
# plt.show()
#
# plt.figure('cube')
# plt.title('Cubic')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.ylim(0, 1000)
# plt.plot(my_samples, my_cubic)
# plt.plot(my_samples, my_exponential)
# plt.show()
#
# plt.figure('expo')
# plt.title('Exponential')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.ylim(0, 1000)
# plt.plot(my_samples, my_exponential)
# plt.show()

# plt.figure('lin quad')
# plt.clf()
# plt.title('Linear vs. Quadratic')
# plt.plot(my_samples, my_linear, label='linear')
# plt.plot(my_samples, my_quadratic, label='quadratic')
# plt.legend(loc='upper left')
# plt.show()
#
# plt.figure('cube exp')
# plt.clf()
# plt.title('Cubic vs. Exponential')
# plt.plot(my_samples, my_cubic, label='cubic')
# plt.plot(my_samples, my_exponential, label='exponential')
# plt.legend(loc='upper left')
# plt.show()

# b - blue, r - red, g - green, k - black
# - - line, o - circle, ^ - triangle, -- - dash

plt.figure('lin quad')
plt.clf()
plt.subplot(211)
plt.ylim(0, 900)
plt.plot(my_samples, my_linear, 'b-', label='linear', linewidth=2.0)
plt.subplot(212)
plt.ylim(0, 900)
plt.plot(my_samples, my_quadratic, 'r', label='quadratic', linewidth=3.0)
plt.legend(loc='upper left')
plt.title('Linear vs. Quadratic')
plt.show()

plt.figure('cube exp')
plt.clf()
plt.subplot(121)
plt.ylim(0, 140000)
plt.plot(my_samples, my_cubic, 'g--', label='cubic', linewidth=4.0)
plt.subplot(122)
plt.ylim(0, 140000)
plt.plot(my_samples, my_exponential, 'r', label='exponential', linewidth=5.0)
plt.yscale('log')
plt.legend(loc='upper left')
plt.title('Cubic vs. Exponential')
plt.show()
