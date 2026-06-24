import os

BASE_URL = "https://reqres.in/api"

REQRES_API_KEY = os.getenv(
    "free_user_3EqwNfJjHbaSI4VWRBchJllgjn9"
)

KAFKA_TOPIC = "orders"

REQUEST_TIMEOUT = 15

RETRY_COUNT = 3