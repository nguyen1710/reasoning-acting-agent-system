from chatLLM import ChatLLM
from promtBuilder import ReActPromptBuilder
from parser import ReActParser

class SystemAnalyzer:
    def __init__(self):
        self.llm = ChatLLM()
        self.prompt_builder = ReActPromptBuilder()
        self.parser = ReActParser()

    def analyze(self, spec_text: str) -> dict:
        prompt = self.prompt_builder.build_prompt(spec_text)
        raw_response = self.llm.query(prompt)
        return self.parser.parse(raw_response)
