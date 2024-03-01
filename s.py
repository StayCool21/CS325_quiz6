# 1. You are working on a codebase for managing online orders. Currently, the Order
# class has the following functionalities:
# a. Storing order details (customer info, items, shipping address)
# b. Calculating total order cost (including taxes and discounts)
# c. Validating order data (checking item availability, customer address etc.)
# d. Sending order confirmation emails to customers
# e. Updating inventory levels after order processing
# Question: Write a Program (WAP) on how you would refactor the Order class to
# follow the Single Responsibility Principle (SRP). 

# The above class violates the Single Responsibility Principle (SRP) because it has multiple responsibilities.
# It should be refactored to follow the SRP. Below is the refactored code:
        
class Order:
    def __init__(self, customer_info, items, shipping_address) -> None:
        self.customer_info = customer_info
        self.items = items
        self.shipping_address = shipping_address

    def calculate_total_cost(self) -> float:
        total = 0

        for items in self.items:
            total += items.price # loop through the items and calculate the total cost
        return total
    
class OrderValidator:
    def vaildate_order(self) -> None:
        # check if the item is available
        # check if the customer address is valid
        print("Order is valid!")

class OrderConfirmation:
    def send_order_confirmation(self) -> None:
        print("Order confirmation email sent to customer!")

class InventoryUpdater:
    def update_inventory(self) -> None:
        print("Inventory updated after order processing!")

class Item:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class OrderProcessor:
    def process_order(self) -> None:
        order = Order()
        order_validator = OrderValidator()
        order_confirmation = OrderConfirmation()
        inventory_updater = InventoryUpdater()

        order_validator.vaildate_order()
        order_confirmation.send_order_confirmation()
        inventory_updater.update_inventory()
        print("Order processed successfully!")

# The refactored code follows the Single Responsibility Principle (SRP) by separating the responsibilities into different classes.
        