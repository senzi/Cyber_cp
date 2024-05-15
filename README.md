---
title: Cyber CP Demo Application
emoji: 🤖
colorFrom: "#ff00ff" # 紫色
colorTo: "#00ffff" # 青色
sdk: Gradio
sdk_version: 4.31.1
app_file: app.py
pinned: false
---

# Cyber CP Demo 应用
这是一个使用Gradio库创建的简单应用，用于计算两个名字的CP值（兼容性得分）和生成基于名字性格特点的故事提示。

## 项目依赖
本项目依赖于`gradio`和`hashlib`库。项目依赖项已在`requirements.txt`文件中列出。安装依赖项的步骤如下：

1. 确保已经安装了Python环境。
2. 克隆本项目到本地，或者下载并解压项目压缩包。
3. 在项目根目录下，运行以下命令来安装依赖项：
   ```
   pip install -r requirements.txt
   ```

## 启动应用
要启动应用，请在项目根目录下执行以下命令：

```
python app.py
```

这将启动一个本地服务器，通常你可以在浏览器中通过访问 `http://localhost:7860` 来查看应用界面。

## 使用说明
1. 在应用界面中，输入两个名字（A和B）。
2. 点击“计算cp值”按钮，将计算并显示两个名字的哈希值和CP值。
3. 点击“生成故事Prompt”按钮，将根据两个名字生成一个故事提示。
4. 复制生成的故事提示，并可以将其交给Kimi生成故事。

## 注意事项
- 确保在运行应用之前已经安装了所有必需的依赖项。
- 如果在运行过程中遇到任何问题，请检查Python环境和依赖项是否正确安装。

---

希望您喜欢使用Cyber CP Demo应用！
```
