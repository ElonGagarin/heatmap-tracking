from scipy.stats.kde import gaussian_kde
import numpy as np
x = np.array([])
y = np.array([])
im = np.array([])

k = gaussian_kde(np.vstack([x[::10], y[::10]]))
# xi, yi = np.mgrid[0:4995:4995**0.5*1j,0:3531:y.size**0.5*1j]
xi, yi = np.mgrid[0:4995:10,0:3531:10]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

plt.rcParams['figure.figsize'] = (23.0, 10.0) # set default size of plots

levels = MaxNLocator(nbins=1000).tick_values(   .min(), zi.max())
cmap = plt.get_cmap('YlOrRd')

# alpha=0.5 will make the plots semitransparent
cnt = plt.contourf(xi, yi, zi.reshape(xi.shape), alpha=0.2, levels=levels, cmap=cmap, linestyles=None)

for c in cnt.collections:
    c.set_edgecolor("none")

# plt.colorbar()

plt.gca().set_xlim(450, 3900)
plt.gca().set_ylim(1000, 2500)
# ax1.set_ylim(ax1.get_ylim()[::-1])
plt.imshow(im[::-1,:,:], extent=[0, 4995, 0, 3531], aspect='auto')
plt.gca().invert_yaxis()

plt.axis('off')

plt.savefig('heatmap_mans.png', bbox_inches='tight', pad_inches=0)