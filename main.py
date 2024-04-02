
def create_cook_book(file):
    cook_book = {}
    cook = None
    for line in file:
        if '|' not in line and not line.isdigit() and line:
            cook_book[line] = []
            cook = line
        if '|' in line:
            line = line.split('|')
            cook_book[cook].append({'ingredient_name': line[0], 'quantity': line[1], 'measure': line[2]})
    return cook_book


with open('recipes.txt') as f:
    data = f.read().splitlines()
    book = create_cook_book(data)
    f.close()

print(book)
