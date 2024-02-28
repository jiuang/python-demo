from paddlespeech.server.bin.paddlespeech_client import ASRClientExecutor

asrclient_executor = ASRClientExecutor()
res = asrclient_executor(
    input="./zh.wav",
    server_ip="192.168.11.182",
    port=8090,
    sample_rate=16000,
    lang="zh_cn",
    audio_format="wav")
print(res)