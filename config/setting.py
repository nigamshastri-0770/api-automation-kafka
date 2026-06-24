import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://reqres.in/api"

REQRES_API_KEY = os.getenv(
    "REQRES_API_KEY"
)

# LOCAL → localhost:9092
# GITHUB ACTIONS → kafka:9092
KAFKA_SERVER = os.getenv(
    "KAFKA_BOOTSTRAP_SERVERS",
    "localhost:9092"
)

KAFKA_TOPIC = "orders"

REQUEST_TIMEOUT = 15

RETRY_COUNT = 3