print('Задача №1')

def create_cook_book(file):
    cook_book = {}
    cook = None
    for line in file:
        if '|' not in line and not line.isdigit() and line:
            cook_book[line] = []
            cook = line
        if '|' in line:
            line = line.split('|')
            cook_book[cook].append({'ingredient_name': line[0].strip(),
                                    'quantity': int(line[1].strip()), 'measure': line[2].strip()})

    return cook_book


with open('recipes.txt') as f:
    data = f.read().splitlines()
    book = create_cook_book(data)
    f.close()

print(book)
print()

print('Задча №2')


def get_shop_list_by_dishes(dishes, person_count):
    dish_list = {}
    for dish in dishes:
        ingridiens = book.get(dish)
        for ingridien in ingridiens:
            ingredient_name = ingridien.get('ingredient_name')
            if dish_list.get(ingredient_name):
                dish_list[ingredient_name] = {'measure': ingridien.get('measure'),
                                              'quantity': dish_list[ingredient_name].get('quantity') + ingridien.get('quantity') * person_count}
            else:
                dish_list[ingredient_name] = {'measure': ingridien.get('measure'),
                                              'quantity': ingridien.get('quantity') * person_count}
    print(dish_list)


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print()

print('Задча №3')
def open_file(file_name_list):
    data_list = []
    for file in file_name_list:
        with open(file) as f:
            data = f.read().splitlines()
            f.close()
            data_list.append({file: data})
    return sort_string(data_list)

def sort_string(list_dict):
    return sorted(list_dict, key=lambda x: len(list(x.values())[0]))



def write_data(data):
    for i in data:
        for key, item in i.items():

            with open('result.txt', 'a+') as f:
                print(key, file=f, end='\n')
                print(len(item), file=f, end='\n')
                for string in  item:
                    print(string, file=f, end='\n')
            f.close()


file_name = ['1.txt', '2.txt', '3.txt',]

file_dict = open_file(file_name)

write_data(file_dict)
# print(file_dict)

