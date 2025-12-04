class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}")

class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address

    def place_order(self, item):
        return 0
    
class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle
    
    def deliver(self,order):
        print(f"{order.driver} is delivering {order.item} to {order.customer} using {self.vehicle}")
        order.status = "delivered"

class DeliveryOrder:
    def __init__(self, customer, item, status="preparing"):
        self.customer = customer
        self.item = item
        self.status = status

    def assign_driver(self,driver):
        self.driver = driver

    def summary(self):
        print("Order Summary:")
        print(f"Item: {self.item}")
        print(f"Customer: {self.customer}")
        print(f"Status: {self.status}")
        print(f"Driver: {self.driver}")
        print()

alice = Customer("Alice", "KU")
bob = Customer("Bob", "CU")
david = Driver("David", "motorcycle")

alice.introduce()
bob.introduce()
david.introduce()
print()

order1 = DeliveryOrder(alice.name, "Laptop")
order1.assign_driver(david.name)
order1.summary()

order2 = DeliveryOrder(bob.name, "Headphones")
order2.assign_driver(david.name)
order2.summary()

david.deliver(order1)
david.deliver(order2)
print()

print("Final Status:")
print(f"Order for {order1.item} → {order1.status}")
print(f"Order for {order2.item} → {order2.status}")