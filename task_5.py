def buying_phone_card(p: str) -> int:
    price = int(p[p.find('$', 0)+1:])

    if price not in [5, 10, 25, 50, 100]:
        print('Недопустимое значение')

    match price:
        case 5:
            return 5
        case 10:
            return 10
        case 25:
            return 28
        case 50:
            return 58
        case 100:
            return 120


print(buying_phone_card(input('Введите стоимость карты в $: ')))