def numbers_in_range(a: int,
                     b: int) -> None:
    if a > b:
        a, b = b, a
    
    lots_numbers = '13489'

    for number in range(a, b + 1):
        flag = True
        for i in str(number):
            if i not in lots_numbers:
                flag = False
                break

        if flag == True:
            print(number)


numbers_in_range(int(input('Введите число A: ')),
                 int(input('Введите число B: ')))