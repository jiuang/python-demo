from com.xjj.demo import File
import speech_recognition as sr
import requests

# from speech_recognition import whisper
from pydub import AudioSegment
import datetime

# 创建Recognizer对象
r = sr.Recognizer()

# 打开默认的麦克风进行录制
with sr.Microphone() as source:
    print("正在等待语音输入...")

    # r.adjust_for_ambient_noise(source)  # 调整麦克风的环境噪声

    while True:
        # current_time = datetime.datetime.now()
        # print("1: " + str(current_time))
        audio = r.listen(source)    # 从麦克风中获取音频数据
        # print("2: " + str(datetime.datetime.now() - current_time))
        print("已监听到语音输入，正在识别……")


        # 使用Google语音识别引擎将语音转换为文本
        try:
            text = r.recognize_google(audio, language='zh-CN') # 需要翻墙
            # text = r.recognize_whisper(audio, model="small", language="english")
            print("识别到语音文本：" + text)

            # File.removeFile("audio.wav")


            # with open("audio.wav", "wb") as audio_file:
            #     audio_file.write(audio.get_wav_data())
                # audio_file.close()
            # 发起GET请求，接口在com/xjj/demo/FastAPI.py文件中
            base_url = "http://192.168.11.182:8998/api/digital/talking/"
            url_with_params = f"{base_url}?text={text}"
            response = requests.get(url_with_params)

            # 发起POST请求，音频bytes
            # base_url = "http://192.168.11.182:8998/api/digital/talking/"
            # files = {'audio': audio.get_wav_data()}  # 将文件打开并作为字典的值传入
            # response = requests.post(base_url, files=files)


        except sr.UnknownValueError:
            print("无法识别语音……")
        except sr.RequestError as e:
            print("请求错误：", str(e))
