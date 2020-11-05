import unittest

from item_and_qt import ItemAndQty, Shop, ShoppingBasket


class TestItemsShop(unittest.TestCase):
    # Testing the repr method prints the write data
    def test_item_and_qty_repr(self):
        item = ItemAndQty("item_1", 100, 10)
        result = "The item name : " + str(item.item_name) + ".\n"
        result += "The item price : " + str(item.price) + ".\n"
        result += "The quantity : " + str(item.quantity) + "."

        self.assertEqual(str(item), result)
    # Testing the loading csv method loads the data in the shop class

    def test_loading_csv(self):

        shop = Shop()

        shop.load_initial_stock("./test_stock.csv")

        res = {

            "item_1": shop.data_member.get("item_1"),
            "item_2": shop.data_member.get("item_2"),
        }
        self.assertEqual(shop.data_member, res)

    # Testing the items in stock method by passing item name

    def test_items_in_stock(self):
        shop = Shop()
        shop.add_item_and_qty(
            {"item_name": "new_item", "price": 10, "quantity": 20})
        self.assertEqual(shop.items_in_stock("new_item"), 20)

    # Testing the add item method to add items to the basket

    def test_add_item_and_qty(self):

        shop = Shop()

        shoppingBasket = ShoppingBasket(shop)
        shoppingBasket.add_item_and_qty("item_1", 30)

        self.assertEqual(shoppingBasket.calculate_total_cost(), 300)


if __name__ == "__main__":
    unittest.main()
