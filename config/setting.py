import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://reqres.in/api"

REQRES_API_KEY = "free_user_3EqwNfJjHbaSI4VWRBchJllgjn9"

KAFKA_TOPIC = "orders"

REQUEST_TIMEOUT = 15

RETRY_COUNT = 3