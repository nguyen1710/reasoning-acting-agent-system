import os
import groq
from LangGraph.State import State

class ValidatorAgent:
    def __init__(self, model):
        self.agent = groq.Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )
        self.model = model

    def validate(self, state: State):
        return self.agent.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content":  """
                                You are a validator agent. Your task is to validate the list of actors, functions and relationships created by the analyst agent with the system specification.
                                You will check if any actors, functions or relationship are missing.
                                For relationships, will check if it is a valid relationship and if its actor and target are correct.
                                Your output should follow this format:
                                Missing Actors: [list of missing actors]
                                Missing Functions: [list of missing functions] 
                                Missing Relationships: [list of missing relationships]
                                Invalid Relationships: [list of invalid relationships]
                                Relationships with wrong actors: [list of relationships with wrong actors]
                                Relationships with wrong targets: [list of relationships with wrong targets]
                                """,
                },
                {
                    "role": "user",
                    "content": f"""
                                System Specification: {state["specification"]}
                                Actors: {state["actors"]}
                                Functions: {state["functions"]}
                                Relationships: {state["relationships"]}
                                """,
                }
            ],
            model=self.model,
        ).choices[0].message.content
    