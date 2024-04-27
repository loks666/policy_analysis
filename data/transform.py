import os

from docx import Document


def convert_docx_to_txt(docx_path, txt_path):
    # 打开Word文档
    doc = Document(docx_path)

    # 创建一个TXT文件并打开以写入内容
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        # 遍历Word文档中的段落并写入TXT文件
        for paragraph in doc.paragraphs:
            txt_file.write(paragraph.text + '\n')


if __name__ == "__main__":
    # 指定Word文件夹路径和输出TXT文件夹路径
    word_folder_path = r"D:\A博\战略院\FOCUS SIX\doc"
    txt_folder_path = r"D:\A博\战略院\FOCUS SIX\txt"

    # 确保输出目录存在，如果不存在则创建
    os.makedirs(txt_folder_path, exist_ok=True)

    # 遍历Word文件夹中的所有文件
    for filename in os.listdir(word_folder_path):
        if filename.endswith(".docx") or filename.endswith(".doc"):
            # 构建Word和TXT文件的完整路径
            word_file_path = os.path.join(word_folder_path, filename)
            txt_file_path = os.path.join(txt_folder_path, os.path.splitext(filename)[0] + ".txt")

            # 调用函数进行转换
            convert_docx_to_txt(word_file_path, txt_file_path)

            print(f"Conversion complete for {filename}. Text saved to {txt_file_path}")
