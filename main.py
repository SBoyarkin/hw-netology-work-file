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
