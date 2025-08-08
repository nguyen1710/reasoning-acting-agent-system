import json

class ReActParser:
    def parse(self, response_text: str) -> dict:
        start = response_text.find("{")
        end = response_text.rfind("}") + 1
        try:
            json_str = response_text[start:end]
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON format from LLM response.")

