def multiples_for_a_and_b(a: int,
                          b: int,
                          n: int
                          ) -> None:
    for number in range(1, n+1):
        if number % a == 0 and number % b == 0:
            print(number)


multiples_for_a_and_b(int(input('Введите число A: ')),
                      int(input('Введите число B: ')),
                      int(input('Введите число N: ')))