import easyocr
import cv2

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary_image

def ocr_image(image_path):
    # 图像预处理
    processed_image = preprocess_image(image_path)

    reader = easyocr.Reader(['ch_sim','en'], gpu=True) # this needs to run only once to load the model into memory
    result = reader.readtext(processed_image, detail=0)
    print(result)
    for index, i in enumerate(result):
        result = filter_text(i)
        print(f"第{index+1}行内容为： {result}\n")
    # long_text = ' '.join(result)
    # print(long_text)
    # if filter_text(long_text):
    #     print(long_text)


def filter_text(text):
#     如果text中有包含特殊字符，则去掉字符串中的特殊字符
    if text:
        if any(char in text for char in '!@#$%^&*()_+{}|:"<>?[];\',./`~'):
            text = ''.join(char for char in text if char not in '!@#$%^&*()_+{}|:"<>?[];\',./`~')
            return text
        else:
            return text


if __name__ == '__main__':
    ocr_image('jingqu.png')