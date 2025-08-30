from .State import State
from .xml_builder import UMLXMLBuilder

class UMLXMLAgent:
    def __init__(self, state: State):
        self.state = state
        self.builder = UMLXMLBuilder(state)

    def run(self):
        self.builder.build_all()
        return self.builder.to_xml_string()

    def save(self, filename: str):
        self.builder.save_xml(filename)
