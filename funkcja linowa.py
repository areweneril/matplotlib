import pylab
'''
x = [1,2,3]
y = [4,5,6]

pylab.plot(x,y)
pylab.show()

a = 1
b = 2

x = range(-10, 10)

y = []

for i in x:
    y.append(a * i + b)

pylab.plot(x,y)
pylab.title("Wykres f(x) = a*x +b")
pylab.grid(True)
pylab.show()
'''
a = 2
x = range(11)
for i in x:
    print(a+i)
y = [a+i for i in range(11)]
print(y)

x = pylab.arange(-10, 10, 0.5)
print(x)
len(x)
a = 3
y1 = [i / -3 + a for i in x if i <= 0]