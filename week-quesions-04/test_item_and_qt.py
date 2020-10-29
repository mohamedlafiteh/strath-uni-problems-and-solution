import unittest

from item_and_qt import ItemAndQty, Shop, ShoppingBasket


class TestItemsShop(unittest.TestCase):
    def test_item_and_qty_repr(self):
        item = ItemAndQty("item1", 100, 10)
        result = "The item name : " + str(item.item_name) + ".\n"
        result += "The item price : " + str(item.price) + ",.\n"
        result += "The quantity : " + str(item.quantity) + "."

        self.assertEqual(str(item), result)

    def test_loading_csv(self):

        shop = Shop("item_0", 0, 0)

        shop.load_initial_stock("./stock.csv")

        res = {
            "item_0": shop.data_member.get("item_0"),
            "item_1": shop.data_member.get("item_1"),
            "item_2": shop.data_member.get("item_2"),
        }
        self.assertEqual(shop.data_member, res)

    def test_items_in_stock(self):
        shop = Shop("new_item", 200, 300)
        self.assertEqual(shop.items_in_stock("new_item"), 300)

    def test_add_item_and_qty(self):

        shop = Shop("item_0", 0, 0)

        shoppingBasket = ShoppingBasket(shop)
        shoppingBasket.add_item_and_qty("item_1", 30)

        self.assertEqual(shoppingBasket.calculate_total_cost(), 300)

if __name__ == "__main__":
    unittest.main()