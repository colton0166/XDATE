# 國曆轉農曆查詢系統

這是一個簡單的網頁應用程式，可以將國曆（西曆）日期轉換為農曆日期。

## 功能特色

- 直觀的日期選擇介面
- 即時轉換國曆至農曆
- 顯示農曆年、月、日
- 顯示生肖
- 支援閏月顯示

## 安裝說明

1. 確保您已安裝 Python 3.7 或更新版本

2. 安裝所需套件：
```bash
pip install -r requirements.txt
```

3. 執行應用程式：
```bash
python app.py
```

4. 開啟瀏覽器，訪問：
```
http://localhost:5000
```

## 使用方法

1. 在日期選擇器中選擇想要轉換的國曆日期
2. 點擊「轉換」按鈕
3. 系統將顯示對應的農曆日期資訊

## 技術架構

- 後端：Python Flask
- 前端：HTML, JavaScript, Tailwind CSS
- 日期轉換：lunarcalendar 套件 
---

## Render 部署說明

1. 將此專案上傳至 GitHub
2. Render 建立新的 Web Service，選取此 Repo
3. 設定 Start Command 為：
```
gunicorn wsgi:app
```
4. 將 JSON 資料檔也上傳進 repo（例如放在根目錄）
