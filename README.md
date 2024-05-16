# Звіт з лабораторної роботи №8. Заздрісні функції.
> Виконала студентка групи ІКМ-М223в **Павленко Дарина**
> 
### Мета: Рефакторінг коду з проблемою «Заздрісні функції».

### Завдання 1: Наданий код
    
    class Customer:
        def __init__(self, name, address):
            self.name = name
            self.address = address

        def get_address(self):
            return self.address

    class Order:
        def __init__(self, customer, product, quantity):
            self.customer = customer
            self.product = product
            self.quantity = quantity

        def print_order_details(self):
            print(f"Order for {self.product} x {self.quantity}")
            print(f"Shipping to {self.customer.get_address()}")

        def calculate_shipping_cost(self):
            address = self.customer.get_address()
            if "New York" in address:
                return 5.00
            elif "California" in address:
                return 10.00
            else:
                return 15.00

### Рішення
Проблема "заздрісних функцій" виникає, коли один клас занадто сильно залежить від іншого, використовуючи його методи та поля. Для рефакторингу цього коду, нам слід зменшити залежність класу Order від класу Customer:

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
        
Отже, змінено клас Customer, його поля name та address стали приватними, щоб зменшити залежність класу Order. Тепер клас Order використовує метод _customer.get_address() замість self.customer.get_address(). Також тепер використовується SHIPPING_COSTS для визначення вартості доставки для різних місць.
