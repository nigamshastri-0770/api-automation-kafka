import time
import requests

RETRYABLE = [500, 502, 503, 504]


def safe_request(
        method,
        url,
        retries=3,
        timeout=10,
        **kwargs
):

    delay = 2

    for attempt in range(retries):

        try:

            response = requests.request(
                method,
                url,
                timeout=timeout,
                **kwargs
            )

            if response.status_code in RETRYABLE:

                raise requests.HTTPError(
                    f"Retryable: {response.status_code}"
                )

            return response

        except Exception:

            if attempt == retries - 1:
                raise

            time.sleep(delay)

            delay *= 2