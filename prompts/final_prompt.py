


def create_final_prompt(flights, hotels, itinerary):

    return f"""
        Generate final travel response.

        Flights:
        {flights}

        Hotels:
        {hotels}

        Itinerary:
        {itinerary}

        Format:
        1. Flight
        2. Hotel
        3. Travel Plan
        4. Summary
    """