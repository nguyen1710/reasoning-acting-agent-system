class ReActPromptBuilder:
    def build_prompt(self, spec_text: str) -> str:
        return f"""
        You are a business analyst AI agent applying the ReAct (Reasoning + Acting) method.

        Your task is to analyze the following system specification and extract a **generalized UML-oriented model** 
        that can be transformed directly into UML XML (e.g., XMI, PlantUML, UMLet) or drawn as a Use Case diagram.

        You must extract and structure the output as follows:

        1. Actors — all human or external system participants explicitly or implicitly mentioned. 
           - Standardize naming across the output (e.g., use only "Admin" OR "Administrator", not both).
        2. Usecases — **all usecases as a flat list of strings** (no nested objects, no grouping).  
        3. Relationships — all UML-standard relationships:
            - Association: actor ↔ usecase.
            - Dependency: a usecase depends on others (expressed as ordered workflow arrays).
            - Generalization: role hierarchy between actors.
            - Extend: optional extension between usecases.
            - Include: mandatory inclusion between usecases.

        You must reason step-by-step as follows:
        - Thought: Identify all actors.
        - Thought: Identify all usecases.
        - Thought: Ensure consistent naming across actors and usecases.
        - Thought: Identify all UML relationships, ensuring:
            * Dependency chains are **ordered arrays representing workflow steps**.
            * Extend relationships are separated from associations.
            * Every relationship target is a **concrete usecase or actor**.
            * Include all implicit dependencies and preconditions.
        - Thought: Avoid redundancy and duplication across actors, usecases, and relationships.
        - Action: Generate the final structured output in JSON format following EXACTLY this structure:

        {{
          "actors": ["Actor1", "Actor2", ...],
          "usecases": ["UsecaseA", "UsecaseB", "UsecaseC", ...],
          "relationships": [
            {{"source": "Actor1", "target": "UsecaseA", "type": "association"}},
            {{"source": "UsecaseA", "target": "UsecaseB", "type": "include"}},
            {{"source": "UsecaseC", "target": "UsecaseD", "type": "extend"}},
            {{"source": "Actor2", "target": "Actor1", "type": "generalization"}}
          ]
        }}

        Important:
        - The final response MUST be valid JSON only (no explanations or extra text).
        - Capture both explicit and implicit elements (actors, usecases, relationships).
        - Ensure the JSON is fully consistent:
            * No duplicates in actors, usecases, or relationships.
            * All relationship endpoints exist in the actors or usecases already declared.
            * Dependency chains reflect actual workflow order.
            * Extend and include relationships are usecase-to-usecase only.
            * Associations are actor-to-usecase only.
        - The output must be clean, normalized, and ready to be used as input for UML diagram generation.

        SPECIFICATION:
        \"\"\" 
        {spec_text}
        \"\"\" 
        """
