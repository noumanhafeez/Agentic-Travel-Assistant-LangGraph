from langchain_core.messages import (
    HumanMessage,
    SystemMessage
)

from config.llm import get_llm


llm = get_llm()

def itinerary_agent(state):


    prompt = f"""
        Create a travel itinerary.
        User Query:
        {state['user_query']}

        Flight Results:
        {state['flight_results']}

        Hotel Results:
        {state['hotel_results']}
        """

    response = llm.invoke(

        [

            SystemMessage(
                content=(
                    "You are an expert "
                    "travel planner."
                )
            ),

            HumanMessage(
                content=prompt
            )

        ]

    )

    return {

        "itinerary":
        response.content,

        "messages":
        [response],

        "llm_calls":
        state.get(
            "llm_calls",
            0
        ) + 1
    }