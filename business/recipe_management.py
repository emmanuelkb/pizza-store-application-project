from business.models import Ingredient, PizzaRecipe
from pizza_store_repository import PizzaRecipeRepository
from typing import Optional

class RecipeManagement:
    def __init__(self) -> None:
        self.__repository = PizzaRecipeRepository()
        self.__recipes:list[PizzaRecipe] = []
        self.load_recipes()

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self) -> PizzaRecipe:
        if self.__index >= len(self.__recipes) - 1:
            raise StopIteration()
        self.__index += 1
        return self.__recipes[self.__index]

    def recipes(self):
        items = []
        for item in self:
            items.append(item)
        return items

    def load_recipes(self) -> None:
        try:
            self.__recipes = self.__repository.load_pizza_recipes()
        except Exception as e:
            print(f"Error loading recipes: {e}")

    def save_recipes(self) -> None:
        try:
            self.__repository.save_recipes(self.__recipes)
        except Exception as e:
            print(f"Error saving recipes: {e}")

    def add_recipe(self, recipe: PizzaRecipe) -> None:
        try:
            self.__recipes.append(recipe)
            self.save_recipes()
            print(f"Successfully added recipe: {recipe.name}")
        except Exception as e:
            print(f"Error adding recipe: {e}")

    def remove_recipe(self, recipe_name: str) -> None:
        try:
            found = False
            for i in range(len(self.__recipes)):
                if self.__recipes[i].name == recipe_name:
                    self.__recipes.pop(i)
                    self.save_recipes()
                    print(f"Successfully removed recipe: {recipe_name}")
                    found = True
                    break
            if not found:
                print(f"Recipe not found: {recipe_name}")
        except Exception as e:
            print(f"Error removing recipe: {e}")

    def update_recipe(self, recipe_name: str, new_ingredients: dict[str, float]) -> None:
        try:
            recipe = self.get_recipe_by_name(recipe_name)
            if recipe:
                recipe.ingredients.clear()
                for ing_name, quantity in new_ingredients.items():
                    ingredient = Ingredient(ing_name, quantity, "units", 0)
                    recipe.add_ingredient(ingredient)
                self.save_recipes()
                print(f"Successfully updated recipe: {recipe_name}")
            else:
                print(f"Recipe not found: {recipe_name}")
        except Exception as e:
            print(f"Error updating recipe: {e}")

    def get_recipe_by_name(self, name: str) -> Optional[PizzaRecipe]:
        for recipe in self.__recipes:
            if recipe.name == name:
                return recipe
        return None

    def list_recipes(self) -> None:
        print("\n==== AVAILABLE RECIPES ====")
        if not self.__recipes:
            print("No recipes available")
            return
        for recipe in self.__recipes:
            print(recipe)
