import os

from pdf2docx import Converter


def convert_pdf_to_doc(pdf_path, doc_dir):
    # 获取PDF文件名（不包含扩展名）
    pdf_filename = os.path.splitext(os.path.basename(pdf_path))[0]

    # 构造输出的DOC文件路径
    doc_filename = f"{pdf_filename}.doc"
    doc_path = os.path.join(doc_dir, doc_filename)

    # 创建转换器对象
    cv = Converter(pdf_path)

    # 进行转换并保存为DOC文件
    cv.convert(doc_path, start=0, end=None)
    cv.close()

    print(f"转换完成：{pdf_path} -> {doc_path}")


# 输入的PDF文件夹路径
pdf_folder = r"D:\policy_analysis\paper\pdf"

# 输出的DOC文件夹路径
doc_folder = r"D:\policy_analysis\paper\doc"

# 遍历PDF文件夹中的所有PDF文件
for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, file)
        convert_pdf_to_doc(pdf_path, doc_folder)
