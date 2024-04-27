# policy_analysis

#### 项目表述

- 京津政策分析

#### 项目文件
```
policy_analysis
├─data
│  └─txt // 政策文件，自己下
├─paper // 论文pdf转doc
│  ├─doc // doc论文
│  └─pdf // pdf论文
├─result //共现语义图
├─stopwords // 停用词列表
└─util //mysql工具类
```
代码就自己看吧，有注释

### 运行
```
conda create -n policy python=3.10.14
conda activate policy
pip install -r requirements.txt
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

### 结果图

- 一致性得分原图
![政策主题一致性得分_raw.png](policy_score.png)
- 一致性得分处理图
![政策主题一致性得分.png](policy_score_raw.png)
- 共现语义图原图
![semantic_graph.png](result/semantic_graph.png)
- 共现语义图处理图  
 ![top_100_semantic_graph.png](result/top_100_semantic_graph.png)

### 联系方式(有偿咨询)
- QQ:284190056
- Wechat：AirEliauk9527