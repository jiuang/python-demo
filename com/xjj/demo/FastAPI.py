from fastapi import FastAPI, File, UploadFile
import uvicorn
import nest_asyncio
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

preset = "fast"

# @app.get("/fastapi")
# def lip_sync(text: str):
#     print("接收到参数：" + text)

# @app.post("/fastapi")
# def lip_sync(audio: UploadFile):
#     print("接收到参数……")
#     with open("audio22222.wav", "wb") as audio_file:
#         audio_file.write(audio.read())

@app.post("/fastapi")
async def file_upload(file: bytes = File(..., max_length=2097152)):
    """使用File类，文件内容会以bytes的形式读入内存，适合小上传文件"""
    with open("D:\\audio.wav", "wb") as f:
        f.write(file)
    f.close()
    return {"file_size": len(file)}

if __name__ == "__main__":
    PORT = 17860
    nest_asyncio.apply()
    uvicorn.run(app, host="0.0.0.0", port=PORT)
