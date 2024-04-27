import os
import sys

import pandas as pd

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

print()
# 读取Excel文件
excel_file = '京津协同政策集.xlsx'
df = pd.read_excel(excel_file)

# 用于存储处理后的文件名
processed_links = []

# 遍历txt文件夹及其子文件夹中的所有txt文件
for root, dirs, files in os.walk('txt'):
    for file in files:
        if file.endswith('.txt'):
            file_path = os.path.join(root, file)

            # 读取txt文件内容
            with open(file_path, 'r', encoding='utf-8') as txt_file:
                content = txt_file.read()

                # 截取‘原文链接：’后到.html中间的字符
                start_index = content.find('原文链接：') + len('原文链接：')
                end_index = content.find('.html', start_index)

                if start_index != -1 and end_index != -1:
                    extracted_link = content[start_index:end_index + len('.html')]
                    processed_links.append(extracted_link)

# 去重处理
processed_links_set = set(processed_links)
print(f'文件数量: {len(processed_links_set)}')

# 匹配Excel中的第二列字符
matching_rows = []
added_links = set()  # 用于跟踪已添加的链接

for index, row in df.iterrows():
    link = str(row.iloc[10])
    if link in processed_links_set and link not in added_links:
        matching_rows.append(row)
        added_links.add(link)  # 将已添加的链接记入集合

print(f'匹配到的结果数: {len(matching_rows)}')

# 将匹配到的结果转换为DataFrame
matching_df = pd.DataFrame(matching_rows)
# 保持原有的列名
matching_df.columns = pd.read_excel('京津协同政策集.xlsx', header=2).columns

# 保存为新的Excel文件
new_excel_file = 'new_京津协同政策集.xlsx'
matching_df.to_excel(new_excel_file, index=False)

print(f"匹配完成，结果已保存到 {new_excel_file}")
