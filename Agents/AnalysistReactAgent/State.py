from typing_extensions import TypedDict

class State(TypedDict):
    specification: str
    actors: list[str]     
    usecases: list[str]
    relationships: list[dict]