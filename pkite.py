import os
import hashlib
import json
from datetime import datetime
import shutil

class PKite:
    def __init__(self):
        self.vcs_dir = ".pkite"
        self.objects_dir = os.path.join(self.vcs_dir, "objects")
        self.head_path = os.path.join(self.vcs_dir, "HEAD")
        self.index_path = os.path.join(self.vcs_dir, "index")

    def init(self):
        if os.path.exists(self.vcs_dir):
            print("PKite仓库已存在")
            return
        os.makedirs(self.objects_dir)
        with open(self.head_path, 'w') as f:
            f.write("")
        open(self.index_path, 'w').close()
        print("初始化空的PKite仓库")

    def add(self, filepath):
        if not os.path.exists(self.vcs_dir):
            print("错误：请先运行'pkite init'")
            return
        if not os.path.exists(filepath):
            print(f"错误：文件 '{filepath}' 不存在")
            return
        with open(filepath, 'rb') as f:
            content = f.read()
        file_hash = hashlib.sha1(content).hexdigest()
        obj_path = os.path.join(self.objects_dir, file_hash)
        if not os.path.exists(obj_path):
            with open(obj_path, 'wb') as f:
                f.write(content)
        with open(self.index_path, 'a') as f:
            f.write(f"{file_hash} {filepath}\n")
        print(f"添加 '{filepath}'")

    def commit(self, message):
        if not os.path.exists(self.vcs_dir):
            print("错误：请先运行'pkite init'")
            return
        if not os.path.exists(self.index_path) or os.path.getsize(self.index_path) == 0:
            print("错误：没有文件被暂存")
            return
        with open(self.index_path, 'r') as f:
            staged_files = [line.strip().split() for line in f.readlines()]
        commit_data = {
            "files": staged_files,
            "message": message,
            "timestamp": datetime.now().isoformat(),
            "parent": self._read_head()
        }
        commit_hash = self._store_object(json.dumps(commit_data).encode())
        with open(self.head_path, 'w') as f:
            f.write(commit_hash)
        open(self.index_path, 'w').close()
        print(f"提交成功 [{commit_hash[:6]}] {message}")

    def rollback(self):
        if not os.path.exists(self.vcs_dir):
            print("错误：请先运行'pkite init'")
            return
        current_commit_hash = self._read_head()
        if not current_commit_hash:
            print("错误：没有提交可回滚")
            return
        commit_data = self._read_commit(current_commit_hash)
        if not commit_data or "parent" not in commit_data:
            print("错误：无法读取父提交")
            return
        parent_commit_hash = commit_data["parent"]
        if not parent_commit_hash:
            print("错误：已经是最初提交，无法回滚")
            return
        parent_commit = self._read_commit(parent_commit_hash)
        if not parent_commit:
            print("错误：父提交数据损坏")
            return
        with open(self.head_path, 'w') as f:
            f.write(parent_commit_hash)
        for file_hash, filepath in parent_commit.get("files", []):
            self._restore_file(file_hash, filepath)
        print(f"已回滚到提交 [{parent_commit_hash[:6]}]")

    def _read_head(self):
        if os.path.exists(self.head_path):
            with open(self.head_path, 'r') as f:
                return f.read().strip()
        return ""

    def _store_object(self, data):
        obj_hash = hashlib.sha1(data).hexdigest()
        with open(os.path.join(self.objects_dir, obj_hash), 'wb') as f:
            f.write(data)
        return obj_hash

    def _read_commit(self, commit_hash):
        commit_path = os.path.join(self.objects_dir, commit_hash)
        if not os.path.exists(commit_path):
            return None
        with open(commit_path, 'rb') as f:
            return json.loads(f.read().decode())

    def _restore_file(self, file_hash, filepath):
        src_path = os.path.join(self.objects_dir, file_hash)
        if not os.path.exists(src_path):
            return False
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        shutil.copy(src_path, filepath)
        return True

def main():
    import argparse
    parser = argparse.ArgumentParser(description="pkite - 极简版本控制系统")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("init", help="初始化新仓库")
    add_parser = subparsers.add_parser("add", help="添加文件到暂存区")
    add_parser.add_argument("file", help="要添加的文件")
    commit_parser = subparsers.add_parser("commit", help="提交更改")
    commit_parser.add_argument("message", help="提交信息")
    subparsers.add_parser("rollback", help="回滚到上一次提交")
    args = parser.parse_args()
    pkite = PKite()
    if args.command == "init":
        pkite.init()
    elif args.command == "add":
        pkite.add(args.file)
    elif args.command == "commit":
        pkite.commit(args.message)
    elif args.command == "rollback":
        pkite.rollback()

if __name__ == "__main__":
    main()