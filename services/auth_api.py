from core.retry_handler import safe_request

from config.setting import (
    BASE_URL,
    REQRES_API_KEY
)


class AuthAPI:

    def __init__(
        self,
        base_url=BASE_URL
    ):
        self.base_url = base_url

    def login(
        self,
        email,
        password
    ):

        response = safe_request(

            "POST",

            f"{self.base_url}/login",

            json={
                "email": email,
                "password": password
            },

            headers={

                "Content-Type":
                "application/json",

                "x-api-key":
                REQRES_API_KEY
            }
        )

        print(
            "STATUS:",
            response.status_code
        )

        print(
            "BODY:",
            response.text
        )

        assert response.status_code == 200

        return response.json()