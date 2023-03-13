#Задача 1
with open("рецепты.txt") as file:
    cook_book = {}
    for line in file:
        name_food = line.strip()
        n = int(file.readline())
        ingredient_list = []
        for i in range(n):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(" | ")
            ingredient_list.append({"ingredient_name": ingredient_name, "quantity": quantity,  "measure": measure})
        cook_book[name_food] = ingredient_list
        file.readline()

#Задача 2
def get_shop_list_by_dishes(dishes, person_count):
    ingredient_dict = {}
    ingredients = []
    for food in dishes:
        ingredients = ingredients + cook_book[food]
    for ingred in ingredients:
        if ingred["ingredient_name"] in ingredient_dict:
            ingredient_dict[ingredient_name]["quantity"] += int(ingred["quantity"]) * person_count
        else:
            ingredient_dict[ingred["ingredient_name"]] = {"quantity": int(ingred["quantity"]) * person_count, "measure": ingred["measure"]}
    print(ingredient_dict)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

#Задача 3
catalog = ["f1.txt", "f2.txt", "f3.txt"]
edited_catalog = []
lines = []

while len(catalog) > 0:
    smallest_file = catalog[0]
    for f1 in catalog:
        with open(f1) as file1:
            with open(smallest_file) as file2:
                if len(file1.readlines()) <= len(file2.readlines()):
                    smallest_file = f1
    edited_catalog.append(smallest_file)
    catalog.remove(smallest_file)
sfg = []
with open("f4.txt", "w") as f3:
    for i in edited_catalog:
        with open(i, "r") as file:
            sfg = file.readlines()
            sfg[-1] += "\n"
            for n in sfg:
                f3.write(n)
with open("f4.txt") as f:
    print(f.readlines())