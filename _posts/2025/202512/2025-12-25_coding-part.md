---
title: 'coding part'
date: 2025-12-25
permalink: /posts/2025/12/25/coding_part
tags:
  - coding
  - git config
  - remove ds_store
---

# about git
使用git进行版本管理，并且通过`touch ~/.gitignore_global`的方式在home目录下新建了全局git ignore的配置文件，把`.DS_Store`相关的文件都从git中剔除了（此后所有使用git进行版本控制的时候都不追踪该文件）。幸好目前使用git的项目只有两个，删除也比较方便配置步骤：
- 在home目录新建`.gitignore_global`文件
- 在文件中写入以下内容
    ```
    .DS_Store
    **/.DS_Store
    .DS_Store?
    ```
- 对git进行全局设置：`git config --global core.excludesfile ~/.gitignore_global`
- 使用`git config --list`查看是否有 `excludesfile = /Users/[username]/.gitignore_global` 相关内容
- 在已经进行版本控制的项目下，批量删除对 `.DS_Store` 的追踪

删除方式：
- 进入到使用git进行版本控制的项目目录下
- `find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch`
- `git commit -m "delet all .ds_store"`