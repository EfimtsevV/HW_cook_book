class Cook_book:
    def __init__(self):
        self.cook_book = {}
    def parse_recipes(self, file_path):
        with open(file_path, encoding='utf-8') as file:
            while True:
                dish_name = file.readline().strip()
                if not dish_name:
                    break
                ingredient_count = int(file.readline().strip())
                ingredients = []
                for _ in range(ingredient_count):
                    ingredient_data = file.readline().strip().split(' | ')
                    ingredient_name, quantity, measure = ingredient_data
                    ingredients.append({
                        'ingredient_name': ingredient_name,
                        'quantity': int(quantity),
                        'measure': measure
                    })
                self.cook_book[dish_name] = ingredients
                file.readline()  # Read the blank line separating the next dish
        return self.cook_book
    
    def get_shop_list_by_dishes(self, dishes: list, person_count: int):
        shop_list = {}
        for dish in dishes:
            for ingredient in self.cook_book[dish]:
                if ingredient['ingredient_name'] not in shop_list:
                    shop_list[ingredient['ingredient_name']] = {'quantity': ingredient['quantity'] * person_count, 'measure': ingredient['measure']}
                else:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
        return shop_list