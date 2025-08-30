from typing_extensions import TypedDict

class State(TypedDict):
    specification: str
    actors: list[str]
    usecases: list[dict]    
    relationships: list[dict]  


