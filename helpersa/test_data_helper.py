import random
import uuid


def get_valid_object():
    def random_string():
        return str(uuid.uuid4())

    def random_year():
        return random.randint(2015, 2023)

    def random_price():
        return round(random.uniform(1000.00, 3000.00), 2)

    obj = {
        "name": random_string(),
        "data": {
            "year": random_year(),
            "price": random_price(),
            "CPU model": random_string(),
            "Hard disk size": random_string()
        }
    }

    return obj