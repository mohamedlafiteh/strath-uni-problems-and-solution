import csv
import json
from copy import copy


class ItemAndQty:

    # This constructor only has three data members.

    def __init__(self, item_name, price, quantity):
        self.item_name = str(item_name)
        self.price = float(price)
        self.quantity = int(quantity)

# This function prints the data members.

    def __repr__(self):
        s = "The item name : " + str(self.item_name) + ".\n"
        s += "The item price : " + str(self.price) + ".\n"
        s += "The quantity : " + str(self.quantity) + "."
        return s

# The cost function returns the total cost of items by price and quantity multiplication.

    def cost(self):
        multiplication_result = self.price * self.quantity
        return multiplication_result


class Shop:

    # This constractor has one data member a dictionary

    def __init__(self):
        #item_and_qty = ItemAndQty()
        self.data_member = {}


# This function create Item not exists or increment quantity by quantity supplied if it does.


    def add_item_and_qty(self, item):
        if item.get("item_name") in self.data_member.keys():
            self.data_member.get(item.get("item_name")
                                 ).quantity += item.get("quantity")
        else:
            item_and_qty = ItemAndQty(
                item.get("item_name"), item.get("price"), item.get("quantity")
            )
            data_member = {item_and_qty.item_name: item_and_qty}
            self.data_member.update(data_member)

# This function load the stock from csv file

    def load_initial_stock(self, csv_file_path):

        stock_list = self.csv_to_json(csv_file_path)
        for item in stock_list:
            self.add_item_and_qty(item)

    # This function loads the csv in json format

    def csv_to_json(self, csv_file_path):
        item_list = []
        with open(csv_file_path, encoding="utf-8") as csvf:
            csv_reader = csv.DictReader(csvf)

            for raw in csv_reader:
                item_dict = {}
                item_dict["item_name"] = raw["item_name"]
                item_dict["price"] = float(raw["price"])
                item_dict["quantity"] = int(raw["quantity"])
                item_list.append(item_dict)
        return item_list

# This function returns ItemAndQty object by name or None if not exists

    def item_and_qty_by_name(self, item_name):
        item = self.data_member.get(item_name)

        if item:
            return item
        return None

# This function returns quantity of the item by name or 0 if not exists

    def items_in_stock(self, item_name):
        item = self.data_member.get(item_name)
        if item:
            return self.item_and_qty_by_name(item_name).quantity
        return 0


class ShoppingBasket:
    def __init__(self, shop):
        self.shop = shop
        self.shop.load_initial_stock("./stock.csv")
        self.basket = []
        self.total_cost = 0

    def add_item_and_qty(self, item_name, quantity):
        item = self.shop.item_and_qty_by_name(item_name)
        # if the item exist in the shop
        if item:
            # if the item exist in the basket
            if item in self.basket:
                basket_item = self.basket[self.basket.index(item)]
                basket_item.quantity += quantity
            # if item is not exist in the basket
            else:
                new_item = copy(item)
                new_item.quantity = quantity
                self.basket.append(new_item)
            item.quantity -= quantity
        else:
            self.basket.append(item)
        return 0

# This function calculate the total cost of items in the basket

    def calculate_total_cost(self):
        for item in self.basket:
            self.total_cost += item.cost()
        return self.total_cost

# This function clears all items in the basket
    def clear_items(self):
        self.basket.clear()


if __name__ == "__main__":

    shop = Shop()
    shop.load_initial_stock("./stock.csv")
    # print("------->before", shop.data_member)

    shop.add_item_and_qty({"item_name": "item_8", "price": 20, "quantity": 30})
    shop.add_item_and_qty({"item_name": "item_8", "price": 20, "quantity": 30})

    # print("------->after", shop.data_member)

    s = ShoppingBasket(shop)
    s.add_item_and_qty("item_4", 3)
    print("------->", s.basket)
