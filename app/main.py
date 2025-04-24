import shutil
from markitdown import MarkItDown
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4

md = MarkItDown()
app = FastAPI(
    title="MarkItDown API",
    description="API 用於將 Markdown 文件轉換為其他格式",
    version="1.0.0",
)

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允許所有來源，生產環境中應該限制為特定域名
    allow_credentials=True,
    allow_methods=["*"],  # 允許所有方法
    allow_headers=["*"],  # 允許所有標頭
)

from pydantic import BaseModel

class ConversionResponse(BaseModel):
    result: str

@app.post("/convert",
    response_model=ConversionResponse,
    summary="將 Markdown 文件轉換為純文本",
    description="上傳 Markdown 文件並將其轉換為純文本格式。"
)
async def convert_markdown(
    file: UploadFile
):
    """
    將上傳的 Markdown 文件轉換為純文本。
    
    - **file**: 要轉換的 Markdown 文件
    
    返回:
    - **result**: 轉換後的純文本內容
    """
    unique_id = uuid4()
    temp_dir = f"./temp/{unique_id}"

    shutil.os.makedirs(temp_dir, exist_ok=True)

    file_path = f"{temp_dir}/{file.filename}"
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    result = md.convert(file_path)
    content = result.text_content

    shutil.rmtree(temp_dir)
    return {"result": content}
