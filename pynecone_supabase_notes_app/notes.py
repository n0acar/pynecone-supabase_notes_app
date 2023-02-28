import pynecone as pc

from .base_state import State

class NotesState(State):
    @pc.var
    def owner_username(self):
        return self.get_query_params().get("username")

def notes():
    return pc.text("User" + NotesState.owner_username)