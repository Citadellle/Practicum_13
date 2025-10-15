import re
import calendar

def time_to_special_format(time: str) -> None:
    time_parts = re.split(r'[/ :]+', time)
    month = int(time_parts[0])
    day = int(time_parts[1])
    year = time_parts[2]    
    hour = int(time_parts[3])
    minute = int(time_parts[4])
    second = int(time_parts[5])

    if (month > 12 or month < 1) or (minute > 59 or minute < 0) or (second > 59 or second < 0) \
        or (day > calendar.monthrange(int(year), month)[1] or day < 1):
        print('Ошибка в вводе времени')
        return None
    
    if hour > 24:
        print('Ошибка в вводе времени')
        return None
    elif hour in [i for i in range(0, 11+1)]:
        hour = f'{hour}AM'
    else:
        hour = f'{hour}PM'
        
    
    time_in_special_format = f'{day}.{month}.{year[2:4]} {hour}:{minute}:{second}'

    print(time_in_special_format)
time_to_special_format(input('Введите дату и время: '))
