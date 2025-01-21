from business.pizza_store import PizzaStore

class PizzaStoreApp:
    def __init__(self):
        self.__store = PizzaStore()

    def show_main_menu(self) -> None:
        print("\n=== PIZZA STORE MANAGEMENT SYSTEM ===")
        print("1. Manage Inventory")
        print("2. Manage Recipes")
        print("3. Manage Menu Items")
        print("4. Manage Side Items")
        print("5. Manage Orders")
        print("6. Search Recipes")
        print("7. Exit")

    def show_inventory_menu(self) -> None:
        print("\n=== INVENTORY MANAGEMENT ===")
        print("1. Add Ingredient")
        print("2. Remove Ingredient")
        print("3. Use Ingredients for Recipe")
        print("4. Check Reorder Levels")
        print("5. View Current Inventory")
        print("6. Back to Main Menu")

    def show_recipe_menu(self) -> None:
        print("\n=== RECIPE MANAGEMENT ===")
        print("1. Add Recipe")
        print("2. Remove Recipe")
        print("3. Update Recipe")
        print("4. View All Recipes")
        print("5. Back to Main Menu")

    def show_menu_item_menu(self) -> None:
        print("\n=== MENU MANAGEMENT ===")
        print("1. Add Menu Item")
        print("2. Remove Menu Item")
        print("3. Update Menu Item")
        print("4. View Menu Items by Category")
        print("5. View All Menu Items")
        print("6. Back to Main Menu")

    def show_side_menu(self) -> None:
        print("\n=== SIDE ITEM MANAGEMENT ===")
        print("1. Add Side Item")
        print("2. Remove Side Item")
        print("3. View Side Items by Category")
        print("4. View All Side Items")
        print("5. Back to Main Menu")

    def show_order_menu(self) -> None:
        print("\n=== ORDER MANAGEMENT ===")
        print("1. Create New Order")
        print("2. Update Order Status")
        print("3. View Orders")
        print("4. Generate Kitchen Slip")
        print("5. Back to Main Menu")

    def process_command(self) -> None:
        while True:
            self.show_main_menu()
            try:
                option = int(input("Enter option: "))
                if option == 1:
                    self.__store.process_inventory_menu(self.show_inventory_menu)
                elif option == 2:
                    self.__store.process_recipe_menu(self.show_recipe_menu)
                elif option == 3:
                    self.__store.process_menu_item_menu(self.show_menu_item_menu)
                elif option == 4:
                    self.__store.process_side_menu(self.show_side_menu)
                elif option == 5:
                    self.__store.process_order_menu(self.show_order_menu)
                elif option == 6:
                    self.__store.search_recipes()
                elif option == 7:
                    print("Bye")
                    break
                else:
                    print("Invalid option.")
            except ValueError:
                print("Please enter a valid number.")

if __name__ == "__main__":
    app = PizzaStoreApp()
    app.process_command()