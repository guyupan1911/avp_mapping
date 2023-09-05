"""
scripts preprocess 4seasons dataset
"""

import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def set_axes_equal(ax: plt.Axes):
    """Set 3D plot axes to equal scale.

    Make axes of 3D plot have equal scale so that spheres appear as
    spheres and cubes as cubes.  Required since `ax.axis('equal')`
    and `ax.set_aspect('equal')` don't work on 3D.
    """
    limits = np.array([
        ax.get_xlim3d(),
        ax.get_ylim3d(),
        ax.get_zlim3d(),
    ])
    origin = np.mean(limits, axis=1)
    radius = 0.5 * np.max(np.abs(limits[:, 1] - limits[:, 0]))
    _set_axes_radius(ax, origin, radius)

def _set_axes_radius(ax, origin, radius):
    x, y, z = origin
    ax.set_xlim3d([x - radius, x + radius])
    ax.set_ylim3d([y - radius, y + radius])
    ax.set_zlim3d([z - radius, z + radius])

def DrawGnssPoses(csv):
  gnss_poses = np.loadtxt(csv, delimiter=",", skiprows=1)
  mpl.rcParams['legend.fontsize'] = 10
  fig = plt.figure()
  ax = fig.add_subplot(projection='3d')

  x = gnss_poses[:, 1]
  y = gnss_poses[:, 2]
  z = gnss_poses[:, 3]

  ax.set_xlabel('tran_x')
  ax.set_ylabel('tran_y')
  ax.set_zlabel('tran_z')

  # ax1 = fig.add_subplot(projection='3d')
  ax.plot(x, y, label='Ground slide track projection')
  ax.plot(x, y, z, 'g-', label='3D trajectory')

  ax.set_box_aspect([1,1,1])
  set_axes_equal(ax)

  ax.legend()
  plt.show()

if __name__=='__main__':
  csv = "/home/yuxuanhuang/DataSet/4Seasons/2020-12-22_12-04-35/GNSSPoses.txt"
  DrawGnssPoses(csv)