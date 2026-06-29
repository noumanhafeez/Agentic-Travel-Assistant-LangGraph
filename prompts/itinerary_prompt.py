

def create_itinerary_prompt(user_query, flights, hotels):

    return f"""
        Create a professional travel itinerary.

        User Request:
        {user_query}

        Flights:
        {flights}

        Hotels:
        {hotels}

        Generate:
            - Flight recommendation
            - Hotel recommendation
            - Daily itinerary
            - Budget tips
    """