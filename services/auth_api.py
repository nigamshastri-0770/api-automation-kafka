from config.setting import (
    BASE_URL,
    REQRES_API_KEY
)

from core.retry_handler import safe_request


class AuthAPI:

    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def login(
        self,
        email,
        password
    ):

        assert REQRES_API_KEY, "REQRES_API_KEY missing"

        response = safe_request(

            "POST",

            f"{self.base_url}/login",

            json={
                "email": email,
                "password": password
            },

            headers={
                "x-api-key": REQRES_API_KEY
            }
        )

        print(response.status_code)

        assert response.status_code == 200

        return response.json()