def apiMessage(query_type: str, response: str) -> str:
    response_map = {
        "Queries": response,
        "Default": "I can't answer the provided query, for further information you can follow the provided link or contact us.",
        "Greet": response
    }

    if query_type in response_map:
        return response_map[query_type]
    else:
        raise ValueError("I can't help you right now")
