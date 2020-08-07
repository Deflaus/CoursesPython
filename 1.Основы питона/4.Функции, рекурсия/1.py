def fact(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


try:
    n = int(input("Введите число n:"))
except ValueError:
    print("Некорректные данные")
else:
    print(fact(n))
