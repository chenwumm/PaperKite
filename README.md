
# 🪁 PaperKite 极简版本控制系统

✨ 轻如纸鸢 | 仅140行代码 | 新手友好

## 📂 目录

- [1. 快速开始 🚀](#🚀 1. 快速开始)
- [2. 核心功能 📚](#📚 2. 核心功能)
- [3. 项目介绍 ❓](#❓ 3. 项目介绍)
- [4. 支持项目 🌟](#🌟 4. 支持项目)

---

## 🚀 1. 快速开始

```bash
# 克隆仓库 (🌟欢迎Star)
git clone https://github.com/chenwumm/PaperKite/

# 创建项目目录
mkdir my_project && cd my_project

# 初始化仓库 🌱
python ~/PaperKite/pkite.py init

# 添加所有文件 ➕
python ~/PaperKite/pkite.py add .

# 首次提交 💌
python ~/PaperKite/pkite.py commit "Hello PaperKite!"
```

---

## 📚 2. 核心功能

📦 仓库初始化

```bash
python ~/PaperKite/pkite.py init
```

- 创建隐藏的 `.pkite` 目录  
- 生成 `HEAD` 和 `index` 文件  
- ❗️ 已存在仓库时会提醒

➕ 文件追踪

```bash
# 添加单个文件
python ~/PaperKite/pkite.py add README.md

# 添加整个目录
python ~/PaperKite/pkite.py add .
```

- 使用 SHA-1 哈希存储文件内容  
- 自动忽略 `.pkite` 目录

---

## ❓ 3. 项目介绍

为什么要叫 "PaperKite"？

PaperKite 译作纸风筝，"纸" 代表这个项目是轻量级的，"风筝" 代表这个项目灵活易用。

有哪些优点？

1. 大约 160 行代码，体积小巧。  
2. 保留了其他版本控制系统（比如 Git、SVN 等）的核心功能，比如初始化、提交等。

有哪些缺点？

1. 相比 Git 等版本控制系统，PKite 缺少分支概念、代码版本差异对比等功能。  
2. 无法查看提交历史。  
3. 不适用于大型项目或多人协作。

适用于哪些场景？

1. 适用于个人开发、中小型项目等。  
2. 适用于了解 VCS（Version Control System，版本控制系统）的基本原理。

---

## 🌟 4. 支持项目

> 这是作者的第一个开源项目，欢迎到 GitHub 仓库贡献您的意见：

[https://github.com/chenwumm/PaperKite](https://github.com/chenwumm/PaperKite)

🌈 你的 Star 是我飞翔的动力，期待你们的 Issues 和 PR。

---

尾巴

本文档由 DeepSeek 帮助我编写，所以看着可能会有些 AI 成分，请见谅。

---

© 2025 PaperKite | 文档版本 1.1