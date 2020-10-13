import reading_csv

from reading_csv import read_csv


class Customer:

    def __init__(self, cus_id, first_name, last_name):
        self.cus_id = cus_id
        self.first_name = first_name
        self.last_name = last_name
        self.purchase_list = []

    def __repr__(self):
        return f"Customer { self.name} purchase total: {sum(self.purchase_list)}"


class Purchase:
    def __init__(self, item_id, amount_paid):
        self.item_id = item_id
        self.amount_paid = amount_paid

    def __repr__(self):
        return f"item { self.item_id} total paid : {self.amount_paid}"
