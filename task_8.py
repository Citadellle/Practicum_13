import re
import calendar

def time_to_special_format(time: str) -> None:
    time_parts = re.split(r'[/ :]+', time)
    month = int(time_parts[0])
    if month > 12:
        print('Ошибка в вводе времени')
        return None

    year = time_parts[2]

    day = int(time_parts[1])
    if day > calendar.monthrange(int(year), month)[1]:
        print('Ошибка в вводе времени')
        return None

    hour = int(time_parts[3])
    if hour > 24:
        print('Ошибка в вводе времени')
        return None
    elif hour in [i for i in range(0, 11+1)]:
        hour = f'{hour}AM'
    else:
        hour = f'{hour}PM'
    
    minute = int(time_parts[4])
    if minute > 59:
        print('Ошибка в вводе времени')
        return None
    
    second = int(time_parts[5])
    if second > 59:
        print('Ошибка в вводе времени')
        return None
    
    time_in_special_format = f'{day}.{month}.{year[2:4]} {hour}:{minute}:{second}'

    print(time_in_special_format)



time_to_special_format(input('Введите дату и время: '))