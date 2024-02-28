import speech_recognition as sr
import requests

import threading
import asyncio

# 创建Recognizer对象
r = sr.Recognizer()


def listen():
    # 打开默认的麦克风进行录制
    with sr.Microphone() as source:
        print("正在等待语音输入...")

        # r.adjust_for_ambient_noise(source)  # 调整麦克风的环境噪声

        while True:
            # 从麦克风中获取音频数据
            audio = r.listen(source)
            print("已监听到语音输入，正在识别……")
            # 开启线程，异步调用
            asyncio.run(start_thread(audio))


async def run_listen_request(audio):
    print("进入异步调用，发起http请求...")
    try:
        # 发起POST请求，音频bytes
        base_url = "http://192.168.11.182:8998/api/digital/talking/"
        # 将文件打开并作为字典的值传入
        files = {'audio': audio.get_wav_data()}
        response = requests.post(base_url, files=files)
        response.close()
    except sr.UnknownValueError:
        print("无法识别语音……")
    except sr.RequestError as e:
        print("请求错误：", str(e))


async def start_thread(audio):
    print("--------thread started...")
    thread = threading.Thread(target=lambda: asyncio.run(run_listen_request(audio)))
    thread.start()
    print("--------thread end...")


if __name__ == "__main__":
    listen()