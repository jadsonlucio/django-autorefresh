from django.conf import settings
from fresh import settings as fresh_settings


def filter_fresh_request(record):
    msg, level, _ = record.args
    if getattr(settings, "FRESH_FILTER_LOGGING", fresh_settings.FRESH_FILTER_LOGGING):
        fresh_filter_path = f"GET {getattr(settings, 'FRESH_FILTER_PATH', fresh_settings.FRESH_FILTER_PATH)}"
        if (
            getattr(settings, "FRESH_FILTER_LEVEL", fresh_settings.FRESH_FILTER_LEVEL)
            >= int(level)
            and fresh_filter_path in msg
        ):
            return False

    return True
