# 🐍 使用 `pyenv` 管理多版本 Python（macOS 专用笔记）

> ✅ 适用于：保留旧版（如 3.8.9），安装新版（如 3.14/3.13/3.12），自由切换，互不干扰  
> ⚠️ 前提：已安装 [Homebrew](https://brew.sh)

---

## 一、为什么用 `pyenv`？

- 安全安装多个 Python 版本（官方、Homebrew、系统自带互不影响）
- 通过 `python` 命令自动指向当前激活版本
- 支持 **全局默认** 或 **项目级局部** 版本设置
- 所有版本安装在 `～/.pyenv/versions/`，干净隔离

---

## 二、安装 `pyenv`

```bash
# 1. 通过 Homebrew 安装
brew install pyenv

# 2. 配置 shell（以 zsh 为例，macOS 默认）
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ～/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ～/.zshrc
echo 'eval "$(pyenv init -)"' >> ～/.zshrc

# 3. 重载配置
source ～/.zshrc
# 或关闭终端后重新打开
```

> 💡 如果你用 **bash**，请将 `.zshrc` 替换为 `～/.bash_profile`

---

## 三、常用命令速查

| 命令 | 说明 |
|------|------|
| `pyenv --version` | 查看 pyenv 版本 |
| `pyenv install --list` | 列出所有可安装的 Python 版本 |
| `pyenv install 3.11.4` | 安装指定版本（首次会编译，稍慢） |
| `pyenv versions` | 查看已安装的版本（带 `*` 表示当前激活） |
| `pyenv global 3.11.4` | 设置 **全局默认** Python 版本 |
| `pyenv local 3.8.9` | 在当前目录设置 **项目级** Python 版本（生成 `.python-version` 文件） |
| `pyenv rehash` | 重建 shims（安装新包或修复命令时用） |

---

## 四、验证是否生效

```bash
# 查看当前 python 路径（应来自 pyenv）
which python
# → /Users/xxx/.pyenv/shims/python

# 查看版本
python --version    # 应显示你设置的版本，如 Python 3.11.4
python3 --version   # 同样有效，与 python 指向同一解释器

# 查看 shims 是否包含 python
ls ～/.pyenv/shims/python*
# 应包含：python, python3, python3.11 等
```

---

## 五、常见问题解决

### ❌ 问题1：`pyenv global` 设置了，但 `python --version` 还是旧版本  
✅ **原因**：shell 未正确加载 pyenv 初始化脚本  
🔧 **解决**：
- 确保 `～/.zshrc` 中包含：
  ```bash
  eval "$(pyenv init -)"
  ```
- 执行 `source ～/.zshrc` 或重启终端

---

### ❌ 问题2：`python` 命令不存在，只有 `python3`  
✅ **原因**：某些 Python 构建未自动生成 `python` shim（罕见）  
🔧 **解决**：
```bash
# 重新安装当前版本（会重建 shims）
pyenv install --force 3.11.4
pyenv global 3.11.4
```

---

### ❌ 问题3：VS Code / IDE 仍使用旧解释器  
✅ **解决**：
- 在 VS Code 中按 `Cmd+Shift+P` → 输入 `Python: Select Interpreter`
- 手动选择：`～/.pyenv/versions/3.11.4/bin/python`

---

## 六、安全提醒

- 🔒 **不要修改 `/usr/bin/python`** —— macOS 系统依赖它
- 🔒 **不要手动创建全局软链接**（如 `ln -s ... /usr/local/bin/python`）——会破坏 pyenv 管理
- ✅ 所有操作都在用户目录下完成，完全安全

---

## 七、推荐工作流

```bash
# 安装常用稳定版本
pyenv install 3.11.9
pyenv install 3.12.7
pyenv install 3.14.0

# 全局用最新稳定版
pyenv global 3.14.0

# 老项目用旧版
cd ～/legacy-project
pyenv local 3.8.9

# 新项目用现代版
cd ～/new-project
pyenv local 3.12.7
```

> 每个项目自动使用对应 Python，无需手动切换！

---

## 八、附：Python 官方支持状态（截至 2026 年 1 月）

| 版本 | 状态 | 建议 |
|------|------|------|
| 3.14 | ✅ 最新稳定 | 新项目首选 |
| 3.13 | ✅ 稳定 | 可用 |
| 3.12 | ✅ 仅安全更新 | 保守项目可用 |
| 3.11 | ✅ 仅安全更新 | 兼容性好 |
| 3.10 | ⚠️ 2026-10 停止支持 | 尽量避免 |
| **3.8 / 3.9** | ❌ **已停止支持** | **尽快迁移** |

---

> 📌 **你的当前版本：Python 3.8.9（已于 2024 年 10 月停止支持）→ 强烈建议升级！**