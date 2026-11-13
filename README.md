# Orchestra Atlas — 管弦樂配器知識庫

這是以 **AGENTS.md 驅動擴充**的靜態互動網站，將管弦樂樂器知識與配器技巧整理成可搜尋、可分類、可互相連結的條目。主題結合音樂編曲與 AI 專案管理，重點不只是一次性完成網頁，而是讓不同的 AI 在閱讀 `AGENTS.md` 後，都能依相同規則繼續新增內容。

## 已有功能

- 首頁介紹與隨資料變動的條目統計
- 弦樂、木管、銅管、配器技巧的分類篩選
- 中文／英文名稱、摘要與標籤的即時搜尋
- 點擊卡片查看完整詳情、跨條目延伸閱讀
- RWD 手機介面、鍵盤可用的原生對話框
- `content/entries.json` 結構化內容與 Python 驗證腳本
- 初始六筆內容：小提琴、大提琴、長笛、法國號、旋律加倍、聲部進行

## 本機瀏覽

因瀏覽器對 `file://` 的 fetch 限制，不要直接用檔案總管雙擊 `index.html`；在專案根目錄開終端機執行：

```bash
python3 scripts/validate.py
python3 -m http.server 8000
```

再開啟 <http://localhost:8000>。按 `Ctrl+C` 停止伺服器。無需 Node.js、套件安裝或 API key。

## 新增內容：標準範例

1. 讓 AI 先讀 `AGENTS.md`。
2. 參考 `examples/new-entry-example.json`，在 `content/entries.json` 的 JSON array 加入一個物件。
3. 執行 `python3 scripts/validate.py`，確認 PASS。
4. 重新整理網站；新條目會自動出現在首頁卡片、統計數字與搜尋結果。

**示範交辦：**「請先讀 AGENTS.md，新增雙簧管條目，遵循既有欄位、分類和風格，完成後驗證並回報。」

## 專案結構

```text
AGENTS.md                     AI 開發規範
README.md                     專案說明
index.html                    首頁
assets/style.css              全站視覺與 RWD
assets/app.js                 資料載入與互動
content/entries.json          單一內容資料來源
scripts/validate.py           資料驗證
examples/new-entry-example.json 新條目範例（不會自動載入）
```

## GitHub Pages 發布

1. 在 GitHub 建立一個 **Public** repository，例如 `orchestra-atlas`。
2. 將此資料夾內的**所有檔案**上傳至 repository 根目錄，包括 `AGENTS.md` 和 `content/entries.json`（不要再包一層同名資料夾）。
3. 到 repository 的 **Settings → Pages → Build and deployment**，選擇 **Deploy from a branch**，Branch 選 `main`、Folder 選 `/(root)`，儲存。
4. 發布成功後，可使用 `https://<你的帳號>.github.io/orchestra-atlas/` 訪問，實際網址以 GitHub Pages 顯示為準。
5. 開啟公開網站，檢查搜尋、篩選、卡片詳情正常運作，再繳交 Repository 與 Pages 網址。

也可以在專案根目錄透過 Git CLI 上傳：

```bash
git init
git add .
git commit -m "Initial Orchestra Atlas"
git branch -M main
git remote add origin https://github.com/<你的帳號>/orchestra-atlas.git
git push -u origin main
```

建立遠端 repo 與 GitHub 認證需由你在自己的 GitHub 帳號完成。

## 作業重點

這個專案將 AI 的工作流程寫入版本控制：每次 AI 都先讀規則，對資料做小幅修改，再以相同的驗收程序確認結果。新的知識條目不需要複製 HTML/CSS，展示了清楚的可重複使用性與延伸性。

## 內容說明

示範知識為入門教學性摘要，音域與技術限制採概略描述；正式用於配器或演奏時，應另外查閱專門配器教材、樂器演奏資料及個別樂手能力。本文內容不是樂器性能的絕對保證。
# orchestral-atlas
