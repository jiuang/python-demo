import pyaudio
import numpy as np
import wave

import requests
import com.xjj.demo.File as FileUtil

# 设置参数
CHUNK = 1024  # 每次读取的样本点数
FORMAT = pyaudio.paInt16  # 采集到的音频格式为16位有符号整型
CHANNELS = 1  # 单声道
RATE = 44100  # 采样率（Hz）
RECORD_SECONDS = 10  # 录制时长最长为10秒

# 打开流进行录制
while True:
    p = pyaudio.PyAudio()  # 创建PyAudio对象
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    # print("正在录制...")
    frames = []
    valid_voice_num = 0
    continue_low_num = 0
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        f = np.frombuffer(data, dtype=np.int16)
        volume = abs(f).mean() / CHUNK * RATE
        # print(volume)
        if volume >= 1000:
            frames.append(data)
            valid_voice_num += 1
            continue_low_num = 0
        if volume < 1000:
            continue_low_num += 1
            if continue_low_num > 10:
                break

    if valid_voice_num > 5:
        print("录制完成……")
        FileUtil.removeFile("audio.wav")
        wf = wave.open("audio.wav", 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        # 发起POST请求，音频bytes
        base_url = "http://192.168.11.182:8998/api/digital/talking/"
        # 将文件打开并作为字典的值传入
        with open("audio.wav", "rb") as audio_file:
            files = {'audio': audio_file.read()}
            response = requests.post(base_url, files=files)
            response.close()

    stream.stop_stream()  # 停止输入流
    stream.close()  # 关闭输入流
    p.terminate()  # 结束PyAudio会话
