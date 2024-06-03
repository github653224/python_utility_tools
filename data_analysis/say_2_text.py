import speech_recognition as sr


def say_2_text_via_wav(audio_file):
    r = sr.Recognizer()
    audio_file = 'my_baby.wav'
    with sr.AudioFile(audio_file) as source:
       audio = r.record(source)
    try:
       print("文本内容：",r.recognize_sphinx(audio))
       #默认会识别为英文，如果要识别中文，需要下载普通话识别文件
    except Exception as e:
       print(e)




import whisper
class WhisperTranscriber(object):
    def __init__(self, model_name):
        self.model = whisper.load_model(model_name)
    def whisper_transcribe(self, audio_path):
        audio = self.model.transcribe(audio_path, fp16=False)
# language 参数省略，默认即为英语
        return audio['text']


if __name__ == '__main__':
    # transcriber = WhisperTranscriber("base")
    # text = transcriber.whisper_transcribe("my_baby.mp3")
    # print(text)

    audio_file = 'my_baby.wav'
    say_2_text_via_wav(audio_file)