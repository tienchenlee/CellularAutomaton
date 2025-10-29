#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 設定格子大小
N = 50

# 隨機初始化格子 (0 = 死亡, 1 = 活著)
grid = np.random.choice([0, 1], size=(N, N))

def update(frameNum, img, grid, N):
    # 建立新的格子狀態
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # 計算鄰居總數 (使用 modulo 繞邊界)
            total = (
                grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]
            )
            # Game of Life 規則
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 1
    # 更新格子
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# 建立動畫
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='binary')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N), frames=200, interval=100, save_count=50)

plt.show()
