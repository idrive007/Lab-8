#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Customer:
    def __init__(self, name, address):
        self._name = name
        self._address = address

    def get_address(self):
        return self._address


class Order:
    SHIPPING_COSTS = {
        "New York": 5.00,
        "California": 10.00,
    }

    def __init__(self, customer, product, quantity):
        self._customer = customer
        self.product = product
        self.quantity = quantity

    def print_order_details(self):
        print(f"Order for {self.product} x {self.quantity}")
        print(f"Shipping to {self._customer.get_address()}")

    def calculate_shipping_cost(self):
        address = self._customer.get_address()
        for location, cost in self.SHIPPING_COSTS.items():
            if location in address:
                return cost
        return 15.00

    


# In[ ]:




