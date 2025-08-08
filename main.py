import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END

from LangGraph.State import State
from Agents.ValidatorAgent.ValidatorAgent import ValidatorAgent

load_dotenv()

model = "llama-3.3-70b-versatile"
# Khởi tạo các agent
validator = ValidatorAgent(model)

# Xây dựng graph
graph_builder = StateGraph(State)

# Thêm các node vào graph
# graph_builder.add_node("analysist_agent", )
graph_builder.add_node("validator_agent", validator.validate)

# Kết nối các node trong graph
# graph_builder.add_edge(START, "analysist_agent")
# graph_builder.add_edge("analysist_agent", "validator_agent")
graph_builder.add_edge(START, "validator_agent")
graph_builder.add_edge("validator_agent", END)

graph = graph_builder.compile()

# Xuất minh họa của graph
os.makedirs("misc", exist_ok=True)

graph_png = graph.get_graph().draw_mermaid_png()
with open("misc/graph.png", "wb") as f:
    f.write(graph_png)

print("Graph saved to misc/graph.png")

if __name__ == "__main__":
    test_state: State = {
        "specification":    """"
                            Users can register accounts, log in, and edit personal information.
                            Administrators can approve new users, block offending accounts.
                            Both can create posts, comment, and rate other posts.
                            """,
        "actors": ['User', 'Admin'], 
        "functions": ['Register account', 'Login', 'Edit personal information', 'Approve new users', 'Block violating accounts', 'Create post', 'Comment', 'Rate posts'], 
        "relationships": [{'actor': 'User', 'function': 'Register account', 'target': 'System'}, {'actor': 'User', 'function': 'Login', 'target': 'System'}, {'actor': 'User', 'function': 'Edit personal information', 'target': 'Own account'}, {'actor': 'Admin', 'function': 'Approve new users', 'target': 'User accounts'}, {'actor': 'Admin', 'function': 'Block violating accounts', 'target': 'User accounts'}, {'actor': 'User', 'function': 'Create post', 'target': 'Content'}, {'actor': 'Admin', 'function': 'Create post', 'target': 'Content'}, {'actor': 'User', 'function': 'Comment', 'target': 'Content'}, {'actor': 'Admin', 'function': 'Comment', 'target': 'Content'}, {'actor': 'User', 'function': 'Rate posts', 'target': 'Content'}, {'actor': 'Admin', 'function': 'Rate posts', 'target': 'Content'}],
    }

    test_run = graph.invoke(test_state)
    print("Test run result:", test_run)