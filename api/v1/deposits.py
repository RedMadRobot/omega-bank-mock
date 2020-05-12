if method == "GET":

    response_body = {
        "data": {
            "deposits": [
                {
                    "id": 5,
                    "name": "Platinum",
                    "number": "NDSL RA01 203 4455 01",
                    "value": 30234
                },
                {
                    "id": 6,
                    "name": "Package",
                    "number": "NDSL RA01 203 4455 02",
                    "value": 12976
                },
                {
                    "id": 7,
                    "name": "Elite",
                    "number": "NDSL RA01 203 4455 03",
                    "value": 51234
                },
                {
                    "id": 8,
                    "name": "Platinum",
                    "number": "NDSL RA01 203 4455 04",
                    "value": 73417
                }
            ]
        }
    }

elif method == "POST":

    class Deposit:
        def __init__(self, name, number, value):
            self.name = name
            self.number = number
            self.value = value
    
    deposit_types = {
        "package": Deposit("Package", "NDSL RA01 203 4455 05", 10000),
        "platinum": Deposit("Platinum", "NDSL RA01 203 4455 06", 20000),
        "elite": Deposit("Elite", "NDSL RA01 203 4455 07", 30000)
    }

    deposit_type = body_parameters.get("type", "Unsupported Type")

    deposit = deposit_types.get(deposit_type, Deposit("Unsupported Type", "-", -1))
    
    response_body = {
        "data": {
            "deposit": {
                "id": 9,
                "name": deposit.name,
                "number": deposit.number,
                "value": deposit.value
            }
        }
    }

else:
    response_body = "Invalid request"
