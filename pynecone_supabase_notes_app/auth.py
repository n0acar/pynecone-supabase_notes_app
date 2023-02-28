import pynecone as pc

from .base_state import State


class AuthState(State):
    email: str
    username: str
    password: str

    def signup(self):
        print("pain")
        return pc.redirect("/")

    def login(self):
        print("pain")
        return pc.redirect("/")


def signup() -> pc.Component:
    return pc.flex(
        pc.stack(
            pc.stack(
                pc.heading('Sign up'),
                pc.text('enjoy taking notes ✍')
            ),
            pc.box(
                pc.stack(
                    pc.form_control(
                        pc.form_label("email", html_for="email"),
                        pc.input(on_blur=AuthState.set_email),
                        is_required=True,
                    ),
                    pc.form_control(
                        pc.form_label("username", html_for="text"),
                        pc.input(on_blur=AuthState.set_username),
                        is_required=True,
                    ),
                    pc.form_control(
                        pc.form_label("password", html_for="password"),
                        pc.input(on_blur=AuthState.set_password),
                        is_required=True,
                    ),
                    pc.button(on_click=AuthState.signup)
                )
            ),
            pc.link(
                pc.button("Log In", width="100%"), href="/login")
            )
        )


def login() -> pc.Component:
    return pc.flex(
        pc.stack(
            pc.stack(
                pc.heading('Sign in'),
                pc.text('enjoy taking notes ✍')
            ),
            pc.box(
                pc.stack(
                    pc.form_control(
                        pc.form_label("email", html_for="email"),
                        pc.input(on_blur=AuthState.set_email),
                        is_required=True,
                    ),
                    pc.form_control(
                        pc.form_label("password", html_for="password"),
                        pc.input(on_blur=AuthState.set_password),
                        is_required=True,
                    ),
                    pc.button(on_click=AuthState.login)
                )
            ),
            pc.link(
                pc.button("Sign Up", width="100%"), href="/signup")
            )
        )

