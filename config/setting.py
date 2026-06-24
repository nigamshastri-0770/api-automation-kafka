import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://reqres.in/api"

REQRES_API_KEY = os.getenv(
    "REQRES_API_KEY"
)

KAFKA_TOPIC = "orders"

REQUEST_TIMEOUT = 15

RETRY_COUNT = 3