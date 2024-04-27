import os
import shutil


def filter_key():
    # 源文件夹路径
    source_folder = 'txt'
    # 目标文件夹路径
    destination_folder = 'txt/filtered'
    # 创建目标文件夹（如果不存在）
    os.makedirs(destination_folder, exist_ok=True)

    def move_files_with_keyword(source_folder, destination_folder, keyword):
        for root, dirs, files in os.walk(source_folder):
            for filename in files:
                if filename.endswith('.txt'):
                    file_path = os.path.join(root, filename)

                    # 读取文件内容
                    with open(file_path, 'r', encoding='utf-8') as file:
                        file_content = file.read()

                    # 检查文件内容是否包含关键词
                    if keyword in file_content:
                        # 获取相对路径，并构建目标路径
                        relative_path = os.path.relpath(file_path, source_folder)
                        destination_path = os.path.join(destination_folder, relative_path)

                        # 创建目标文件夹路径
                        os.makedirs(os.path.dirname(destination_path), exist_ok=True)

                        # 移动文件到目标文件夹
                        shutil.move(file_path, destination_path)
                        print(f'Moved {filename} to {destination_folder}')

    move_files_with_keyword(source_folder, destination_folder, '科技创新')
    print('File filtering completed.')


def filter_city():
    import os
    import shutil

    # 源文件夹路径
    src_folder = 'txt/test'

    # 目标文件夹路径
    dst_folder = 'txt/city/beijing'

    # 遍历源文件夹下的所有文件
    for filename in os.listdir(src_folder):
        if "北京" in filename:  # 判断文件名中是否含有"北京"
            src_file = os.path.join(src_folder, filename)  # 源文件路径
            dst_file = os.path.join(dst_folder, filename)  # 目标文件路径

            # 使用shutil模块移动文件
            shutil.move(src_file, dst_file)

    print("文件移动完成")


if __name__ == '__main__':
    # filter_key()
    filter_city()
