from src.Classes import Cook_book

cook_book_1 = Cook_book()
 
# Задание 1 - создание словаря с ингридиентами

All_ingredients = (cook_book_1.parse_recipes('recipes.txt'))

# Задание 2 - создание словаря с ингридиентами и количеством гостей

shop_list = cook_book_1.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

