# -*- coding: utf-8 -*

"""

    maze.maze
    ~~~~~~~~~

    stamaimer 06/28/17

"""


import argparse
from collections import namedtuple

import numpy as np


class Node:

    maze_size = 0

    def __init__(self, index, parent):

        self.index = index

        self.parent = parent

        if self.parent:

            if self.index[0] == self.parent.index[0] or self.index[1] == self.parent.index[1]:

                self.g_value = 10

            else:

                self.g_value = 14

        else:

            self.g_value = 0

        self.h_value = 2 * (self.maze_size - 1) - index[0] - index[1]

        self.f_value = self.g_value + self.h_value

    def __repr__(self):

        return "Index: %r\tParent: %r\tGValue: %r\tHValue: %r\tFValue: %r" % (self.index, self.parent.index if self.parent else "None",
                                                                              self.g_value, self.h_value, self.f_value)


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

        np.savetxt(filename, maze, fmt="%i")

    except Exception as e:

        print e.message

    else:

        print filename

    return maze, maze_size


def get_surrounded_index(node, maze, maze_size):

    row, col = node.index

    index = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
             (row, col - 1),                     (row, col + 1),
             (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]

    valid_index = [item for item in index if item[0] != -1 and item[0] != maze_size and
                                             item[1] != -1 and item[1] != maze_size and
                                             maze[item[0]][item[1]] != 1]

    return valid_index


def astar(maze, maze_size):

    Node.maze_size = maze_size

    open_list = []

    close_list = []

    current_node = Node((0, 0), 0)

    open_list.append(current_node)

    while open_list:

        open_list.sort(key=lambda node: node.f_value)

        if open_list[0].index == (maze_size - 1, maze_size - 1):

            pass

        open_list.remove(current_node)

        close_list.append(current_node)



    open_list.extend([Node(index, current_node) for index in get_surrounded_index(current_node, maze, maze_size)])


if __name__ == "__main__":

    astar(*generate_maze(10, 0.4))
