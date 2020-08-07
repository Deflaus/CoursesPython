class Animals:
    weight = 0
    name = ''
    nickname = ''
    voice = ''
    eaten = False

    def __init__(self, weight, name, voice):
        self.weight = weight
        self.name = name
        self.voice = voice
        self.eaten = False

    def feed(self):
        self.eaten = True
        print('Покормили: {}'.format(self.name))

    def say(self):
        print('{} сказал(а) {}'.format(self.name, self.voice))


# класс животных дающих молоко
class Milk_animals(Animals):
    milked = False

    def milk(self):
        self.milked = True
        print('Подоили: {}'.format(self.name))


# класс животных дающих шерсть
class Wool_animals(Animals):
    have_cut = False

    def cut(self):
        self.have_cut = True
        print('Постригли шерсть у: {}'.format(self.name))


# класс птиц
class Birds(Animals):
    egg_got = False

    def get_eggs(self):
        self.egg_got = True
        print('Собрали яйца у: {}'.format(self.name))


milk_animal_list = []
bird_list = []
wool_animal_list = []
animal_list = []

# создаем экземпляр для каждого животного
goose1 = Birds(10, 'Гусь1', 'Га-га')
bird_list.append(goose1)

goose2 = Birds(10, 'Гусь2', 'Га-га')
bird_list.append(goose2)

cow = Milk_animals(400, 'Корова', 'Мууу')
milk_animal_list.append(cow)

sheep1 = Wool_animals(50, 'Овца', 'Бэээ')
wool_animal_list.append(sheep1)

sheep2 = Wool_animals(50, 'Овца', 'Бэээ')
wool_animal_list.append(sheep2)

chicken1 = Birds(5, 'Курица', 'Ко-ко')
bird_list.append(chicken1)

chicken2 = Birds(4, 'Курица', 'Ко-ко')
bird_list.append(chicken2)

goat1 = Wool_animals(30, 'Коза', 'Мэээ')
milk_animal_list.append(goat1)

goat2 = Wool_animals(30, 'Коза', 'Мэээ')
milk_animal_list.append(goat2)

duck = Birds(6, 'Утка', 'Кря-кря')
bird_list.append(duck)

for bird in bird_list:
    Animals.feed(bird)
    Birds.get_eggs(bird)
    Animals.say(bird)

    animal_list.append(bird)

for milk in milk_animal_list:
    Animals.feed(milk)
    Milk_animals.milk(milk)
    Animals.say(milk)

    animal_list.append(milk)

for wool in wool_animal_list:
    Animals.feed(wool)
    Wool_animals.cut(wool)
    Animals.say(wool)

    animal_list.append(wool)

weight = 0
max_weight = 0

for animal in animal_list:
    weight += animal.weight
    if max_weight < animal.weight:
        max_weight = animal.weight
        max_weight_animal = animal

print('Общий вес {} кг'.format(weight))
print('Самый большой вес у животного {} '.format(max_weight_animal.name))
