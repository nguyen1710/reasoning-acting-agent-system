from langgraph.graph import StateGraph, START, END
from .analyzer import SystemAnalyzer
from .State import State

analyzer = SystemAnalyzer()
graph_builder = StateGraph(State)

# Node: phân tích specification
def analyze_spec(state: State) -> dict:
    result = analyzer.analyze(state["specification"])
    return {
        "actors": result.get("actors", []),    
        "usecases": result.get("usecases", []),
        "relationships": result.get("relationships", [])
    }

graph_builder.add_node("analyze", analyze_spec)
graph_builder.add_edge(START, "analyze")
graph_builder.add_edge("analyze", END)

graph = graph_builder.compile()
