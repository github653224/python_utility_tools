import easyocr
import pyttsx3 as pyttsx

def text_2_say(text_content):
    engine = pyttsx.init()
    engine.say(text_content)
    engine.runAndWait()
def ocr_image(image_path):
    reader = easyocr.Reader(['ch_sim','en'], gpu=True) # this needs to run only once to load the model into memory
    # reader = easyocr.Reader(['ch_sim','en', 'ch_tra'], gpu=True, download_enabled=True) # this needs to run only once to load the model into memory
    # reader = easyocr.Reader(['en', 'ch_tra'], gpu=True, download_enabled=True) # this needs to run only once to load the model into memory
    result = reader.readtext(image_path, detail=0)
    long_text = ' '.join(result)
    print(long_text)
    if filter_text(long_text):
        # print(long_text)
        text_2_say(long_text)


# 编写函数来排除 特殊符号，繁体字，只保留中文和英文和数字,在朗读时候，把排除的符号替换成空格，返回true或false
def filter_text(text):
    if text.isalpha() or text.isdigit() or text.isalnum():
        return True
    else:
        return False




if __name__ == '__main__':
    ocr_image('fapiao.jpeg')