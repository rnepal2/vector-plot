'''
This python program plots the vectors on a rectangular mesh.
The x, y and z components of vectors at (x, y) coordinates are
plotted using python scripts!
The input is text file containing columns of x, y, mx, my and mz. 
where m=(mx, my, mz) is a (magnetization) vector.
'''

import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import rc


def Plot(input_mag_texture):
    data_table = input_mag_texture
    x_position_list = []
    y_position_list = []
    mx_list = []
    my_list = []
    mz_list = []
    for i in range(len(data_table)):
        x_position = data_table[i][0]*1e9  # in nm
        y_position = data_table[i][1]*1e9  # in nm
        mx = data_table[i][3]
        my = data_table[i][4]
        mz = data_table[i][5]
        x_position_list.append(x_position)
        y_position_list.append(y_position)
        mx_list.append(mx)
        my_list.append(my)
        mz_list.append(mz)
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.quiver(x_position_list, y_position_list, mx_list, my_list, mz_list, cmap=plt.cm.RdBu)
    cbar = plt.colorbar()
    cbar.set_clim(vmin=-1, vmax=1)
    cbar.set_label(r"$m_z$", fontsize=14)
    plt.title(r'Skyrmion Lattice', fontsize=14)
    plt.xlabel(r"$x-position (nm)$", fontsize=14)
    plt.ylabel(r"$y-position (nm)$", fontsize=14)
    plt.xlim(0, 128)
    plt.ylim(0, 128)
    plt.axes().set_aspect('equal')
    plt.show()

input_data = np.loadtxt("mag_texture.txt", skiprows=2)
#Plotting
Plot(input_data)
 
