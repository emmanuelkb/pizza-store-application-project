from business.models import Order, OrderStatus
from pizza_store_repository import OrderRepository
from typing import Optional

class OrderManagement:
    def __init__(self) -> None:
        self.__repository = OrderRepository()
        self.__orders:list[Order] = []
        self.load_orders()

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self) -> Order:
        if self.__index >= len(self.__orders) - 1:
            raise StopIteration()
        self.__index += 1
        return self.__orders[self.__index]

    def orders(self):
        items = []
        for item in self:
            items.append(item)
        return items
    
    def load_orders(self) -> None:
        try:
            self.__orders = self.__repository.load_orders()
        except Exception as e:
            print(f"Error loading orders: {e}")
    
    def save_orders(self) -> None:
        try:
            self.__repository.save_orders(self.__orders)
        except Exception as e:
            print(f"Error saving orders: {e}")
    
    def create_order(self, order: Order) -> None:
        try:
            self.__orders.append(order)
            self.save_orders()
            print(f"Successfully created order: {order.order_id}")
        except Exception as e:
            print(f"Error creating order: {e}")
    
    def update_order_status(self, order_id: str, status: OrderStatus) -> None:
        try:
            for order in self.__orders:
                if order.order_id == order_id:
                    order.status = status
                    self.save_orders()
                    print(f"Successfully updated order {order_id} status to {status.value}")
                    return
            print(f"Order not found: {order_id}")
        except Exception as e:
            print(f"Error updating order status: {e}")
    
    def get_order_by_id(self, order_id: str) -> Optional[Order]:
        for order in self.__orders:
            if order.order_id == order_id:
                return order
        return None
    
    def list_orders(self, status: Optional[OrderStatus] = None) -> None:
        print("\n=== ORDERS ===")
        if not self.__orders:
            print("No orders found")
            return
        filtered_orders = self.__orders
        if status:
            filtered_orders = []
            for order in self.__orders:
                if order.status == status:
                    filtered_orders.append(order)
        
        for order in filtered_orders:
            print(f"\nOrder ID: {order.order_id}")
            print(f"Customer: {order.customer_name}")
            print(f"Status: {order.status.value}")
            print(f"Delivery Time: {order.delivery_time}")
            print(f"Total: ${order.calculate_total():.2f}")
    
    def generate_kitchen_slip(self, order_id: str) -> None:
        order = self.get_order_by_id(order_id)
        if order:
            print(order.generate_kitchen_slip())
        else:
            print(f"Order not found: {order_id}")
    