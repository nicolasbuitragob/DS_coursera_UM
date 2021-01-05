import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np

#%matplotlib notebook
n = 1000
# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, n)
#x2 = np.random.gamma(2, 1.5, 10000)
#x3 = np.random.exponential(2, 10000)+7
#x4 = np.random.uniform(14,20, 10000)

# plot the histograms
#plt.figure(figsize=(9,3))
#plt.hist(x1, density=True, bins=20, alpha=0.5)
#plt.hist(x2, density=True, bins=20, alpha=0.5)
#plt.hist(x3, density=True, bins=20, alpha=0.5)
#plt.hist(x4, density=True, bins=20, alpha=0.5);
#plt.axis([-7,21,0,0.6])

#plt.text(x1.mean()-1.5, 0.5, 'x1\nNormal')
#plt.text(x2.mean()-1.5, 0.5, 'x2\nGamma')
#plt.text(x3.mean()-1.5, 0.5, 'x3\nExponential')
#plt.text(x4.mean()-1.5, 0.5, 'x4\nUniform')
#plt.show()


def anim(curr):
    if curr == n:
        a.event_source.stop()
    plt.cla()
    bins = np.arange(-4, 4, 0.5)
    plt.hist(x1[:curr], bins=bins)
    plt.axis([-4,4,0,30])
fig = plt.figure()
a = animation.FuncAnimation(fig,anim,interval = 100)
plt.show()