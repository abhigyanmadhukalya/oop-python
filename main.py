import numpy as np

def format_float(x, trim_leading=True, **kwargs):
    s = np.format_float_positional(x, **kwargs)
    if trim_leading is True and int(x) == 0 and len(s) > 1:
        s = s.replace("0.", ".")
    return s

class Item:

    pay_rate = 0.8  # The pay rate after 20% discount

    Items = []

    def __init__(self, name: str, price: float, quantity: int):
        # Validate data types for parameters
        assert price >= 0, f"Price {price} is less than 1"
        assert quantity >= 0, f"Quantity {quantity} is less than 1"

        # Assign self to operator
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.Items.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

# OBJECTS
item1 = Item("Phone", 500, 5)
item2 = Item("Laptop", 1000, 10)
item3 = Item("Headphones", 200, 5)
item4 = Item("Cable", 10, 5)
item5 = Item("Mouse", 50, 5)
item6 = Item("Keyboard", 75, 5)

# You can add more attributes even after defining them in __init__
item1.has_numpad = False
item2.has_numpad = True

for i in Item.Items:
    i.apply_discount()
    print(
        f"The price of {i.name} after appplying the discount is ${format_float(i.price)}"
    )

print("-----------------------")

for i in Item.Items:
    print(
        f"The price of {i.name} is ${format_float(i.calculate_total_price())}")

# print(Item.__dict__) # All the attributes for Class Level
# print(item1.__dict__) # All the attributes for Instance Level

print("\n")
print(Item.Items)
