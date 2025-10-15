def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number**0.5 + 1)):
        if number % i == 0:
            return False
    return True


def prime_numbers_up_to_N(n: int) -> None:
    for number in range(2, n + 1):
        if is_prime(number):
            print(number)


prime_numbers_up_to_N(int(input('Введите число N: ')))