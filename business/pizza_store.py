from business.models import *
from pizza_store_repository import *
from datetime import datetime
from business.inventory_management import InventoryManager
from business.menu_management import MenuManagement
from business.recipe_management import RecipeManagement
from business.side_management import SideManagement
from business.order_managment import OrderManagement
from uuid import uuid4

class PizzaStore:
    def __init__(self):
        self.__inventory_mgr = InventoryManager()
        self.__recipe_mgt = RecipeManagement()
        self.__menu_mgt = MenuManagement()
        self.__side_mgt = SideManagement()
        self.__order_mgt = OrderManagement()

    def process_inventory_menu(self, show_menu) -> None:
        while True:
            show_menu()
            try:
                option = int(input("Enter option: "))
                if option == 1:
                    name = input("Enter ingredient name: ")
                    quantity = float(input("Enter quantity: "))
                    unit = input("Enter unit (e.g., grams, ml): ")
                    reorder_level = int(input("Enter reorder level: "))
                    ingredient = Ingredient(name, quantity, unit, reorder_level)
                    self.__inventory_mgr.add_ingredient(ingredient)
                elif option == 2:
                    name = input("Enter ingredient name: ")
                    quantity = float(input("Enter quantity to remove: "))
                    self.__inventory_mgr.remove_ingredient(name, quantity)
                elif option == 3:
                    recipe_ingredients = {}
                    while True:
                        name = input("Enter ingredient name (or '1' to finish): ")
                        if name == '1':
                            break
                        quantity = float(input("Enter quantity needed: "))
                        recipe_ingredients[name] = quantity
                    self.__inventory_mgr.use_ingredient(recipe_ingredients)
                elif option == 4:
                    self.__inventory_mgr.check_reorder_levels()
                elif option == 5:
                    self.__inventory_mgr.print_inventory()
                elif option == 6:
                    break
                else:
                    print("Invalid option.")
            except ValueError:
                print("Please enter valid values.")

    def process_recipe_menu(self, show_menu) -> None:
        while True:
            show_menu()
            try:
                option = int(input("Enter option: "))
                if option == 1:
                    name = input("Enter recipe name: ")
                    ingredients = []
                    while True:
                        ing_name = input("Enter ingredient name (or '1' to finish): ")
                        if ing_name == '1':
                            break
                        quantity = float(input("Enter quantity: "))
                        unit = input("Enter unit: ")
                        reorder_level = int(input("Enter reorder level: "))
                        ingredient = Ingredient(ing_name, quantity, unit, reorder_level)
                        ingredients.append(ingredient)
                    recipe = PizzaRecipe(name, ingredients)
                    self.__recipe_mgt.add_recipe(recipe)
                elif option == 2:
                    name = input("Enter recipe name to remove: ")
                    self.__recipe_mgt.remove_recipe(name)
                elif option == 3:
                    name = input("Enter recipe name to update: ")
                    new_ingredients = {}
                    while True:
                        ing_name = input("Enter ingredient name (or '1' to finish): ")
                        if ing_name.lower() == '1':
                            break
                        quantity = float(input("Enter quantity: "))
                        new_ingredients[ing_name] = quantity
                    self.__recipe_mgt.update_recipe(name, new_ingredients)
                elif option == 4:
                    self.__recipe_mgt.list_recipes()
                elif option == 5:
                    break
                else:
                    print("Invalid option.")
            except ValueError:
                print("Please enter valid values.")

    def process_menu_item_menu(self, show_menu) -> None:
        while True:
            show_menu()
            try:
                option = int(input("Enter option: "))
                if option == 1:
                    name = input("Enter menu item name: ")
                    description = input("Enter description: ")
                    print("\nAvailable sizes:")
                    for size in PizzaSize:
                        print(f"- {size.name}")
                    size = PizzaSize[input("Enter size: ").upper()]
                    price = float(input("Enter price: "))
                    print("\nAvailable categories:")
                    for category in PizzaCategory:
                        print(f"- {category.name}")
                    category = PizzaCategory[input("Enter category: ").upper()]
                    recipe_name = input("Enter recipe name for this item: ")
                    recipe = self.__recipe_mgt.get_recipe_by_name(recipe_name)
                    if recipe:
                        menu_item = PizzaMenuItem(name, description, size, price, category, recipe)
                        self.__menu_mgt.add_menu_item(menu_item)
                    else:
                        print("Recipe not found.")
                elif option == 2:
                    name = input("Enter menu item name to remove: ")
                    self.__menu_mgt.remove_menu_item(name)
                elif option == 3:
                    current_name = input("Enter current menu item name: ")
                    name = input("Enter new menu item name: ")
                    description = input("Enter new description: ")
                    print("\nAvailable sizes:")
                    for size in PizzaSize:
                        print(f"- {size.name}")
                    size = PizzaSize[input("Enter new size: ").upper()]
                    price = float(input("Enter new price: "))
                    print("\nAvailable categories:")
                    for category in PizzaCategory:
                        print(f"- {category.name}")
                    category = PizzaCategory[input("Enter new category: ").upper()]
                    recipe_name = input("Enter recipe name for this item: ")
                    recipe = self.__recipe_mgt.get_recipe_by_name(recipe_name)
                    if recipe:
                        new_menu_item = PizzaMenuItem(name, description, size, price, category, recipe)
                        self.__menu_mgt.update_menu_item(current_name, new_menu_item)
                    else:
                        print("Recipe not found.")
                elif option == 4:
                    print("\nAvailable categories:")
                    for category in PizzaCategory:
                        print(f"- {category.name}")
                    category = PizzaCategory[input("Enter category: ").upper()]
                    items = self.__menu_mgt.get_menu_items_by_category(category)
                    if items:
                        print(f"\nItems in category {category.value}:")
                        for item in items:
                            print(item)
                    else:
                        print(f"No items found in category {category.value}")
                elif option == 5:
                    self.__menu_mgt.list_menu_items()
                elif option == 6:
                    break
                else:
                    print("Invalid option.")
            except (ValueError, KeyError):
                print("Please enter valid values.")

    def process_side_menu(self, show_menu) -> None:
        while True:
            show_menu()
            try:
                option = int(input("Enter option: "))
                if option == 1:
                    name = input("Enter side item name: ")
                    description = input("Enter description: ")
                    price = float(input("Enter price: "))
                    print("\nAvailable categories:")
                    for category in SideCategory:
                        print(f"- {category.name}")
                    category = SideCategory[input("Enter category: ").upper()]
                    side_item = SideMenuItem(name, description, price, category)
                    self.__side_mgt.add_side(side_item)
                elif option == 2:
                    name = input("Enter side item name to remove: ")
                    self.__side_mgt.remove_side(name)
                elif option == 3:
                    print("\nAvailable categories:")
                    for category in SideCategory:
                        print(f"- {category.name}")
                    category = SideCategory[input("Enter category: ").upper()]
                    sides = self.__side_mgt.get_sides_by_category(category)
                    if sides:
                        print(f"\nSide items in category {category.value}:")
                        for side in sides:
                            print(side)
                    else:
                        print(f"No side items found in category {category.value}")
                elif option == 4:
                    self.__side_mgt.list_sides()
                elif option == 5:
                    break
                else:
                    print("Invalid option.")
            except (ValueError, KeyError):
                print("Please enter valid values.")

    def process_order_menu(self, show_menu) -> None:
        while True:
            show_menu()
            try:
                option = int(input("Enter option: "))
                if option == 1:
                    self.create_new_order()
                elif option == 2:
                    order_id = input("Enter order ID: ")
                    print("\nAvailable statuses:")
                    for status in OrderStatus:
                        print(f"- {status.name}")
                    status = OrderStatus[input("Enter new status: ").upper()]
                    self.__order_mgt.update_order_status(order_id, status)
                elif option == 3:
                    print("\nFilter by status (or press Enter for all orders):")
                    for status in OrderStatus:
                        print(f"- {status.name}")
                    status_input = input("Enter status: ").upper()
                    status = OrderStatus[status_input] if status_input else None
                    self.__order_mgt.list_orders(status)
                elif option == 4:
                    order_id = input("Enter order ID: ")
                    self.__order_mgt.generate_kitchen_slip(order_id)
                elif option == 5:
                    break
                else:
                    print("Invalid option.")
            except (ValueError, KeyError):
                print("Please enter valid values.")

    def create_new_order(self) -> None:
        try:
            customer_name = input("Enter customer name: ")
            phone = input("Enter phone number: ")
            delivery_date = input("Enter delivery date (YYYY-MM-DD): ")
            delivery_time = input("Enter delivery time (HH:MM): ")
            delivery_datetime = datetime.strptime(f"{delivery_date} {delivery_time}", "%Y-%m-%d %H:%M")
            order_id = str(uuid4())
            order = Order(customer_name, phone, delivery_datetime,order_id)
            while True:
                print("\nAdd items to order:")
                print("1. Add Standard Pizza")
                print("2. Add Custom Pizza")
                print("3. Add Side Item")
                print("4. Finish Order")
                option = int(input("Enter option: "))
                if option == 1:
                    self.__menu_mgt.list_menu_items()
                    pizza_name = input("Enter pizza name: ")
                    quantity = int(input("Enter quantity: "))
                    menu_item = self.__menu_mgt.get_menu_item_by_name(pizza_name)
                    if menu_item:
                        order.add_item(PizzaOrderItem(quantity, menu_item))
                        print(f"Added {quantity}x {pizza_name} to order")
                    else:
                        print("Pizza not found in menu")
                elif option == 2:
                    print("\nAvailable sizes:")
                    for size in PizzaSize:
                        print(f"- {size.name}")
                    size = PizzaSize[input("Enter size: ").upper()]
                    custom_pizza = CustomPizza(size, 14.00)
                    while True:
                        topping = input("Enter topping (or '1' to finish): ")
                        if topping.lower() == '1':
                            break
                        quantity = int(input("Enter quantity: "))
                        custom_pizza.add_topping(topping, quantity)
                    pizza_quantity = int(input("Enter quantity of this custom pizza: "))
                    order.add_item(PizzaOrderItem(pizza_quantity, custom_pizza))
                elif option == 3:
                    self.__side_mgt.list_sides()
                    side_name = input("Enter side item name: ")
                    quantity = int(input("Enter quantity: "))
                    for side in self.__side_mgt.sides():
                        if side.name == side_name:
                            order.add_item(SideOrderItem(quantity, side))
                            print(f"Added {quantity}x {side_name} to order")
                            break
                    else:
                        print("Side item not found")
                elif option == 4:
                    if not order.items:
                        print("Cannot create empty order")
                        continue
                    self.__order_mgt.create_order(order)
                    print(f"\nOrder total: ${order.calculate_total():.2f}")
                    self.__order_mgt.generate_kitchen_slip(order.order_id)
                    break
                else:
                    print("Invalid option.")
        except ValueError:
            print("Please enter valid values.")
        except Exception as e:
            print(f"Error creating order: {e}")

    def search_recipes(self) -> None:
        print("\n=== RECIPE SEARCH ===")
        recipe_name = input("Enter recipe name to search for: ").lower()
        found = False
        for recipe in self.__recipe_mgt.recipes():
            if recipe_name in recipe.name.lower():
                print(recipe)
                found = True
        if not found:
            print("No recipes found matching your search.")

    @property
    def inventory_mgr(self):
        return self.__inventory_mgr
    
    @property
    def recipe_mgt(self):
        return self.__recipe_mgt
    
    @property
    def menu_mgt(self):
        return self.__menu_mgt
    
    @property
    def side_mgt(self):
        return self.__side_mgt
    
    @property
    def order_mgt(self):
        return self.__order_mgt