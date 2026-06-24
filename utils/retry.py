import time

def retry(fn, timeout=10, interval=1):
    """
    Retry function until success or timeout
    """
    start = time.time()

    while time.time() - start < timeout:
        result = fn()
        if result:
            return result
        time.sleep(interval)

    return None