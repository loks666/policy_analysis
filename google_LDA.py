import csv
import os
import re

import gensim
import gensim.corpora as corpora
import jieba
import matplotlib
import matplotlib.pyplot as plt
from gensim.models import CoherenceModel

from util.Mysql import query


def main():
    global data_set, dictionary, corpus, Lda
    # 1. 加载数据和停用词
    stopwords_path = 'stopwords'
    # 2. 数据预处理
    text_data = []  # 存储所有文本数据
    stopwords = set()
    for filename in os.listdir(stopwords_path):
        if filename.endswith('.txt'):
            with open(os.path.join(stopwords_path, filename), 'r', encoding='utf-8') as file:
                stopwords.update(file.read().split())
    # 执行查询
    sql = "SELECT * FROM policy_file WHERE NAME NOT LIKE '%卫生健康%' AND NAME NOT LIKE '%园林%' AND NAME LIKE '%天津%' AND (LENGTH( `content`) - LENGTH(REPLACE ( `content`, '京津协同', '' ))) / LENGTH( '京津协同' ) > 0;"
    results = query(sql)
    # 处理查询结果
    data_set = []  # 存储分词后的文本
    for result in results:
        id, name, content = result
        chinese_pattern = re.compile(r'[\u4e00-\u9fa5]{2,4}')
        words = [word for word in jieba.cut(content) if chinese_pattern.search(word) and word not in stopwords]
        data_set.append(words)
    print(data_set)  # 输出所有分词列表
    dictionary = corpora.Dictionary(data_set)  # 构建 document-term matrix
    corpus = [dictionary.doc2bow(text) for text in data_set]
    Lda = gensim.models.ldamodel.LdaModel  # 创建LDA对象
    # 在函数之外初始化一个空列表以存储数据
    coherence_data = []

    def coherence(num_topics):
        lda_model = Lda(corpus, num_topics=num_topics, id2word=dictionary, passes=50)  # passes为迭代次数，次数越多越精准
        coherence_model_lda = CoherenceModel(model=lda_model, texts=data_set, dictionary=dictionary, coherence='c_v')
        coherence_lda = coherence_model_lda.get_coherence()
        print(f"第 {num_topics} 个模型一致性得分为: {coherence_lda}")
        coherence_data.append((num_topics, coherence_lda))
        return coherence_lda

    # 绘制折线图
    x = range(1, 41)  # 主题范围数量
    y = [coherence(i) for i in x]
    # 写入 CSV 文件
    with open('graph.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['主题数量', '一致性的得分'])  # 写入标题行
        writer.writerows(coherence_data)  # 写入数据行

    plt.plot(x, y, color='black', linestyle='solid')
    plt.xlabel('主题数量')
    plt.ylabel('一致性得分')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.title('政策主题一致性得分')
    plt.savefig('policy_score.png')
    plt.show()


if __name__ == '__main__':
    main()
