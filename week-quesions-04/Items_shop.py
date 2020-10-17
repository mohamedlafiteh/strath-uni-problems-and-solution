import csv
import json


class ItemAndQty:
    def __init__(self, item_name, price, quantity):
        self.item_name = str(item_name)
        self.price = float(price)
        self.quantity = int(quantity)

    def __repr__(self):
        s = "The item name : " + str(self.item_name) + ".\n"
        s += "The item price : " + str(self.price) + ",.\n"
        s += "The quantity : " + str(self.quantity) + "."

        return s

    def cost(self):
        return self.price * self.quantity


class Shop:
    def __init__(self, item_name, price, quantity):
        item_and_qty = ItemAndQty(item_name, price, quantity)
        self.data_member = {item_and_qty.item_name: item_and_qty}

    def add_item_and_qty(self, items):
        if items.get("item_name") in self.data_member.keys():
            self.data_member.get(items.get("item_name")).quantity += items.get(
                "quantity"
            )
        else:
            item_and_qty = ItemAndQty(
                items.get("item_name"), items.get(
                    "price"), items.get("quantity")
            )
            data_member = {item_and_qty.item_name: item_and_qty}
            self.data_member.update(data_member)

    def load_initial_stock(self, csv_file_path):
        stock_list = self._csv_to_json(csv_file_path)
        for stock in stock_list:
            self.add_item_and_qty(stock)

    def _csv_to_json(self, csv_file_path):
        item_list = []
        with open(csv_file_path, encoding="utf-8") as csvf:
            csv_reader = csv.DictReader(csvf)
            for raw in csv_reader:
                item_dict = {}
                item_dict["item_name"] = raw["item_name"]
                item_dict["price"] = int(raw["price"])
                item_dict["quantity"] = int(raw["quantity"])
                item_list.append(item_dict)
        return item_list

    def item_and_qty_by_name(self, item_name):
        item = self.data_member.get(item_name)
        if item:
            return item
        return None

    def items_in_stock(self, item_name):
        item = self.data_member.get(item_name)
        if item:
            return self.item_and_qty_by_name(item_name).quantity
        return 0


class ShoppingBasket:
    def __init__(self):
        self.shop = Shop("i1", 10, 0)
        self.shop.load_initial_stock("./stock.csv")
        self.basket = {}
        self.total_cost = 0

    def add_item_and_qty(self, item_name, quantity):
        item = self.shop.item_and_qty_by_name(item_name)
        if item:
            item.quantity -= quantity
            basket_item = self.basket.get(item.item_name)
            if basket_item:
                basket_item.quantity += quantity
            else:
                self.basket.update(
                    Shop(item.item_name, item.price, quantity).data_member
                )
        return 0

    def calculate_total_cost(self):
        for item in self.basket:
            self.total_cost += self.basket[item].cost()
        return self.total_cost

    def clear_items(self):
        self.basket.clear()

# another_blah = ShoppingBasket()
# another_blah.add_item_and_qty("item_2", 15)
# another_blah.add_item_and_qty("item_3", 10)
# print("----------->", another_blah.basket)
# print("------>", another_blah.calculate_total_cost())


if __name__ == '__main__':

    s = ItemAndQty("milk", 4, 8)
