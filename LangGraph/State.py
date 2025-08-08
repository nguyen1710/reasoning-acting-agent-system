from typing_extensions import TypedDict

class State(TypedDict):
    specification: str
    actors: list[str]
    functions: list[str]
    relationships: list[str]