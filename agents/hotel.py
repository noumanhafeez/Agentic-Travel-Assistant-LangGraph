from langchain_core.messages import AIMessage

from tools.search_tool import (
    tavily_search
)


def hotel_agent(state):

    query = (
        f"Best hotels for "
        f"{state['user_query']}"
    )

    try:

        result = tavily_search(
            query
        )

    except Exception as e:

        result = (
            f"Hotel search failed: {e}"
        )

    return {

        "hotel_results": result,

        "messages": [

            AIMessage(
                content="Hotel data collected"
            )

        ],

        "llm_calls": (
            state.get(
                "llm_calls",
                0
            ) + 1
        )
    }