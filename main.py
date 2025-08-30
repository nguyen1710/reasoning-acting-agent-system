from AnalysistReactAgent.graphBuilder import graph
from AnalysistReactAgent.State import State
from XMLAgent.uml_agent import UMLXMLAgent

if __name__ == "__main__":
    spec = """
    The system is an E-Commerce Platform.

    Guests can browse products and must register before logging in.  
    Users can log in, search for products, add items to the shopping cart, and place orders.  
    Placing an order requires the user to log in and have at least one item in the cart.  
    Users can also write product reviews after purchasing an item.  

    Premium Users, who are a specialized type of User, can access exclusive deals and faster shipping options.  

    Sellers can list new products, update product details, and manage their inventory. They must log in before performing these actions.  

    DeliveryStaff are responsible for shipping orders, updating delivery status, and confirming delivery.  

    Administrators oversee the entire system. They can approve or block sellers, manage users, and handle disputes.  
    Administrators must log in before performing any action.  

    SupportAgents can assist users by answering queries and resolving complaints. Their ability to resolve complaints depends on the complaint submission by users.  

    All reviews must be linked to a specific product, and complaints must be linked to a specific order.
    """

    # Bước 1: chạy graph để phân tích spec
    analyzed_state: State = graph.invoke({"specification": spec})

    # Bước 2: chuyển sang UML Agent
    uml_state: State = {
        "actors": analyzed_state.get("actors", []),
        "usecases": analyzed_state.get("usecases", []),
        "relationships": analyzed_state.get("relationships", [])
    }

    agent = UMLXMLAgent(uml_state)
    xml_str = agent.run()

    print(xml_str)
    agent.save("uml.xml")
