class Ingredient:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price  # стоимость за 100гр

    @property
    def cost(self):
        n = (self.weight / 100) * self.price
        return n


class Pizza:
    def __init__(self, name, ingredients=None):
        self.name = name
        # в пицца передается объект <__main__.Ingredient object at 0x10ad3bcb0> из ингредиентов
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients

    @property
    def cost(self):

        total_cost = sum(ingredient.cost for ingredient in self.ingredients)  # Сумма стоимости ингредиентов
        return total_cost + 100  # Добавляем 100 рублей за основу


chicken = Ingredient('chicken', 200, 80)
mozzarella = Ingredient('mozzarella', 300, 110)
sauce_bbq = Ingredient('sauce bbq', 150, 70)
red_onion = Ingredient('red onion', 150, 50)
barbecue = Pizza('BBQ', [chicken, mozzarella, sauce_bbq, red_onion])

print('Стоимость пиццы BBQ', barbecue.cost)
print(chicken)
