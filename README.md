# Emotional Portrait Portfolio

童年情绪肖像作品集 — 静态网站，通过 GitHub Pages 免费托管。

## 在线访问

仓库已推送。请在 GitHub 开启 Pages（仅需一次）：

1. 打开 https://github.com/cengxvnuo/Emotional-Portrait-Portfolio/settings/pages  
2. **Build and deployment → Source** 选择 **GitHub Actions**  
3. 等待 Actions 工作流 `Deploy GitHub Pages` 跑绿  

完成后网站地址为：

**https://cengxvnuo.github.io/Emotional-Portrait-Portfolio/**

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
