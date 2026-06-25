import requests


class OrderService:

    BASE_URL = "https://dummyjson.com"

    @classmethod
    def get_order(cls):

        response = requests.get(
            f"{cls.BASE_URL}/products/1"
        )

        return response