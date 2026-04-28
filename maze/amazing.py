#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   amazing.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/20 11:35:57 by andry-ha            #+#    #+#            #
#   Updated: 2026/04/20 11:37:43 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random


def generate_maze(width=21, height=21):
    # Create a grid of walls (1 = wall, 0 = path)
    maze = [[1 for _ in range(width)] for _ in range(height)]

    def walk(x, y):
        maze[y][x] = 0  # Mark current cell as path

        # Define directions: North, South, East, West (move 2 steps to skip walls)
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check if neighbor is within bounds and not yet visited
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                # Remove wall between current cell and neighbor
                maze[y + dy // 2][x + dx // 2] = 0
                walk(nx, ny)

    walk(1, 1)  # Start carving from (1, 1)
    return maze


def print_maze(maze):
    for row in maze:
        # Use '#' for walls and ' ' for paths
        print("".join('#' if cell == 1 else ' ' for cell in row))


my_maze = generate_maze(25, 15)
print_maze(my_maze)
