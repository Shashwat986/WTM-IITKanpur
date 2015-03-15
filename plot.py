import matplotlib.pyplot as plt
import pylab
import numpy as np

plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.plot([0,1,2,3,4], [0,1,4,9,16], 'g--')
plt.ylabel('Some Numbers')
plt.axis([0, 6, 0, 20])
plt.show()


x_vals = np.linspace(-1,1,1000)
y_vals = [x*np.sin(1.0/x) for x in x_vals]
plt.plot(x_vals,y_vals)
plt.show()

fp = open("wings.txt")
vals = [int(k.strip()) for k in fp.readlines()]
fp.close()
pylab.hist(vals)
pylab.show()
