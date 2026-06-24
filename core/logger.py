import logging

logger = logging.getLogger("api")
logger.setLevel(logging.INFO)

if not logger.handlers:
    h=logging.StreamHandler()
    f=logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    h.setFormatter(f)
    logger.addHandler(h)
