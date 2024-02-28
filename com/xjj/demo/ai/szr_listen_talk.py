import speech_recognition as sr
import requests

# 创建Recognizer对象
r = sr.Recognizer()

# 打开默认的麦克风进行录制
with sr.Microphone() as source:
    print("正在等待语音输入...")

    # r.adjust_for_ambient_noise(source)  # 调整麦克风的环境噪声

    while True:
        audio = r.listen(source)    # 从麦克风中获取音频数据
        print("已监听到语音输入，正在识别……")

        try:
            # 发起POST请求，音频bytes
            base_url = "http://192.168.11.182:8998/api/digital/talking/"
            files = {'audio': audio.get_wav_data()}  # 将文件打开并作为字典的值传入
            response = requests.post(base_url, files=files, stream=True)
        except sr.UnknownValueError:
            print("无法识别语音……")
        except sr.RequestError as e:
            print("请求错误：", str(e))
