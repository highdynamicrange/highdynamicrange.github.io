# 个人主页维护

## 两个站点的分工

- 个人主页：个人介绍、关注方向、早期编程笔记与 HDR Lab 入口。
- HDR Lab：AI 工具项目、评测设计、实验报告和新的产品与内容体验。

新内容通常写入 HDR Lab；个人主页中的精选项目链接在 `src/pages/index.astro` 更新。两个仓库各自构建、发布，互相用公开网址关联，没有运行时接口依赖。

## 早期笔记

`src/content/archive` 是当前网站使用的内容集合。原始文件继续保留在 `_posts`；迁移时只补充标题、摘要与来源，正文不变。`npm test` 检查三篇原始正文的一致性。

没有原始日期的游戏项目笔记不补造日期。旧的 Git 笔记 permalink、`/year-archive/`、`/portfolio/` 和 `/about.html` 保留兼容入口。

## 视觉主题

`src/styles/global.css` 与 HDR Lab 共用同一套初始设计：纸色底、松绿色、编辑手记式标题。两个仓库分别保有样式文件，修改共同主题时需同步更新并检查两站页面。

## 构建与发布

Node.js 24，`npm ci` 后运行 `npm run dev`。`npm run verify` 执行类型检查、归档正文测试、构建与站内链接检查。链接检查使用 Python 3。

推送 `master` 后通过 GitHub Actions 部署 `dist`。GitHub Pages 的构建来源应设为 GitHub Actions。

## 旧模板保留

`_pages`、`_layouts`、`_includes`、`_sass`、`_publications` 等为原 Academic Pages / Jekyll 模板，保留为历史源文件，不进入当前 Astro 构建。其 npm 工具与 MIT 许可证仍保留。

`_config.yml` 中已保留已有的 `HDR` 名称，并修正个人资料与 GitHub 地址。兼容导航与旧首页也已指向当前主题。原 talk-map 自动任务改为手动运行，避免模板流程继续写入无关内容。

当前发布只依赖 `src`、`public`、Astro 配置与锁定依赖，不再需要 Ruby。
