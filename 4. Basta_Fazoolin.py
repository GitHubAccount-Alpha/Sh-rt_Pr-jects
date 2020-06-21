from datetime import time

############################################# MENU
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name=name
    self.items=items
    self.start_time=start_time
    self.end_time=end_time
  def __repr__(self):
    return "{a} menu available from {b}:00 am to {c}:00 pm".format(a=self.name, b=self.start_time, c=self.end_time)
############################################# BILL CALCULATION  
  def calculate_bill(self, purchased_items):
    total_price=0        
    for k in self.items:
      for i in purchased_items:
        if k==i: 
          total_price=total_price+self.items[k]
    return total_price
############################################# FRANCISE
class Franchise:
  def __init__(self, address, menus):
    self.menus=menus
    self.address=address
  def __repr__(self):
    return "Our address is {a}".format(a=self.address)
  def available_menus(self,time):
    a=[]
    for i in self.menus:
      if i.start_time <= time and i.end_time > time:
        a.append(i)
    return a
############################################# BUSINESS
class Business:
  def __init__(self, name, franchises):
    pass

############################################# MENU
brunch=Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)
early_bird=Menu("Early Bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 15, 18)
dinner=Menu("Dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 17, 23)             
kids=Menu("Kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21) 
print(dinner)
############################################# BILL CALCULATION  
brunch_price=brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
print(brunch_price)

early_bird_price=early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"])
print(early_bird_price)
############################################# FRANCISE
menus=[brunch, early_bird, dinner, kids]
flagship_store=Franchise("1232 West End Road", menus)
new_installment=Franchise("12 East Mulberry Street", menus)
print(flagship_store.available_menus(12))

############################################# BUSINESS
arepas_menu=Menu("Take a’ Arepa", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 10, 20) 
arepas_place=Franchise("189 Fitzgerald Avenue", arepas_menu)
franchises=[flagship_store, new_installment, arepas_place]
business_1=Business("Basta Fazoolin' with my Heart",franchises)
