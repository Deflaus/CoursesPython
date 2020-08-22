def dict_of_dishes():
    lines = []
    cook_book = {}
    i = 0

    with open('recipes.txt', 'r') as f:
        for line in f:
            # переписываем файл в список для удобства работы
            lines.append(line.rstrip('\n'))

    for element in lines:
        if element.isdigit():
            # задаем ключи-названия блюд в словарь
            cook_book[lines[i - 1]] = ''
        # количество строк в списке рецептов
        i += 1

    str_of_count_of_ingr = 1  # строка с количеством ингридиентов

    for dish in cook_book:
        ingr_quan_meas_list = []
        num_of_str = str_of_count_of_ingr + 1  # номер строки
        for i in range(0, int(lines[str_of_count_of_ingr])):
            ingridients_dict = {}
            list_of_items_of_ingr = lines[num_of_str].split(' | ')
            num_of_str += 1
            ingridients_dict = {'ingridient_name': list_of_items_of_ingr[0],
                'quantity': int(list_of_items_of_ingr[1]),
                'measure': list_of_items_of_ingr[2]}
            # список, в который собираем ингредиенты одного блюда
            ingr_quan_meas_list.append(ingridients_dict)
        cook_book[dish] = ingr_quan_meas_list
        str_of_count_of_ingr += num_of_str + 1
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = dict_of_dishes()
    shop_dict = {}
    for recipe in dishes:
        for ingridients_dict in cook_book[recipe]:
            if ingridients_dict['ingridient_name'] not in shop_dict.keys():
                shop_dict[ingridients_dict['ingridient_name']] = {
                    'measure': ingridients_dict['measure'],
                    'quantity': ingridients_dict['quantity'] * person_count,
                }
            else:
                shop_dict[ingridients_dict['ingridient_name']]['quantity'] += ingridients_dict['quantity'] * person_count
    return shop_dict

def main():
    print('Решение задачи №1')
    print(dict_of_dishes())

    print('Решение Задачи №2')
    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2
    print(get_shop_list_by_dishes(dishes, person_count))


if __name__ == "__main__":
    main()
