# Emotional Portrait Portfolio

童年情绪肖像作品集 — 静态网站，通过 GitHub Pages 免费托管。

## 在线访问

部署完成后，网站地址为：

**https://cengxvnuo.github.io/Emotional-Portrait-Portfolio/**

（若仓库 Settings → Pages 使用其他分支或目录，请以 GitHub 显示的实际 URL 为准。）

## 本地预览

```bash
python scripts/prepare-deploy.py
# 然后用本地服务器打开 index.html，例如：
python -m http.server 8080
```

浏览器访问 http://localhost:8080

## 更新网站

1. 在本地修改 `code-edited.html` 并放入 `assets/image/` 素材  
2. 运行 `python scripts/prepare-deploy.py` 生成 `index.html`  
3. 提交并推送到 `main` 分支，GitHub Actions 会自动发布 Pages  
