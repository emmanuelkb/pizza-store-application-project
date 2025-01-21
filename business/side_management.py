from business.models import SideMenuItem, SideCategory
from pizza_store_repository import SideMenuRepository

class SideManagement:
    def __init__(self) -> None:
        self.__repository = SideMenuRepository()
        self.__sides:list[SideMenuItem] = []
        self.load_sides()

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self) -> SideMenuItem:
        if self.__index >= len(self.__sides) - 1:
            raise StopIteration()
        self.__index += 1
        return self.__sides[self.__index]

    def sides(self):
        items = []
        for item in self:
            items.append(item)
        return items
    
    def load_sides(self) -> None:
        try:
            self.__sides = self.__repository.load_sides()
        except Exception as e:
            print(f"Error loading sides: {e}")
    
    def save_sides(self) -> None:
        try:
            self.__repository.save_sides(self.__sides)
        except Exception as e:
            print(f"Error saving sides: {e}")
    
    def add_side(self, side: SideMenuItem) -> None:
        try:
            self.__sides.append(side)
            self.save_sides()
            print(f"Successfully added side item: {side.name}")
        except Exception as e:
            print(f"Error adding side item: {e}")
    
    def remove_side(self, name: str) -> None:
        try:
            for i in range(len(self.__sides)):
                if self.__sides[i].name == name:
                    self.__sides.pop(i)
                    self.save_sides()
                    print(f"Successfully removed side item: {name}")
                    return
            print(f"Side item not found: {name}")
        except Exception as e:
            print(f"Error removing side item: {e}")
    
    def get_sides_by_category(self, category: SideCategory) -> list[SideMenuItem]:
        result = []
        for side in self.__sides:
            if side.category == category:
                result.append(side)
        return result
    
    def list_sides(self) -> None:
        print("\n=== AVAILABLE SIDE ITEMS ===")
        if not self.__sides:
            print("No side items available")
            return
        for side in self.__sides:
            print(side)
