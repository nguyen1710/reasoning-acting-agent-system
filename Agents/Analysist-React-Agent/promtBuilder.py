class ReActPromptBuilder:
    def build_prompt(self, spec_text: str) -> str:
        return f"""
                    You are a business analyst AI agent applying the ReAct (Reasoning + Acting) method.

                    Your task is to analyze the following system specification and extract:
                    1. Actors — the human or system participants involved.
                    2. Functions — the key actions or behaviors allowed in the system.
                    3. Relationships — describe links in the form [Actor → Function → Target].

                    You must reason step-by-step as follows:
                    - Thought: Identify all possible actors.
                    - Thought: Identify what actions each actor can perform.
                    - Thought: Group related actions under logical functions.
                    - Action: Generate the final structured output in the format:

                    {{
                    "actors": [...],
                    "functions": [...],
                    "relationships": [
                        {{"actor": "X", "function": "Y", "target": "Z"}}
                    ]
                    }}

                    SPECIFICATION:
                    \"\"\"
                    {spec_text}
                    \"\"\"
                """
