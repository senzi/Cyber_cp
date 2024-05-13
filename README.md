# Reflex 应用快速入门

本文档概述了创建一个基本Reflex应用的步骤。

环境准备
---

确保你已经安装了Python环境以及Reflex框架。如果没有安装Reflex框架，可以通过以下命令进行安装：

```bash
pip install reflex
```

创建应用
---

创建一个新的Python文件，例如 `app.py`。

使用以下代码作为应用的基础框架。

```python
from rxconfig import config
import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

class State(rx.State):
    """应用的状态类。"""

def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.chakra.vstack(
            rx.chakra.heading("欢迎使用 Reflex!", size="sm"),
            rx.chakra.text("通过编辑 ", rx.chakra.code(filename)),
            rx.chakra.button(
                "查看我们的文档!",
                on_click=lambda: rx.redirect(docs_url),
                size="sm",
            ),
            rx.logo(),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )

app = rx.App()
app.add_page(index)
```

运行应用
---

在命令行中，运行以下命令启动应用：

```bash
reflex run
```

应用结构
---

State 类用于管理应用的状态。

index 函数返回应用的主界面，包括一个欢迎标题、一个指向编辑文件的链接、一个按钮用于跳转到Reflex的文档，以及Reflex的Logo。

功能说明
---

用户点击“查看我们的文档!”按钮时，将会跳转到Reflex的官方文档页面。

注意事项
---

确保 `config.app_name` 已经正确设置为你的应用名称。

如果遇到网络问题导致文档链接无法打开，请检查网络连接或链接的有效性。

```bash
# 例如，如果你想改变前端端口，可以通过以下方式运行应用：
FRONTEND_PORT=3001 reflex run
```

或者，通过命令行参数来指定：

```bash
reflex run --frontend-port 3001
```

确保 `rxconfig.py` 文件已经正确设置，并且所有必要的环境变量和配置参数都已经被考虑进去。
```