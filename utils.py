import os

def parse_time(time_string):
    year = time_string[0:4]
    month = time_string[4:6]
    day = time_string[6:8]
    hour = time_string[8:12]
    return [year, month, day, hour]

def get_path(year, month, day):
    return os.path.join(year, month, day)

