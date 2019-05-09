
class JsonSchemas():
    motor_resource_put_request_schema = {
        "type": "object",
        "contentMediaType": "",
        "required": [
            "speed",
            "direction"
        ],
        "properties": {
            "speed": {
                "$id": "#/properties/speed",
                "type": "integer",
                "title": "The Speed Schema",
                "default": 400,
                "examples": [
                    1000
                ],
                "minimum": 0.0,
                "maximum": 1000.0
            },
            "direction": {
                "$id": "#/properties/direction",
                "type": "integer",
                "title": "The Direction Schema",
                "default": 0,
                "examples": [
                    1
                ],
                "minimum": 0.0,
                "maximum": 1.0
            }
        }
    }
