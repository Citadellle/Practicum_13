import re
import datetime

def time_to_special_format(time: str) -> int:
    time_parts = re.split(r'[/ :]+', time)
    month = int(time_parts[0])
    year = int(time_parts[2])
    day = int(time_parts[1])
    hour = int(time_parts[3])
    minute = int(time_parts[4])
    second = int(time_parts[5])

    first_date = datetime.datetime(year, 1, 1, 0, 0, 0)
    current_date = datetime.datetime(year, month, day, hour, minute, second)
    
    return ((current_date - first_date).days * 24 * 60 * 60 + (current_date - first_date).seconds)


print(time_to_special_format(input('Введите дату и время: ')))