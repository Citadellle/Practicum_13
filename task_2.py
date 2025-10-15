def Fibonacci_sequence(n: int) -> None:
    e_0, e_1 = 0, 1
    string = []

    for _ in range(n):
        string.append(e_1)
        e_0, e_1 = e_1, e_1 + e_0
    
    print(*string, sep = ', ')


Fibonacci_sequence(int(input()))