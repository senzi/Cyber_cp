"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.chakra.vstack(
            rx.chakra.heading("Welcome to Reflex!", size="sm"),
            rx.chakra.text("Get started by editing ", rx.chakra.code(filename)),
            rx.chakra.button(
                "Check out our docs!",
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
