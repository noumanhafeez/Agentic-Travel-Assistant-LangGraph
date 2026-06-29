from langgraph.graph import (StateGraph, START, END)
from schemas.state import (TravelState)
from agents.flight import (flight_agent)
from agents.hotel import (hotel_agent)
from agents.itinerary import (itinerary_agent)
from agents.final import (final_agent)
from memory.checkpoint import (create_checkpointer)


def build_graph():

    graph = StateGraph(TravelState)

    # Nodes

    graph.add_node("flight_agent", flight_agent)
    graph.add_node("hotel_agent", hotel_agent)
    graph.add_node("itinerary_agent", itinerary_agent)
    graph.add_node("final_agent", final_agent)

    # Edges

    graph.add_edge(START, "flight_agent")
    graph.add_edge("flight_agent", "hotel_agent")
    graph.add_edge("hotel_agent", "itinerary_agent")
    graph.add_edge("itinerary_agent", "final_agent")
    graph.add_edge("final_agent", END)

    # Memory Checkpointer

    checkpointer = (create_checkpointer())

    app = graph.compile(checkpointer=checkpointer)

    return app