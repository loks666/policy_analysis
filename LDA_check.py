import os
import re

import jieba
import matplotlib.pyplot as plt
from gensim import corpora, models

# 1. 加载数据和停用词
txt_folder = 'txt/city/beijing'
stopwords_path = 'stopwords'

# 2. 数据预处理
text_data = []  # 存储所有文本数据
stopwords = set()

for filename in os.listdir(stopwords_path):
    if filename.endswith('.txt'):
        with open(os.path.join(stopwords_path, filename), 'r', encoding='utf-8') as file:
            stopwords.update(file.read().split())

for filename in os.listdir(txt_folder):
    if filename.endswith('.txt'):
        with open(os.path.join(txt_folder, filename), 'r', encoding='utf-8') as file:
            text = file.read()
            text_data.append(text)

# 3. 使用 Jieba 分词
corpus = []  # 存储分词后的文本
for text in text_data:
    chinese_pattern = re.compile(r'[\u4e00-\u9fa5]{2,4}')
    words = [word for word in jieba.cut(text) if chinese_pattern.search(word) and word not in stopwords]
    corpus.append(words)
# 4. 使用 LDA 模型进行主题建模
dictionary = corpora.Dictionary(corpus)
corpus = [dictionary.doc2bow(text) for text in corpus]
lda_model = models.LdaModel(corpus, id2word=dictionary, num_topics=15)  # 5个主题，可以根据需要调整

# 5. 提取每个主题的主要词汇
topic_keywords = []
for i in range(lda_model.num_topics):
    print(lda_model.show_topic(i))
    topic_words = lda_model.show_topic(i, topn=1)  # 获取主题的第一个主要词汇
    if topic_words:  # 检查是否找到了主题词汇
        keyword = topic_words[0][0]  # 取第一个词汇
        # 使用正则表达式去除非字母和数字的字符
        topic_keywords.append(keyword)
    else:
        print(f"No keywords found for Topic {i + 1}")

# 输出信息
print(f"Number of topics: {lda_model.num_topics}")
print(f"Actual topic keywords: {topic_keywords}")

# 6. 提取主题分布
topic_distributions = []
for doc in corpus:
    topic_distribution = lda_model[doc]
    topic_distributions.append(topic_distribution)

# 7. 生成折线图
plt.figure(figsize=(10, 5))
for i, topic in enumerate(topic_distributions):
    topic_weights = [weight for _, weight in topic]
    if i < len(topic_keywords):  # 检查索引是否在范围内
        topic_label = f"{topic_keywords[i]}"  # 添加主题的第一个词汇到标签
        plt.plot(range(len(topic_weights)), topic_weights, label=topic_label, linewidth=2)  # 增加线条宽度
    else:
        print(f"No keyword for Topic {i + 1}")

# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.xlabel("主题数量")
plt.ylabel("一致性得分")
plt.title("政策主题一致性得分")
plt.legend()
plt.show()
