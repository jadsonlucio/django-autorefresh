from fresh.settings import Config


def filter_fresh_request(record):
    msg, level, _ = record.args
    if Config.FILTER_LOGGING:
        if Config.FILTER_LEVEL >= int(level) and f"GET {Config.FILTER_PATH}" in msg:
            return False

    return True
