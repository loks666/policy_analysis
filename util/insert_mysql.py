import os

import mysql.connector

# MySQL数据库连接配置
db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Lx284190056",
    "database": "tju",
}

# 文件夹路径
folder_path = "../txt/raw/京津协同政策集"

# 连接到MySQL数据库
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# 检查表是否存在，如果存在则删除
table_name = "policy_file"
cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
if cursor.fetchone():
    cursor.execute(f"DROP TABLE {table_name}")

# 创建表
create_table_sql = """
CREATE TABLE `policy_file` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `name` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '文件名',
  `content` longtext COLLATE utf8mb4_bin,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
"""
cursor.execute(create_table_sql)

# 遍历文件夹并插入文本文件内容
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
            content = file.read()
            name = os.path.splitext(filename)[0]  # 使用文件名作为数据库记录的文件名
            # 插入数据，不指定id
            sql = "INSERT INTO policy_file (name, content) VALUES (%s, %s)"
            values = (name, content)
            cursor.execute(sql, values)
            connection.commit()

# 关闭数据库连接
cursor.close()
connection.close()
