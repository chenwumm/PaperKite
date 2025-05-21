---
这个是旧版文档，新版文档请见[https://chenwumm.github.io/doc/pkite.html](https://chenwumm.github.io/doc/pkite.html)
---
# PaperKite使用文档
PaperKite(简称PKite)是一个极简代码版本控制系统，他大约只有160行代码。接下来介绍他如何使用。
## 一 克隆PKite仓库
```bash
git clone https://github.com/chenwumm/PaperKite/
```
## 二 初始化仓库
新建仓库目录并切换到仓库目录:
```bash
mkdir 仓库名称
cd 仓库名称
```
执行:
```bash
python ~/PaperKite/pkite.py init
```
初始化pkite仓库。
## 三 把文件添加到暂存区并提交
执行以下命令，把文件添加到暂存区:
```bash
python ~/PaperKite/pkite.py 要添加的文件
```
好像还不支持添加本目录(add .)  
截至5月20日，PaperKite已经支持添加本目录(add .)。  
提交:
```bash
python ~/PaperKite/pkite.py commit "提交信息"
```
## 四 回滚到上一次提交
```bash
python ~/PaperKite/pkite.py rollback
```
## 尾巴
这个其实是我开源的第一个小项目啦。希望多点follow和star。
