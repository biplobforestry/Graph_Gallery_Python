# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:09:23 2024

@author: b.dey
"""

import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np
import math
import matplotlib.patches as patches
import tkinter as tk
%matplotlib tk
root = tk.Tk()
root.withdraw()
plt.style.use('fivethirtyeight')

# make figure and assign axis objects
fig = plt.figure(figsize=(15,7.5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)


fig.suptitle('A. Ozone stress', fontsize=20, fontname='Times New Roman', va='center')
ratios = [0.17, 8.69, 3.84, 82.36, 0.12, 1.58, 3.2] 
labels = ['Acid', 'Alcohol', 'Carbonyl', 'CxHy', 'CxHyNO','Others','Isoprene']
others_ratios = [0.09, 0.7, 0.02,0.78] #percentages of "others" group



explode = [0.1, 0, 0, 0,-0.2, 0.1,0]  # Only explode the "Others" group
colors_main = [ '#FF0000','#15B01A','#00FFFF','#FFD700','#f52ac9','#6E750E','#DDA0DD']

legend_labels = [f'{name}: {value:.2f}' for name, value in zip(
    ['Aromatic (%)', 'CxHyO (%)','Sesquiterpenes (%)', 'Monoterpenes (%)'],
    others_ratios
)]

# rotate so that the "Others" wedge is on the right-side middle
angle = -350 * (sum(ratios[:-1]) + ratios[-1] / 2) / sum(ratios)
wedges, texts, autotexts = ax1.pie(ratios, autopct='%1.1f%%', startangle=angle, labels=labels, explode=explode, colors=colors_main)

# pie chart text properties control
for text in texts:
    text.set_fontname('Times New Roman')
    text.set_fontsize(20)
for autotext in autotexts:
    autotext.set_fontname('Times New Roman')
    autotext.set_fontsize(20)

# bar chart parameters for "Others" breakdown
xpos = 0
bottom = 0
width = 0.2
colors_others = [ '#069AF3', '#FC5A50','#D2B48C','#FA8072']

# Plot bars
for j in range(len(others_ratios)):
    height = others_ratios[j]
    ax2.bar(xpos, height, width, bottom=bottom, color=colors_others[j])
    bottom += height
#ax2.set_title('(%)', fontsize=16, fontname='Times New Roman')
# customize legend
legend = plt.legend(legend_labels, loc='best')
for text in legend.get_texts():
    text.set_fontname('Times New Roman')
    text.set_fontsize(17)

plt.axis('off')
plt.xlim(-2.5 * width, 3 * width)

# use ConnectionPatch to draw lines between the two plots
theta1, theta2 = ax1.patches[5].theta1, ax1.patches[5].theta2
center, r = ax1.patches[5].center, ax1.patches[5].r
bar_height = sum([item.get_height() for item in ax2.patches])

x = r * np.cos(math.pi / 180 * theta2) + center[0]
y = np.sin(math.pi / 180 * theta2) + center[1]
con = ConnectionPatch(xyA=(-width / 2, bar_height), xyB=(x, y), coordsA="data", coordsB="data",
                      axesA=ax2, axesB=ax1)
con.set_color([0, 0, 0])
con.set_linewidth(4)
ax2.add_artist(con)

x = r * np.cos(math.pi / 180 * theta1) + center[0]
y = np.sin(math.pi / 180 * theta1) + center[1]
con = ConnectionPatch(xyA=(-width / 2, 0), xyB=(x, y), coordsA="data", coordsB="data",
                      axesA=ax2, axesB=ax1)
con.set_color([0, 0, 0])
ax2.add_artist(con)
con.set_linewidth(4)
#plt.savefig('C:/BIPLOB/Biplob Thesis/Beech Presentation/Fig_Pie_2.png', format='png', dpi=500, bbox_inches='tight', pad_inches=0)
plt.show()