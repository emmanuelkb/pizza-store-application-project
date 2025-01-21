import json
from typing import Any
from business.models import Ingredient, PizzaMenuItem,PizzaRecipe, PizzaSize, PizzaCategory, SideMenuItem, SideCategory, Order, OrderStatus,PizzaOrderItem,CustomPizza, SideOrderItem
from datetime import datetime

class BaseRepository:
    def __init__(self, filename: str):
        self.__filename = filename
    
    def save_data(self, data: list[dict[str, Any]]):
        with open(f"data_files/{self.__filename}", 'w') as file:
            json.dump(data, file, indent=4)
    
    def load_data(self) -> list[dict[str, Any]]:
        try:
            with open(f"data_files/{self.__filename}", 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []


class IngredientRepository(BaseRepository):
    def __init__(self):
        super().__init__("ingredients.json")
    
    def save_ingredients(self, ingredients: list[Ingredient]) -> None:
        data = []
        for ingredient in ingredients:
            ingredient_dict = {
                "name": ingredient.name,
                "quantity": ingredient.quantity,
                "unit": ingredient.unit,
                "reorder_level": ingredient.reorder_level
            }
            data.append(ingredient_dict)
        self.save_data(data)
    
    def load_ingredients(self) -> list[Ingredient]:
        data = self.load_data()
        ingredients = []
        for item in data:
            ingredient = Ingredient(
                name=item["name"],
                quantity=item["quantity"],
                unit=item["unit"],
                reorder_level=item["reorder_level"]
            )
            ingredients.append(ingredient)
        return ingredients


class PizzaMenuRepository(BaseRepository):
    def __init__(self):
        super().__init__("menu.json")
    
    def save_menu_items(self, pizzas: list[PizzaMenuItem]) -> None:
        data = []
        for pizza in pizzas:
            pizza_dict = {
                "name": pizza.name,
                "description": pizza.description,
                "size": pizza.size.value,
                "price": pizza.price,
                "category": pizza.category.value,
                "recipe": {
                    "name": pizza.recipe.name,
                    "ingredients": []
                }
            }
            
            for ingredient in pizza.recipe.ingredients:
                ingredient_dict = {
                    "name": ingredient.name,
                    "quantity": ingredient.quantity,
                    "unit": ingredient.unit,
                    "reorder_level": ingredient.reorder_level
                }
                pizza_dict["recipe"]["ingredients"].append(ingredient_dict)
            
            data.append(pizza_dict)
        self.save_data(data)
    
    def load_menu(self) -> list[PizzaMenuItem]:
        data = self.load_data()
        pizzas = []
        for item in data:
            ingredients = []
            for ing_data in item["recipe"]["ingredients"]:
                ingredient = Ingredient(
                    name=ing_data["name"],
                    quantity=ing_data["quantity"],
                    unit=ing_data["unit"],
                    reorder_level=ing_data["reorder_level"]
                )
                ingredients.append(ingredient)            
            recipe = PizzaRecipe(
                name=item["recipe"]["name"],
                ingredients=ingredients
            )      
            pizza = PizzaMenuItem(
                name=item["name"],
                description=item["description"],
                size=PizzaSize(item["size"]),
                price=item["price"],
                category=PizzaCategory(item["category"]),
                recipe=recipe
            )
            pizzas.append(pizza)
        return pizzas


class PizzaRecipeRepository(BaseRepository):
    def __init__(self):
        super().__init__("recipes.json")
    
    def save_recipes(self, recipes: list[PizzaRecipe]) -> None:
        data = []
        for recipe in recipes:
            recipe_dict = {
                "name": recipe.name,
                "ingredients": []
            }
            for ingredient in recipe.ingredients:
                ingredient_dict = {
                    "name": ingredient.name,
                    "quantity": ingredient.quantity,
                    "unit": ingredient.unit,
                    "reorder_level": ingredient.reorder_level
                }
                recipe_dict["ingredients"].append(ingredient_dict)
            data.append(recipe_dict)
        self.save_data(data)

    def load_pizza_recipes(self) -> list[PizzaRecipe]:
        data = self.load_data()
        recipes = []
        for item in data:
            ingredients = []
            for ing_data in item["ingredients"]:
                ingredient = Ingredient(
                    name=ing_data["name"],
                    quantity=ing_data["quantity"],
                    unit=ing_data["unit"],
                    reorder_level=ing_data["reorder_level"]
                )
                ingredients.append(ingredient)
            recipe = PizzaRecipe(
                name=item["name"],
                ingredients=ingredients
            )
            recipes.append(recipe)
        return recipes
    
class SideMenuRepository(BaseRepository):
    def __init__(self):
        super().__init__("sides.json")
    
    def save_sides(self, sides: list[SideMenuItem]) -> None:
        data = []
        for side in sides:
            data.append(side.to_dict())
        self.save_data(data)
    
    def load_sides(self) -> list[SideMenuItem]:
        data = self.load_data()
        sides = []
        for item in data:
            side = SideMenuItem(
                name=item["name"],
                description=item["description"],
                price=item["price"],
                category=SideCategory(item["category"])
            )
            sides.append(side)
        return sides

class OrderRepository(BaseRepository):
    def __init__(self):
        super().__init__("orders.json")
    
    def save_orders(self, orders: list[Order]) -> None:
        data = []
        for order in orders:
            data.append(order.to_dict())
        self.save_data(data)


    def load_orders(self) -> list[Order]:
        data = self.load_data()
        orders = []
        for item in data:
            order = Order(
                customer_name=item["customer_name"],
                phone=item["phone"],
                delivery_time=datetime.fromisoformat(item["delivery_time"]),
                order_id=item["order_id"]
            )
            order.status = OrderStatus(item["status"])           
            for order_item in item["items"]:
                quantity = order_item["quantity"]
                if order_item["type"] == "pizza":
                    pizza_data = order_item["item"]
                    if "name" in pizza_data:
                        recipe_data = pizza_data["recipe"]
                        ingredients = []
                        for ing_data in recipe_data["ingredients"]:
                            ingredient = Ingredient(
                                name=ing_data["name"],
                                quantity=ing_data["quantity"],
                                unit=ing_data["unit"],
                                reorder_level=ing_data["reorder_level"]
                            )
                            ingredients.append(ingredient)
                        recipe = PizzaRecipe(
                            name=recipe_data["name"],
                            ingredients=ingredients
                        )              
                        pizza = PizzaMenuItem(
                            name=pizza_data["name"],
                            description=pizza_data["description"],
                            size=PizzaSize(pizza_data["size"]),
                            price=pizza_data["price"],
                            category=PizzaCategory(pizza_data["category"]),
                            recipe=recipe
                        )
                        order.add_item(PizzaOrderItem(quantity, pizza))
                    else:
                        custom_pizza = CustomPizza(
                            size=PizzaSize(pizza_data["size"]),
                            base_price=pizza_data["base_price"]
                        )       
                        for topping_name, topping_qty in pizza_data["toppings"].items():
                            custom_pizza.add_topping(topping_name, topping_qty)        
                        order.add_item(PizzaOrderItem(quantity, custom_pizza))
                elif order_item["type"] == "side":
                    side_data = order_item["item"]
                    side = SideMenuItem(
                        name=side_data["name"],
                        description=side_data["description"],
                        price=side_data["price"],
                        category=SideCategory(side_data["category"])
                    )
                    order.add_item(SideOrderItem(quantity, side))
            orders.append(order)
        return orders
    

# def main():
#     ing = IngredientRepository()
#     print(ing.load_ingredients())
#     menu = PizzaMenuRepository()
#     print(menu.load_menu())
#     recipe = PizzaRecipeRepository()
#     print(recipe.load_pizza_recipes())

# if __name__ == "__main__":
#     main()

