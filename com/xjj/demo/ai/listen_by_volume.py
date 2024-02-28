import pyaudio
import numpy as np
from math import log10

# 设置参数
CHUNK = 4096  # 每次录制的样本点数
FORMAT = pyaudio.paInt16  # 采集到的音频格式为16位有符号整型
CHANNELS = 2  # 双声道
RATE = 44100  # 采样率为44100Hz


def get_decibel(data):
    rms = np.sqrt((np.mean([x ** 2 for x in data]) / len(data)))
    decibel = 20 * (log10(rms) - log10(3))
    return round(decibel, 2)


p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
print("开始监听...")
while True:
    try:
        data = stream.read(CHUNK)
        volume = get_decibel(data)
        print("当前音量：{} dB".format(volume))

    except KeyboardInterrupt:
        break

stream.stop_stream()
stream.close()
p.terminate()