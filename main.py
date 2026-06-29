from langchain_core.messages import HumanMessage
from graph.workflow import build_graph

app = build_graph()


def run():

    config = {"configurable": {"thread_id":"user_aarohi"}}

    user_input = input(
        "Enter travel request: "
    )

    result = app.invoke(

        {

            "messages": [

                HumanMessage(
                    content=user_input
                )

            ],

            "user_query":
            user_input,

            "flight_results":
            "",

            "hotel_results":
            "",

            "itinerary":
            "",

            "llm_calls":
            0

        },

        config=config
    )

    print(
        "\nFINAL RESPONSE\n"
    )

    print(
        result[
            "messages"
        ][-1].content
    )


if __name__ == "__main__":
    run()