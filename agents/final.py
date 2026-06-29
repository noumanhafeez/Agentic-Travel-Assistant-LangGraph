from langchain_core.messages import (
    HumanMessage
)

from config.llm import get_llm


llm = get_llm()

def final_agent(state):


    final_prompt = f"""
        Generate final travel response.

        Flights:
        {state['flight_results']}

        Hotels:
        {state['hotel_results']}

        Itinerary:
        {state['itinerary']}
        """

    response = llm.invoke(

        [

            HumanMessage(
                content=final_prompt
            )

        ]

    )

    return {

        "messages":
        [response],

        "llm_calls":
        state.get(
            "llm_calls",
            0
        ) + 1
    }