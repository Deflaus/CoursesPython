boys = list(map(str, input(
    "Введите имена мальчиков через пробел(или нажмите enter, чтобы использовать значения по умолчанию): ").split()))
girls = list(map(str, input(
    "Введите имена девочек через пробел(или нажмите enter, чтобы использовать значения по умолчанию): ").split()))

if len(boys) == 0:
    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
if len(girls) == 0:
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    boys.sort()
    girls.sort()
    print('Идеальные пары:')
    for boy, girl in zip(boys, girls):
        print(boy, 'и', girl)
else:
    print('Количество мальчиков и девочек не равное, знакомить никого не будем, кто-то может остаться без пары')