from enum import Enum
from typing import Any
from datetime import datetime
from uuid import uuid4

class PizzaSize(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRA_LARGE = "extra_large"

class PizzaCategory(Enum):
    VEGETARIAN = "vegetarian"
    MEAT = "meat"
    SPECIALTY = "specialty"
    CUSTOM = "custom"

class SideCategory(Enum):
    SALAD = "salad"
    BEVERAGE = "beverage"
    DESSERT = "dessert"
    APPETIZER = "appetizer"

class OrderStatus(Enum):
    NEW = "new"
    PREPARING = "preparing"
    READY = "ready"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str, reorder_level: int) -> None:
        self.__name = name
        self.__quantity = quantity
        self.__unit = unit
        self.__reorder_level = reorder_level
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def quantity(self) -> float:
        return self.__quantity
    
    @property
    def unit(self) -> str:
        return self.__unit
    
    @property
    def reorder_level(self) -> int:
        return self.__reorder_level
    
    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name
    
    @quantity.setter
    def quantity(self, new_quantity: float) -> None:
        self.__quantity = new_quantity
    
    @unit.setter
    def unit(self, new_unit: str) -> None:
        self.__unit = new_unit
    
    @reorder_level.setter
    def reorder_level(self, new_reorder_level: int) -> None:
        self.__reorder_level = new_reorder_level
    
    def __str__(self) -> str:
        return f"Ingredient: name = {self.__name}, quantity = {self.__quantity}, unit = {self.__unit}, reorder level = {self.__reorder_level}"
    
    def __repr__(self) -> str:
        return "\n" + str(self)
    
    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.__name,
            "quantity": self.__quantity,
            "unit": self.__unit,
            "reorder_level": self.__reorder_level
        }

class PizzaRecipe:
    def __init__(self, name: str, ingredients: list[Ingredient]) -> None:
        self.__name = name
        self.__ingredients = ingredients
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def ingredients(self) -> list[Ingredient]:
        return self.__ingredients
    
    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name
    
    def add_ingredient(self, ingredient: Ingredient) -> None:
        self.__ingredients.append(ingredient)
    
    def remove_ingredient(self, ingredient_name: str) -> None:
        new_ingredients = []
        for ingredient in self.__ingredients:
            if ingredient.name != ingredient_name:
                new_ingredients.append(ingredient)
        self.__ingredients = new_ingredients
    
    def __str__(self) -> str:
        return f"Recipe: name = {self.__name}, ingredients = {self.__ingredients}"
    
    def __repr__(self) -> str:
        return "\n" + str(self)
    
    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.__name,
            "ingredients": [ingredient.to_dict() for ingredient in self.__ingredients]
        }

class PizzaMenuItem:
    def __init__(self, name: str, description: str, size: PizzaSize, price: float, 
                 category: PizzaCategory, recipe: PizzaRecipe) -> None:
        self.__name = name
        self.__description = description
        self.__price = price
        self.__size = size
        self.__recipe = recipe
        self.__category = category
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def description(self) -> str:
        return self.__description
    
    @property
    def price(self) -> float:
        return self.__price
    
    @property
    def size(self) -> PizzaSize:
        return self.__size
    
    @property
    def recipe(self) -> PizzaRecipe:
        return self.__recipe
    
    @property
    def category(self) -> PizzaCategory:
        return self.__category
    
    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name
    
    @description.setter
    def description(self, new_description: str) -> None:
        self.__description = new_description
    
    @price.setter
    def price(self, new_price: float) -> None:
        self.__price = new_price
    
    @size.setter
    def size(self, new_size: PizzaSize) -> None:
        self.__size = new_size
    
    @category.setter
    def category(self, new_category: PizzaCategory) -> None:
        self.__category = new_category
    
    def __str__(self) -> str:
        return f"Pizza Menu Item: name = {self.__name}, description = {self.__description}, size = {self.__size.value}, price = {self.__price}, " \
               f"category = {self.__category.value}, recipe = {self.__recipe}"
    
    def __repr__(self) -> str:
        return "\n" + str(self)
    
    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.__name,
            "description": self.__description,
            "size": self.__size.value,
            "price": self.__price,
            "category": self.__category.value,
            "recipe": self.__recipe.to_dict()
        }

class SideMenuItem:
    def __init__(self, name: str, description: str, price: float, category: SideCategory) -> None:
        self.__name = name
        self.__description = description
        self.__price = price
        self.__category = category
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def description(self) -> str:
        return self.__description
    
    @property
    def price(self) -> float:
        return self.__price
    
    @property
    def category(self) -> SideCategory:
        return self.__category
    
    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.__name,
            "description": self.__description,
            "price": self.__price,
            "category": self.__category.value
        }
    
    def __str__(self) -> str:
        return f"Side Item: {self.__name}, Price: ${self.__price:.2f}, Category: {self.__category.value}"

class CustomPizza:
    def __init__(self, size: PizzaSize, base_price: float) -> None:
        self.__size = size
        self.__base_price = base_price
        self.__toppings:dict[str,int] = {}
        
    def add_topping(self, topping: str, quantity: int = 1) -> None:
        if topping in self.__toppings:
            self.__toppings[topping] += quantity
        else:
            self.__toppings[topping] = quantity
    
    def remove_topping(self, topping: str) -> None:
        if topping in self.__toppings:
            del self.__toppings[topping]
    
    @property
    def size(self) -> PizzaSize:
        return self.__size
    
    @property
    def toppings(self) -> dict[str, int]:
        return self.__toppings.copy()
    
    @property
    def base_price(self) -> float:
        return self.__base_price
    
    def to_dict(self) -> dict[str, Any]:
        return {
            "size": self.__size.value,
            "base_price": self.__base_price,
            "toppings": self.__toppings
        }

class OrderItem:
    def __init__(self, quantity: int) -> None:
        self.__quantity = quantity

    def to_dict(self) -> dict[str, Any]:
        return {
            "quantity": self.quantity
        }
    
    @property
    def quantity(self) -> int:
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value: int) -> None:
        self.__quantity = value

class PizzaOrderItem(OrderItem):
    def __init__(self, quantity: int, pizza: PizzaMenuItem | CustomPizza) -> None:
        super().__init__(quantity)
        self.__pizza = pizza
    
    @property
    def pizza(self) -> PizzaMenuItem | CustomPizza:
        return self.__pizza
    
    def to_dict(self) -> dict[str, Any]:
        return {
            "quantity": self.quantity,
            "type": "pizza",
            "item": self.__pizza.to_dict()
        }

class SideOrderItem(OrderItem):
    def __init__(self, quantity: int, side: SideMenuItem) -> None:
        super().__init__(quantity)
        self.__side = side
    
    @property
    def side(self) -> SideMenuItem:
        return self.__side
    
    def to_dict(self) -> dict[str, Any]:
        return {
            "quantity": self.quantity,
            "type": "side",
            "item": self.__side.to_dict()
        }

class Order:
    def __init__(self, customer_name: str, phone: str, delivery_time: datetime, order_id:str) -> None:
        self.__customer_name = customer_name
        self.__phone = phone
        self.__delivery_time = delivery_time
        self.__status = OrderStatus.NEW
        self.__items:list[OrderItem] = []
        self.__order_id = order_id
    
    @property
    def customer_name(self) -> str:
        return self.__customer_name
    
    @property
    def phone(self) -> str:
        return self.__phone
    
    @property
    def delivery_time(self) -> datetime:
        return self.__delivery_time
    
    @property
    def status(self) -> OrderStatus:
        return self.__status
    # xx
    @property
    def items(self) -> list[OrderItem]:
        return self.__items
    
    @property
    def order_id(self) -> str:
        return self.__order_id
    
    @status.setter
    def status(self, new_status: OrderStatus) -> None:
        self.__status = new_status
    
    def add_item(self, item: OrderItem) -> None:
        self.__items.append(item)
    
    def remove_item(self, index: int) -> None:
        if 0 <= index < len(self.__items):
            self.__items.pop(index)
    
    def calculate_total(self) -> float:
        total = 0.0
        for item in self.__items:
            if isinstance(item, PizzaOrderItem):
                if isinstance(item.pizza, PizzaMenuItem):
                    total += item.pizza.price * item.quantity
                else:
                    pizza_total = item.pizza.base_price
                    for topping_qty in item.pizza.toppings.values():
                        pizza_total += 1.75 * topping_qty
                    total += pizza_total * item.quantity
            elif isinstance(item, SideOrderItem):
                total += item.side.price * item.quantity
        return total
    
    def to_dict(self) -> dict[str, Any]:
        return {
            "order_id": self.__order_id,
            "customer_name": self.__customer_name,
            "phone": self.__phone,
            "delivery_time": self.__delivery_time.isoformat(),
            "status": self.__status.value,
            "items": [item.to_dict() for item in self.__items]
        }
    
    def generate_kitchen_slip(self) -> str:
        slip = "=== KITCHEN ORDER SLIP ===\n"
        slip += f"Order ID: {self.__order_id}\n"
        slip += f"Delivery Time: {self.__delivery_time.strftime('%Y-%m-%d %H:%M')}\n\n"
        slip += "Items:\n"
        for item in self.__items:
            if isinstance(item, PizzaOrderItem):
                if isinstance(item.pizza, PizzaMenuItem):
                    slip += f"{item.quantity}x {item.pizza.name}\n"
                    slip += f"    Size: {item.pizza.size.value}\n"
                    slip += f"    Recipe: {item.pizza.recipe.name}\n"
                    slip += "\n"
                else: 
                    slip += f"{item.quantity}x Custom Pizza\n"
                    slip += f"    Size: {item.pizza.size.value}\n"
                    slip += "    Toppings:\n"
                    for topping, qty in item.pizza.toppings.items():
                        slip += f"      - {topping} (x{qty})\n"
                    slip += "\n"
            elif isinstance(item, SideOrderItem):
                slip += f"{item.quantity}x {item.side.name}\n"
                slip += "\n"
        slip += "=== END OF ORDER ===\n"
        return slip