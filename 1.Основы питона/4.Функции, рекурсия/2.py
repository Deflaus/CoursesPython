def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


try:
    n = int(input("Введите число n:"))
except ValueError:
    print("Некорректные данные")
else:
    print(fibonacci(n))
