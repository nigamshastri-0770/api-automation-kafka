from services.auth_api import (
    AuthAPI
)

from config.setting import (
    BASE_URL
)


def test_login():

    api = AuthAPI(
        BASE_URL
    )

    result = api.login(

        "eve.holt@reqres.in",

        "cityslicka"
    )

    assert "token" in result