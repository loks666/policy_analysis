import os
import shutil

# 源文件夹路径
source_folder = 'txt/京津协同政策集'

# 新目标文件夹路径
destination_folder = 'txt/focus'

# 创建目标文件夹（如果不存在）
os.makedirs(destination_folder, exist_ok=True)


def move_files_with_keyword(source_folder, destination_folder, keyword, chengjie, shujie):
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            if filename.endswith('.txt'):
                file_path = os.path.join(root, filename)
                print(filename)

                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()

                # 检查文件内容是否包含关键词
                a1 = keyword in file_content
                a2 = chengjie in file_content or shujie in file_content
                a3 = file_content.count("京津协同") > 1

                if a1 and (a2 or a3):
                    # 获取相对路径，并构建目标路径
                    relative_path = os.path.relpath(file_path, source_folder)
                    destination_path = os.path.join(destination_folder, relative_path)

                    # 创建目标文件夹路径
                    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

                    # 复制文件到新目标文件夹
                    shutil.copy(file_path, destination_path)


move_files_with_keyword(source_folder, destination_folder, '科技创新', '承接', '疏解')

print('File filtering completed.')
