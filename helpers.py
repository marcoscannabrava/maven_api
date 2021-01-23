from datetime import datetime, timedelta
from dateutil.parser import isoparse

# Helpers
def round_time(iso_timestring, delta=timedelta(minutes=30)):
    dt = isoparse(iso_timestring)
    return dt + (datetime.min - dt) % delta
