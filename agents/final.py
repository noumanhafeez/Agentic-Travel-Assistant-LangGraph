from langchain_core.messages import (
    HumanMessage
)

from config.llm import (
    get_llm
)

from prompts.final_prompt import (
    create_final_prompt
)

llm = get_llm()


def final_agent(state):

    prompt = (
        create_final_prompt(

            flights=
            state[
                "flight_results"
            ],

            hotels=
            state[
                "hotel_results"
            ],

            itinerary=
            state[
                "itinerary"
            ]
        )
    )

    response = llm.invoke(

        [

            HumanMessage(
                content=prompt
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