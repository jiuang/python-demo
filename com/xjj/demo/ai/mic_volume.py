import pyaudio
import numpy as np

def checkMicVolume():
    # 设置参数
    CHUNK = 1024  # 每次读取的样本点数
    FORMAT = pyaudio.paInt16  # 采集到的音频格式为16位有符号整型
    CHANNELS = 1  # 单声道
    RATE = 44100  # 采样率（Hz）
    RECORD_SECONDS = 5  # 录制时长为5秒

    p = pyaudio.PyAudio()  # 创建PyAudio对象
    # 打开流进行录制
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("正在录制...")
    n = 0
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        f = np.frombuffer(data, dtype=np.int16)
        volume = abs(f).mean() / CHUNK * RATE
        if volume < 200000:
            n += 1
            if n > 5:
                break
    print("录制完成！")

    with open("audio.wav", "wb") as audio_file:
        audio_file.write(stream)
    audio_file.close()

    stream.stop_stream()  # 停止输入流
    stream.close()  # 关闭输入流
    p.terminate()  # 结束PyAudio会话

    # 计算平均音量值
    # volume = sum([abs(frame).mean() for frame in frames]) / CHUNK * RATE
    # print("当前麦克风音量大小：", volume)
    # return volume >= 200000

# 29423835
# 19189736
# 16899006
# 2526923

if __name__ == '__main__':
    checkMicVolume()
