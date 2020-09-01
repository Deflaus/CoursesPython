def my_gen(path):
    with open(path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            yield line


if __name__ == "__main__":
    my_gen = my_gen('example.txt')
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
