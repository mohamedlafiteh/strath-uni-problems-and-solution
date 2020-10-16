#!/usr/bin/env python3

import unittest
import Purchases

"""
A unit test class for the Purchases module.
"""
class Test_Purchases(unittest.TestCase):

    """
    Test that the totalAmountPaid function works as expected.
    """
    def test_amountPaid(self):
        customer = Purchases.Customer(1, "John", "Doe")
        customer.purchases += [ Purchases.Purchase(1, 25.0) ]
        customer.purchases += [ Purchases.Purchase(2, 20.0) ]
        self.assertEqual(45, customer.totalAmountPaid())

if __name__ == '__main__':
    unittest.main()
