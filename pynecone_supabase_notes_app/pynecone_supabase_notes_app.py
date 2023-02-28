import pynecone as pc

from .auth import login
from .auth import signup
from .base_state import State
from .notes import notes


def index():
    return pc.text("Home")


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.add_page(login)
app.add_page(signup)
app.add_page(notes, route="notes/[username]")

app.compile()
