import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (10,5))
ax1 = fig.add_subplot(111)

x_measured = [0.669, 0.860, 0.986, 1.154, 1.407, 1.670]
y_measured = [2.637, 4.325, 5.639, 7.156, 9.513, 12.307]

k, b = np.polyfit(x_measured, y_measured, 1)

ax1.scatter(x_measured, y_measured, alpha=0.5, linewidths= 2)

ax1.errorbar(x_measured, y_measured, yerr=0.2, xerr = 0.01, color = 'black', linestyle = 'None')

x_measured.append(0)
y = k * (np.array(x_measured)) + b

ax1.plot(x_measured, y, 'r')

ax1.grid()
print(k, b)
plt.show()