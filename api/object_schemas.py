# actually we are testing mock api in this project, and there are few real constrains for the response,
# but lets' pretend we have more strict schema
create_object_response_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "data": {
            "type": "object",
            "properties": {
                "year": {"type": "integer"},
                "price": {"type": "number"},
                "CPU model": {"type": "string"},
                "Hard disk size": {"type": "string"}
            },
            "required": ["year", "price"]
        },
        "id": {"type": "string"}
    },
    "required": ["name", "data", "id"]
}
