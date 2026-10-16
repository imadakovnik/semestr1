import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize = (9,8)) 
ax1 = fig.add_subplot(221) 
ax2 = fig.add_subplot(222) 
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)


a = np.random.normal(0, 10, 100)
ax1.hist(a, 10, label='n=100')
ax1.legend()
ax1.set_xlabel('Плотность вероятности')
ax1.set_ylabel('Значения')

a = np.random.normal(0, 10, 1000)
ax2.hist(a, 50, label='n=1000')
ax2.legend()
ax2.set_xlabel('Плотность вероятности')
ax2.set_ylabel('Значения')

a = np.random.normal(0, 10, 10000)
ax3.hist(a, 100, label='n=10000')
ax3.legend()
ax3.set_xlabel('Плотность вероятности')
ax3.set_ylabel('Значения')

a = np.random.normal(0, 10, 100000)
ax4.hist(a, 500, label='n=100000')
ax4.legend()
ax4.set_xlabel('Плотность вероятности')
ax4.set_ylabel('Значения')


plt.show()