---
title: Markitdown
emoji: 👁
colorFrom: yellow
colorTo: purple
sdk: gradio
sdk_version: 5.25.0
app_file: app.py
pinned: false
short_description: 微軟markitdown / markdonw 功能
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference



# 將 MarkItDown 變身為 API：超級進化！

想讓 MarkItDown 更加靈活？把它部署成 API 吧！這樣你就可以在 Zapier、n8n 等自動化流程中輕鬆使用它，也可以直接用 UI 上傳檔案轉 Markdown。

## 本專案支援兩種啟動方式：

- `FastAPI` 提供 API 端點（如 `/convert`）
- `Gradio` 提供使用者介面可直接上傳檔案

---

## 🔧 安裝依賴套件

```bash
pip install -r requirements.txt
```


⸻

🚀 啟動方式

啟動 FastAPI API（背景服務）

```
bash uvicorn_start.sh
```
➡ 這會啟動在 http://localhost:8000，提供 /convert 上傳介面。

⸻

啟動 Gradio UI（上傳介面）
```
bash gradio_start.sh
```
➡ 開啟 http://127.0.0.1:7860，左側上傳檔案，右側會顯示 Markdown 結果。

⸻

📤 API 使用範例（JavaScript）
```
const formData = new FormData();
formData.append('file', file);

const response = await fetch('http://localhost:8000/convert', {
  method: 'POST',
  body: formData,
});
```


⸻

MarkItDown as an API: Supercharged Evolution!

Want to make MarkItDown more flexible? Turn it into an API! This way, you can easily use it in workflows like Zapier or n8n, or interact with it via a simple web UI.

Two modes in this project:
	•	FastAPI: provides an API endpoint like /convert
	•	Gradio: provides a user-friendly file upload UI

⸻

🔧 Install dependencies
```
pip install -r requirements.txt
```


⸻

🚀 How to Run

Run FastAPI backend (API only)

bash uvicorn_start.sh

➡ This launches the API server at http://localhost:8000.

⸻

Run Gradio frontend (UI)
```
bash gradio_start.sh
```
➡ This opens http://127.0.0.1:7860 with an interactive file upload interface.

⸻

📤 API Example (JavaScript)
```
const formData = new FormData();
formData.append('file', file);

const response = await fetch('http://localhost:8000/convert', {
  method: 'POST',
  body: formData,
});
```