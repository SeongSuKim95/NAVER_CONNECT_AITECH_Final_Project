from fastapi import FastAPI, Request
import uvicorn
import requests

import re
req = requests.get("http://ipconfig.kr")
server_ip = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

cartoonize_url = "http://115.85.182.51:30003"
track_url = "http://115.85.182.51:30004"

# FastAPI 객체 생성
app = FastAPI()
# 라우터 '/'로 접근 시 {Hello: World}를 json 형태로 반환
@app.post("/save_video")
async def read_root(req: Request):
    data = await req.body()
    file = open("database/uploaded_video/video.mp4", "wb")
    file.write(data)
    file.close()
    
    requests.get(f"{cartoonize_url}/cartoonize")
    requests.get(f"{track_url}/track")
    
    return 200

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=30002, reload=True, access_log=False)
