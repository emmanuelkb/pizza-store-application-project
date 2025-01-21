from business.models import Ingredient
from pizza_store_repository import IngredientRepository

class InventoryManager:
    def __init__(self) -> None:
        self.__repository = IngredientRepository()
        self.__ingredients:dict = {}
        self.load_inventory()
        

    def load_inventory(self) -> None:
        try:
            ingredient_list = self.__repository.load_ingredients()
            for ingredient in ingredient_list:
                self.__ingredients[ingredient.name] = ingredient
        except Exception as e:
            print(f"Error loading inventory: {e}")

    def save_inventory(self) -> None:
        try:
            self.__repository.save_ingredients(list(self.__ingredients.values()))
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def add_ingredient(self, ingredient: Ingredient) -> None:
        try:
            if ingredient.name in self.__ingredients:
                current_ingredient = self.__ingredients[ingredient.name]
                current_ingredient.quantity += ingredient.quantity
                print(f"Updated quantity of {ingredient.name}. New quantity: {current_ingredient.quantity} {current_ingredient.unit}")
            else:
                self.__ingredients[ingredient.name] = ingredient
                print(f"Successfully added {ingredient.name} to inventory")
        except Exception as e:
            print(f"Error adding ingredient: {e}")

    def remove_ingredient(self, ingredient_name: str, quantity: float) -> None:
        try:
            if ingredient_name in self.__ingredients:
                current_qty = self.__ingredients[ingredient_name].quantity
                if current_qty >= quantity:
                    self.__ingredients[ingredient_name].quantity = current_qty - quantity
                    self.save_inventory()
                    print(f"Successfully removed {quantity} {self.__ingredients[ingredient_name].unit} of {ingredient_name}")
                else:
                    print(f"Insufficient quantity. Available: {current_qty} {self.__ingredients[ingredient_name].unit}")
            else:
                print(f"Ingredient {ingredient_name} not found in inventory")
        except Exception as e:
            print(f"Error removing ingredient: {e}")

    def use_ingredient(self, recipe_ingredients: dict[str, float]) -> None:
        try:
            can_make = True
            for ing_name, qty_needed in recipe_ingredients.items():
                if ing_name not in self.__ingredients:
                    print(f"Missing ingredient: {ing_name}")
                    can_make = False
                elif self.__ingredients[ing_name].quantity < qty_needed:
                    print(f"Insufficient {ing_name}. Need {qty_needed}, have {self.__ingredients[ing_name].quantity}")
                    can_make = False
            if can_make:
                for ing_name, qty_needed in recipe_ingredients.items():
                    self.remove_ingredient(ing_name, qty_needed)
                print("Successfully used ingredients")
            else:
                print("insufficient ingredients")
        except Exception as e:
            print(f"Error using ingredients: {e}")

    def check_reorder_levels(self) -> None:
        print("\n==== INVENTORY REORDER ALERT ====")
        found_low = False
        for name, ingredient in self.__ingredients.items():
            if ingredient.quantity <= ingredient.reorder_level:
                print(f"Low Stock: {name} - Current: {ingredient.quantity} {ingredient.unit}, Reorder Level: {ingredient.reorder_level}")
                found_low = True
        if not found_low:
            print("All ingredients above reorder levels")

    def print_inventory(self) -> None:
        print("\n==== CURRENT INVENTORY ====")
        if not self.__ingredients:
            print("No ingredients in inventory")
            return
        for name, ingredient in self.__ingredients.items():
            print(f"{name}: {ingredient.quantity} {ingredient.unit}")
