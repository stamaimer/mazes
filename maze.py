# -*- coding: utf-8 -*

"""

    maze.maze
    ~~~~~~~~~

    stamaimer 06/28/17

"""


import argparse
from collections import namedtuple

import numpy as np


# class Node:
#
#     def __init__(self, value, parent, coordinate):
#
#         self.value = value
#
#         self.parent = parent
#
#         self.coordinate = coordinate


Node = namedtuple("Node", ["value", "parent", "coordinate"])


def generate_maze(maze_size, wall_rate):

    """

    随机生成一个正方形的迷宫，存储到文本文件中。

    迷宫起点：(0, 0)
    迷宫终点：(maze_size - 1, maze_size - 1)

    道路：0
    围墙：1

    :param maze_size: 迷宫大小
    :param wall_rate: 迷宫中围墙所占比例
    :return: None

    """

    maze = np.random.choice([0, 1], size=maze_size**2, p=[1 - wall_rate, wall_rate]).reshape(maze_size, maze_size)

    maze[0][0] = 0

    maze[maze_size - 1][maze_size - 1] = 0

    filename = "mazes/{}.txt".format(maze_size + wall_rate)

    try:

        np.savetxt(filename, fmt="%i")

    except Exception as e:

        print e.message

    else:

        print filename


if __name__ == "__main__":

    pass
