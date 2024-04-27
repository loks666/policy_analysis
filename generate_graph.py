import csv

import matplotlib.pyplot as plt

# 读取 CSV 文件中的数据
x = []  # 存储主题数量
y = []  # 存储一致性得分

with open('graph.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # 跳过标题行
    line_count = 0  # 添加行计数器
    for row in reader:
        # 判断行计数器的值，如果是偶数行（行计数从0开始），则读取数据
        if line_count % 2 == 0:
            num_topics, coherence_score = map(float, row)  # 假设CSV文件中的数据是浮点数
            x.append(num_topics)
            y.append(coherence_score)
        line_count += 1

# 绘制折线图
plt.plot(x, y, color='black', linestyle='solid')
plt.xlabel('主题数量')
plt.ylabel('一致性得分')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('政策主题一致性得分')
plt.savefig('policy_score.png')
plt.show()
