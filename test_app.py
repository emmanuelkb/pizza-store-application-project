from uuid import uuid4
from datetime import datetime, timedelta
from business.pizza_store import PizzaStore
from business.models import (
    Ingredient, PizzaRecipe, PizzaMenuItem, PizzaSize, PizzaCategory,
    SideCategory, SideMenuItem, Order, CustomPizza, OrderStatus,
    PizzaOrderItem, SideOrderItem
)

class PizzaStoreTestApp:
    def __init__(self):
        self.__store = PizzaStore()

    def main(self):
        ingredients = [
            Ingredient("Dough", 100, "kg", 20),
            Ingredient("Tomato Sauce", 50, "liters", 10),
            Ingredient("Mozzarella", 80, "kg", 15),
            Ingredient("Pepperoni", 30, "kg", 5),
            Ingredient("Mushrooms", 25, "kg", 5),
            Ingredient("Onions", 20, "kg", 4),
            Ingredient("Bell Peppers", 15, "kg", 3),
            Ingredient("Olives", 10, "kg", 2)
        ]
        for ingredient in ingredients:
            self.__store.inventory_mgr.add_ingredient(ingredient)
        print("\nIngredients added successfully!")

        margherita_ingredients = [
            Ingredient("Dough", 0.5, "kg", 0),
            Ingredient("Tomato Sauce", 0.2, "liters", 0),
            Ingredient("Mozzarella", 0.3, "kg", 0)
        ]
        pepperoni_ingredients = [
            Ingredient("Dough", 0.5, "kg", 0),
            Ingredient("Tomato Sauce", 0.2, "liters", 0),
            Ingredient("Mozzarella", 0.3, "kg", 0),
            Ingredient("Pepperoni", 0.2, "kg", 0)
        ]
        veggie_ingredients = [
            Ingredient("Dough", 0.5, "kg", 0),
            Ingredient("Tomato Sauce", 0.2, "liters", 0),
            Ingredient("Mozzarella", 0.3, "kg", 0),
            Ingredient("Mushrooms", 0.15, "kg", 0),
            Ingredient("Onions", 0.1, "kg", 0),
            Ingredient("Bell Peppers", 0.15, "kg", 0)
        ]

        recipes = [
            PizzaRecipe("Margherita", margherita_ingredients),
            PizzaRecipe("Pepperoni", pepperoni_ingredients),
            PizzaRecipe("Vegetarian", veggie_ingredients)
        ]
        
        for recipe in recipes:
            self.__store.recipe_mgt.add_recipe(recipe)
        print("Recipes added successfully!")

        margherita_recipe = self.__store.recipe_mgt.get_recipe_by_name("Margherita")
        pepperoni_recipe = self.__store.recipe_mgt.get_recipe_by_name("Pepperoni")
        veggie_recipe = self.__store.recipe_mgt.get_recipe_by_name("Vegetarian")

        if margherita_recipe and pepperoni_recipe and veggie_recipe:
            menu_items = [
                PizzaMenuItem(
                    "Classic Margherita", 
                    "Fresh tomato sauce, mozzarella, and basil", 
                    PizzaSize.MEDIUM, 
                    12.99, 
                    PizzaCategory.VEGETARIAN,
                    margherita_recipe
                ),
                PizzaMenuItem(
                    "Pepperoni Feast", 
                    " added with pepperoni and cheese", 
                    PizzaSize.LARGE, 
                    15.99, 
                    PizzaCategory.MEAT,
                    pepperoni_recipe
                ),
                PizzaMenuItem(
                    "Veggie Supreme", 
                    "Fresh vegetables on a crispy base", 
                    PizzaSize.MEDIUM, 
                    14.99, 
                    PizzaCategory.VEGETARIAN,
                    veggie_recipe
                )
            ]
            
            for item in menu_items:
                self.__store.menu_mgt.add_menu_item(item)
            print("Menu items added successfully!")
        else:
            print("Error: Could not find one or more recipes")

        sides = [
            SideMenuItem("Caesar Salad", "Fresh romaine lettuce with caesar dressing", 6.99, SideCategory.SALAD),
            SideMenuItem("Garlic Bread", "Freshly baked with garlic butter", 4.99, SideCategory.APPETIZER),
            SideMenuItem("Coke", "500ml", 2.99, SideCategory.BEVERAGE),
            SideMenuItem("Chocolate Brownie", "Rich and fudgy", 5.99, SideCategory.DESSERT)
        ]
        
        for side in sides:
            self.__store.side_mgt.add_side(side)
        print("Side items added successfully!")
        order_id_1 = str(uuid4())
        order1 = Order("John Doe", "555-0123", datetime.now() + timedelta(hours=1),order_id_1 )
        margherita = self.__store.menu_mgt.get_menu_item_by_name("Classic Margherita")
        
        salad = None
        for side in self.__store.side_mgt.sides():
            if side.name == "Caesar Salad":
                salad = side
                break
        if margherita and salad:        
            order1.add_item(PizzaOrderItem(1, margherita))
            order1.add_item(SideOrderItem(1, salad))

        order_id_2 = str(uuid4())
        order2 = Order("Jane Smith", "555-0456", datetime.now() + timedelta(hours=2), order_id_2)
        custom_pizza = CustomPizza(PizzaSize.LARGE, 14.00)
        custom_pizza.add_topping("Pepperoni", 2)
        custom_pizza.add_topping("Mushrooms", 1)
        custom_pizza.add_topping("Extra Cheese", 1)
        order2.add_item(PizzaOrderItem(1, custom_pizza))

        self.__store.order_mgt.create_order(order1)
        self.__store.order_mgt.create_order(order2)
        print("Orders created successfully!")

        self.__store.order_mgt.generate_kitchen_slip(order_id_1)
        self.__store.order_mgt.generate_kitchen_slip(order_id_2)
        self.__store.order_mgt.list_orders(OrderStatus.NEW)
        

if __name__ == "__main__":
    app = PizzaStoreTestApp()
    app.main()