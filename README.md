# HDR · highdynamicrange

个人主页与早期编程笔记，与 **HDR Lab** 的 AI 实践和评测内容相连接。

- 个人主页：<https://highdynamicrange.github.io/>
- HDR Lab：<https://highdynamicrange.github.io/hdr-lab/>
- 实验室源码：<https://github.com/highdynamicrange/hdr-lab>

## 开发

使用 Node.js 24（`.nvmrc`）：

```bash
npm ci
npm run dev
npm run verify
```

默认开发地址 `http://localhost:4321/`。`npm run verify` 执行 Astro 类型检查、历史笔记保留测试、静态构建与链接检查。链接检查依赖 Python 3 标准库。

## 内容

- `src/pages/index.astro`：个人介绍和 HDR Lab 精选入口。
- `src/pages/about.astro`：关于我。
- `src/content/archive`：三篇早期笔记，正文从原始文件迁移保留。
- `src/styles/global.css`：与 HDR Lab 统一的视觉主题。

新的作品、评测与体验笔记写在 HDR Lab，通过其内容创建命令自动生成页面；本仓库保留个人入口与历史记录。

## 发布

推送到 `master` 后，GitHub Actions 验证并部署 `dist`。Pages 构建来源需设置为 GitHub Actions。

当前站点使用 Astro。原 Jekyll 模板和文章源文件留在仓库中，未作为新网站内容发布；原 MIT 许可证保留。详见 [维护说明](docs/maintenance.md) 与 [原模板文档](docs/legacy-academicpages.md)。
