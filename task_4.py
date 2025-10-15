def make_payment(p: str) -> None:
    price = int(p[p.find('$', 0)+1:])
    error_mark = 0
    
    if price > 1000:
        error_mark += 1
    elif price < 20:
        error_mark += 1
    
    if error_mark > 0:
        print('Повторить попытку')
    else:
        print('Успех')


make_payment(input('Введите платеж по кредитной карте в $: '))