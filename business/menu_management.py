from business.models import PizzaMenuItem, PizzaCategory
from pizza_store_repository import PizzaMenuRepository
from typing import Optional

class MenuManagement:
    def __init__(self) -> None:
        self.__repository = PizzaMenuRepository()
        self.__menu_items:list[PizzaMenuItem] = []
        self.load_menu()

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self) -> PizzaMenuItem:
        if self.__index >= len(self.__menu_items) - 1:
            raise StopIteration()
        self.__index += 1
        return self.__menu_items[self.__index]

    def menu_items(self):
        items = []
        for item in self:
            items.append(item)
        return items
    
    def get_menu_item_by_name(self, name: str) -> Optional[PizzaMenuItem]:
        for item in self.__menu_items:
            if item.name == name:
                return item
        return None

    def load_menu(self) -> None:
        try:
            self.__menu_items = self.__repository.load_menu()
        except Exception as e:
            print(f"Error loading menu: {e}")

    def save_menu(self) -> None:
        try:
            self.__repository.save_menu_items(self.__menu_items)
        except Exception as e:
            print(f"Error saving menu: {e}")

    def add_menu_item(self, menu_item: PizzaMenuItem) -> None:
        try:
            self.__menu_items.append(menu_item)
            self.save_menu()
            print(f"Successfully added menu item: {menu_item.name}")
        except Exception as e:
            print(f"Error adding menu item: {e}")

    def remove_menu_item(self, name: str) -> None:
        try:
            found = False
            for i in range(len(self.__menu_items)):
                if self.__menu_items[i].name == name:
                    self.__menu_items.pop(i)
                    self.save_menu()
                    print(f"Successfully removed menu item: {name}")
                    found = True
                    break
            if not found:
                print(f"Menu item not found: {name}")
        except Exception as e:
            print(f"Error removing menu item: {e}")

    def update_menu_item(self, name: str, new_menu_item: PizzaMenuItem) -> None:
        try:
            found = False
            for i in range(len(self.__menu_items)):
                if self.__menu_items[i].name == name:
                    self.__menu_items[i] = new_menu_item
                    self.save_menu()
                    print(f"Successfully updated menu item: {name}")
                    found = True
                    break
            if not found:
                print(f"Menu item not found: {name}")
        except Exception as e:
            print(f"Error updating menu item: {e}")

    def get_menu_items_by_category(self, category: PizzaCategory) -> list[PizzaMenuItem]:
        result = []
        for item in self.__menu_items:
            if item.category == category:
                result.append(item)
        return result

    def list_menu_items(self) -> None:
        print("\n==== CURRENT MENU ITEMS ====")
        if not self.__menu_items:
            print("No items on the menu")
            return
        for item in self.__menu_items:
            print(item)
