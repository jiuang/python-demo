import requests

with open("ai/output.wav", "rb") as audio_file:
    audio_file.read()

    # 发起GET请求，接口在com/xjj/demo/FastAPI.py文件中
    #base_url = "http://127.0.0.1:17860/fastapi"
    base_url = "http://192.168.11.182:8998/api/digital/talking/"
    # url_with_params = f"{base_url}?text={text}"
    # response = requests.get(url_with_params)

    # 发起POST请求，传递文件
    file = {'audio': audio_file}  # 将文件打开并作为字典的值传入
    response = requests.post(base_url, files=file)
