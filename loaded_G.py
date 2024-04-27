import pickle

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

# 加载网络图
with open('data/network_graph.pkl', 'rb') as file:
    loaded_G = pickle.load(file)

# 获取前 20 个词频最高的关键词
# 从 CSV 文件中读取数据
word_freq = pd.read_csv('data/word_freq.csv', encoding='utf-8').set_index('word')['count']
# 将数据转换为 Pandas Series
top_keywords = word_freq.head(100).index.tolist()  # 转换为列表

# 创建一个子图，仅包含前 20 个关键词及其边
subgraph = loaded_G.subgraph(top_keywords)

# 绘制共现语义网络图
# pos = nx.circular_layout(subgraph)

pos = nx.fruchterman_reingold_layout(subgraph, dim=2, k=1, pos=None, fixed=None, iterations=500, weight='weight',
                                     scale=20.0)
# pos = nx.spring_layout(subgraph, ddim=2, k=None, pos=None, fixed=None, iterations=50, weight='weight', scale=1.0)

# 设置节点的大小和透明度
node_size = 0
edge_alpha = 0.2

# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 调整图像大小
plt.figure(figsize=(9, 9))
# 调整节点标签的位置，让它显示在节点的下方
label_pos = {node: (x, y - 0.02) for node, (x, y) in pos.items()}
# 绘制网络图，将节点标签显示在节点的下方
nx.draw(subgraph, pos, with_labels=False, node_color='none', node_size=0, edge_color='gray', width=0.4,
        alpha=0.28, style='solid')
nx.draw_networkx_labels(subgraph, label_pos, font_color='black', font_size=15)

# 显示图形
plt.savefig('result/top_100_semantic_graph.png')
plt.show()
# 保存图形到文件
