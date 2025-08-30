import utils

from Agents.XMLAgent.uml_agent import UMLXMLAgent
from Graph.GraphBuilder import graph
from Graph.State import State

from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END

load_dotenv()

if __name__ == "__main__":
    required = [
        "specification",
        "actors",
        "usecases",
        "relationships",
        "missing_actors",
        "missing_usecases",
        "missing_relationships",
        "invalid_relationships",
        "wrong_actors",
        "wrong_targets",
    ]

    # Reading specification
    spec_file = "spec.txt"
    spec = utils.read_spec(spec_file)

    # Intialize State
    test_state: State = {
        "specification": spec,
    }

    result_state = graph.invoke(test_state)
    
    for key in result_state.keys():
        print(f'{key}: {result_state[key]}')
        print()

    agent = UMLXMLAgent(result_state)
    xml_str = agent.run()

    agent.save("uml.xml")