from typing_extensions import TypedDict
import json

class State(TypedDict):
    specification: str
    actors: list[str]
    usecases: list[str]
    relationships: list[str]
    missing_actors: list[str]
    missing_usecases: list[str]
    missing_relationships: list[str]
    invalid_relationships: list[str]
    wrong_actors: list[str]
    wrong_targets: list[str]