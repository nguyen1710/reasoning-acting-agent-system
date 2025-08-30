import os

from .State import State
from Agents.AnalysistReactAgent.analyzer import SystemAnalyzer
from Agents.ValidatorAgent.ValidatorAgent import ValidatorAgent

from langgraph.graph import StateGraph, START, END

validator_model = "llama-3.3-70b-versatile"

# Intialize agents and builder
analyzer = SystemAnalyzer()
validator = ValidatorAgent(validator_model)
graph_builder = StateGraph(State)

# Node: phân tích specification
def analyze_spec(state: State) -> dict:
    result = analyzer.analyze(state["specification"])
    return {
        "actors": result.get("actors", []),    
        "usecases": result.get("usecases", []),
        "relationships": result.get("relationships", [])
    }

def validator_router(state: State) -> str:
    # if ANY error list is non-empty, go back to analyze
    if any([
        state.get("missing_actors"),
        state.get("missing_functions"),
        state.get("missing_relationships"),
        state.get("invalid_relationships"),
        state.get("wrong_actors"),
        state.get("wrong_targets"),
    ]):
        return "analyze"
    else:
        return END

graph_builder.add_node("analyze", analyze_spec)
graph_builder.add_node("validator", validator.validate)

graph_builder.add_edge(START, "analyze")
graph_builder.add_edge("analyze", "validator")
graph_builder.add_conditional_edges("validator", validator_router)

graph = graph_builder.compile()

# Xuất minh họa của graph
os.makedirs("misc", exist_ok=True)

graph_png = graph.get_graph().draw_mermaid_png()
with open("misc/graph.png", "wb") as f:
    f.write(graph_png)
    
print("Graph saved to misc/graph.png")