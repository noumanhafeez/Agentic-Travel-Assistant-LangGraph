from langchain_core.messages import AIMessage

from tools.flight_tool import (
    search_flights
)


def flight_agent(state):

    try:

        result = search_flights(
            state["user_query"]
        )

    except Exception as e:

        result = (
            f"Flight search failed: {e}"
        )

    return {

        "flight_results": result,

        "messages": [

            AIMessage(
                content="Flight data collected"
            )

        ],

        "llm_calls": (
            state.get(
                "llm_calls",
                0
            ) + 1
        )
    }