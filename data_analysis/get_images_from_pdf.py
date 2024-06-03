
import fitz # PyMuPDF
# 设置 PDF 文件路径
file = "ali.pdf"
# 打开 PDF 文件
pdf_file = fitz.open(file)
# 遍历 PDF 页面
for page_index in range(len(pdf_file)):
    # 获取 PDF 页面
    page = pdf_file[page_index]
    # 获取页面上所有图像
    image_list = page.get_images()
    # 输出此页面中找到的图像数量
    if image_list:
        print(f"[+] 在页面：{page_index}，总共发现 {len(image_list)} 张图片。")
    else:
        print(f"[+] 在页面：{page_index}，没有发现图片。")
    for image_index, img in enumerate(page.get_images(), start=1):

        # 获取图像的XREF编号和图像数据
        xref = img[0]
        pix = fitz.Pixmap(pdf_file, xref)
        # 保存图像
        if str(fitz.csRGB) == str(pix.colorspace):
            img_path = f'./imgs/image{page_index+1}_{xref}.png'
            pix.save(img_path)
print(f"[+] 已保存所有图片。")