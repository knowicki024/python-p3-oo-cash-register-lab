#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = None
  
  def add_item(self, title, price, quantity = 1):
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(title)
    self.last_transaction = (price, quantity)

  def apply_discount(self):
        if self.discount == 0:
          print("There is no discount to apply.")  
        else:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            self.total = round(self.total, 2)  # Round to two decimal places
            print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    if self.last_transaction:
      last_price, last_quantity = self.last_transaction
      self.total -= (last_price * last_quantity)
      self.last_transaction = None
    else:
      return "No items to void."

  