from langchain_core.messages import (
    HumanMessage,
    SystemMessage
)

from config.llm import (
    get_llm
)

from prompts.itinerary_prompt import (
    create_itinerary_prompt
)

llm = get_llm()


def itinerary_agent(state):

    prompt = (
        create_itinerary_prompt(
            user_query=state[
                "user_query"
            ],

            flights=state[
                "flight_results"
            ],

            hotels=state[
                "hotel_results"
            ]
        )
    )

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