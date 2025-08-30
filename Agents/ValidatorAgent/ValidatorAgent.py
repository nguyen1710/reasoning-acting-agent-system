import re
import os
import groq
from Graph.State import State
from typing import Dict, List

class ValidatorAgent:
    def __init__(self, model):
        self.agent = groq.Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )
        self.model = model
        self.reasoning_traces = ""

    def update_state(self, state, answer: str) -> Dict[str, List[str]]:
        keys = ["missing_actors",
                "missing_usecases",
                "missing_relationships",
                "invalid_relationships",
                "wrong_actors",
                "wrong_targets"]

        for key in keys:
            state[key] = []
            # ?<= - look behind
            # \s - space
            # [] - một chuỗi các ký tự
            # ^] - ngoại trừ ký tự ]
            lst = re.findall(rf"(?<={key}:)([^]]+)", answer)
            for item in lst:
                cleaned_item = item.strip(" []'\"")
                if cleaned_item:
                    state[key].append(cleaned_item)

    def validate(self, state: State):
        answer = self.agent.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content":  """
                                Your task is to validate lists of actors, usecases and relationships with the system specification.
                                Validation criteria included:
                                (1) No missing actors, usecases or relationships.
                                (2) No extra actors, usecases or relationships.
                                (3) No invalid relationships.
                                (4) Relationships' actors and funcitons must be matched.
                                Validate with interleaving Thought, Action, Observation steps. Thought can be reason about the current situation, and Action can three types:
                                (1) Seach[actors/usecases/relationships], which searches for actors/usecases/relationships presented in system specification.
                                (2) Lookup[actors/usecases/relationships], which look for actors/usecases/relationships in the provied lists of actors/usecases/relationships.
                                (3) Finish[status], which return the status of the actors/usecases/relationships and put it in the correctsponding result's lists, lists of status included: [correct, missing, extra, invalid, wrong actor, wrong target];
                                The output must explicitly follow the format for validate reason
                                Output format:
                                missing_actors:[list of actors with 'missing' status]
                                missing_usecases:[list of usecases with 'missing' status] 
                                missing_relationships:[list of relationships 'missing' status]
                                invalid_relationships:[list of relationships 'invalid' status]
                                wrong_actors:[list of relationships with 'wrong actors' status]
                                wrong_targets:[list of relationships with 'wrong targets' status]
                                """,
                },
                {
                    "role": "user",
                    "content": f"""
                                System Specification: {state["specification"]}
                                Actors: {state["actors"]}
                                Usecases: {state["usecases"]}
                                Relationships: {state["relationships"]}
                                """,
                }
            ],
            model=self.model,
        )
        self.reasoning_traces = answer.choices[0].message.content
        self.update_state(state, self.reasoning_traces)
        return {
        "missing_actors": state.get("missing_actors", []),
        "missing_usecases": state.get("missing_usecases", []),
        "missing_relationships": state.get("missing_relationships", []),
        "invalid_relationships": state.get("invalid_relationships", []),
        "wrong_actors": state.get("wrong_actors", []),
        "wrong_targets": state.get("wrong_targets", []),
    }