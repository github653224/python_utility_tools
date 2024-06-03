import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

# 假设的排名数据，每个列表代表一年的排名
rankings = [
    [2020, [1, 2, 3, 4, 5]],
    [2021, [2, 1, 3, 5, 4]],
    [2022, [3, 1, 2, 4, 5]],
    [2023, [4, 2, 1, 5, 3]],
    [2024, [5, 2, 3, 4, 1]]
]

# 设置语言名称
languages = ['语言1', '语言2', '语言3', '语言4', '语言5']

# 设置画布和轴
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 6)
ax.set_ylim(-0.5, 4.5)
ax.set_yticks(range(len(languages)))
ax.set_yticklabels(languages)

# 初始化条形图
bars = ax.barh(range(len(languages)), [0] * len(languages), color=[np.random.rand(3,) for _ in range(len(languages))])

# 定义更新函数
def update(frame):
    year, ranks = rankings[frame]
    ax.set_title(f'年份: {year}')
    for i, (bar, rank) in enumerate(zip(bars, ranks)):
        bar.set_width(5 - rank + 1)  # 宽度根据排名设置
        bar.set_y(rank - 1)  # y轴位置根据排名设置
    return bars

# 创建动画
ani = FuncAnimation(fig, update, frames=len(rankings), blit=False, interval=1500, repeat=False)

# 使用 FFMpegWriter 保存动画
writer = FFMpegWriter(fps=1, metadata=dict(artist='Me'), bitrate=1800)
ani.save('language_rankings.mp4', writer=writer)

# 显示图表
plt.tight_layout()
plt.show()
