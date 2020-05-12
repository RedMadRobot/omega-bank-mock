if method == "GET":

    response_body = {
        "data": {
            "cards": [
                {
                    "id": 1,
                    "name": "Visa Classic",
                    "number": "NDSL RA01 203 4455 12",
                    "value": 1233
                },
                {
                    "id": 2,
                    "name": "Visa Classic",
                    "number": "NDSL RA01 203 4455 13",
                    "value": 5234
                },
                {
                    "id": 3,
                    "name": "Visa Gold",
                    "number": "NDSL RA01 203 4455 14",
                    "value": 6225
                },
                {
                    "id": 4,
                    "name": "Visa Platinum",
                    "number": "NDSL RA01 203 4455 15",
                    "value": 8885
                }
            ]
        }
    }

elif method == "POST":

    class Card:
        def __init__(self, name, number, value):
            self.name = name
            self.number = number
            self.value = value

    card_types = {
        "classic": Card("Visa Classic", "NDSL RA01 203 4455 16", 1000),
        "gold": Card("Visa Gold", "NDSL RA01 203 4455 16", 2000),
        "platinum": Card("Visa Platinum", "NDSL RA01 203 4455 16", 3000)
    }

    card_type = body_parameters.get("type", "Unsupported Type")

    card = card_types.get(card_type, Card("Unsupported Type", "-", -1))

    response_body = {
        "data": {
            "card": {
                "id": 5,
                "name": card.name,
                "number": card.number,
                "value": card.value
            }
        }
    }

else:
    response_body = "Invalid request"

