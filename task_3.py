def calculating_price_with_discount(price: float,
                                    discount_card: int,
                                    holiday: int
                                    ) -> float:
    discount = 0
    final_price = 0
    
    if price > 5000:
        discount += 3
    elif price > 15000:
        discount += 5
    elif price > 20000:
        discount += 7
    elif price > 30000:
        discount += 10
    
    if discount_card == 1:
        discount += 5
    
    if holiday == 1:
        discount += 3
    
    if discount > 15:
        final_price = price * 0.85
    else:
        final_price = price * (1 - discount/100)

    return round(float(final_price))


print(calculating_price_with_discount(float(input('Введите цену: ')),
                                      int(input('Есть ли скидочная карта? (1 - да, 0 - нет) ')),
                                      int(input('Праздничный ли день ? (1 - да, 0 - нет) '))))