import os
import pickle
import re

import jieba
import networkx as nx
import pandas as pd

# 停用词文件夹路径
stopwords_path = 'stopwords'
# txt文件夹路径
txt_folder = 'txt/test'
# 初始化停用词集合
stopwords = set()

# 遍历停用词文件夹下的所有txt文件
for filename in os.listdir(stopwords_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(stopwords_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            stopwords.update(file.read().split())


def get_text(func=1):
    text = ''
    if func == 2:
        # 遍历文件夹下所有的txt文件并读取内容
        for single_file in os.listdir(txt_folder):
            if single_file.endswith('.txt'):
                file_path = os.path.join(txt_folder, single_file)
                with open(file_path, 'r', encoding='utf-8') as txt_file:
                    file_text = txt_file.read()
                    text += file_text  # 将文件内容追加到字符串中
    else:
        txt_files = [os.path.join(txt_folder, file) for file in os.listdir(txt_folder) if file.endswith('.txt')]
        # 使用列表推导将文件名连接成一个字符串
        text = ', '.join(txt_files)
    return text


# 定义一个正则表达式模式，用于匹配包含中文字符且长度在1到4之间的词语
chinese_pattern = re.compile(r'[\u4e00-\u9fa5]{2,4}')
text = get_text(2)
# 使用jieba分词并筛选出满足条件的词语
words = [word for word in jieba.cut(text) if chinese_pattern.search(word) and word not in stopwords]

# 获取列表 words 的总长度
total_words = len(words)
# 创建一个共现语义网络图
G = nx.Graph()
for i, word1 in enumerate(words):
    for j, word2 in enumerate(words):
        if i != j:
            G.add_edge(word1, word2)
            print(f"当前进度: {i}/{total_words},{j}/{total_words}")

# 在循环处理文本之后，将实际的单词列表赋给 words 变量
words = [word for word in jieba.cut(text) if word not in stopwords]

# 创建一个 Pandas Series 来统计词频
word_freq = pd.Series(words).value_counts()

# 检查文件是否存在
file_path = 'data/word_freq.csv'
if os.path.exists(file_path):
    os.remove(file_path)
word_freq.to_csv(file_path, encoding='utf-8-sig', index=False)
# 将词频数据和词语写入 CSV 文件
word_freq.reset_index().rename(columns={'index': 'word', 0: 'frequency'}).to_csv(file_path, encoding='utf-8-sig',
                                                                                 index=False)

# 保存网络图到文件
with open('data/network_graph.pkl', 'wb') as file:
    pickle.dump(G, file)
