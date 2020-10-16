#!/usr/bin/env python3

import csv

"""
A class to hold information concerning one
purchase.
"""
class Purchase:
    def __init__(self, itemId, amountPaid):
        self.itemId = int(itemId)
        self.amountPaid = float(amountPaid)

    def __repr__(self):
        s = "Purchase:{itemId:" + str(self.itemId) + ","
        s += "amountPaid:" + str(self.amountPaid)
        s += "}"
        return s

"""
A class to hold customer details and their associated
purchases.
"""
class Customer:
    def __init__(self, customerId, firstName, surname):
        self.customerId = int(customerId)
        self.firstName = str(firstName)
        self.surname = str(surname)
        self.purchases = []

    def __repr__(self):
        s = "Customer:{customerId:" + str(self.customerId) + ","
        s += "firstName:\"" + self.firstName + "\","
        s += "surname:\"" + self.surname + "\","
        s += "purchases:" + str(self.purchases)
        s += "}"
        return s

    """
    A function to return the purchases summary string for a customer.
    """
    def purchasesSummary(self):
        s = "customerId:" + str(self.customerId) + "\n"
        s += "ItemId" + "\t" + "AmountPaid\n"
        for purchase in self.purchases:
            s += str(purchase.itemId) + "\t" + str(purchase.amountPaid) + "\n"
        return s

    """
    A function to return the total amount paid by a customer.
    """
    def totalAmountPaid(self):
        total = 0.
        for purchase in self.purchases:
            total += purchase.amountPaid
        return total

"""
A function to load data into memory from a CSV file.
"""
def loadCSV(data, fileName):
    # Open the CSV file.
    csvFile = open(fileName, "r", newline='')
    csvReader = csv.reader(csvFile, delimiter=',', quotechar='"')

    # Clear the dictionary, in case this function is called twice.
    data.clear()

    columnNames = []
    nColumnNames = 0
    for row in csvReader:

        # The first row of the file contains the column names.
        if csvReader.line_num == 1:
            columnNames += row
            nColumnNames = len(columnNames)
            continue

        n = len(row)
        for i in range(n):

            # Prevent i from being too big for columnNames index.
            if i >= nColumnNames:
                continue

            # Find the column name for this column.
            columnName = columnNames[i]

            # If this column is not in the dictionary yet, create column.
            if not columnName in data:
                data[columnName] = []

            # Append this entry to the column.
            data[columnName] += [ row[i] ]

    # Close the CSV file.
    csvFile.close()

"""
A function to create customer objects from input data
tables.
"""
def createObjects(purchaseData, customerData, customers):
    customers.clear()

    # Get the number of rows.
    nRows = 0
    if "Id" in customerData.keys():
        nRows = len(customerData["Id"])

    # Create the customers objects.
    for i in range(nRows):
        customerId = customerData["Id"][i]
        if not customerId in customers:
            customers[customerId] = Customer(customerId, customerData["Firstname"][i], customerData["Surname"][i])

    # Get the number of rows.
    nRows = 0
    if "CustomerId" in purchaseData.keys():
        nRows = len(purchaseData["CustomerId"])

    # Append purchases to the Customer objects.
    for i in range(nRows):
        customerId = purchaseData["CustomerId"][i]

        # Try to find the matching customerId.
        if not customerId in customers.keys():
            continue

        # Append the new Purchase object to the Customer object.
        customers[customerId].purchases += [ Purchase(purchaseData["ItemId"][i],purchaseData["AmountPaid"][i]) ]


"""
A test program to prove that the functionality that
has been implemented works as expected.
"""
if __name__ == "__main__":

    # Load the input CSV files.
    purchaseData = {}
    customerData = {}
    loadCSV(purchaseData, "Purchases.csv")
    loadCSV(customerData, "Customers.csv")

    # Create objects from the data that have been loaded.
    customers = {}
    createObjects(purchaseData, customerData, customers)

    # Test the repr functions.
    print("=====================================")
    print(customers)

    # Test the purchasesSummary and totalAmountPaid function.
    print("=====================================")
    for customer in customers.values():
        print(customer.purchasesSummary())
        print("Total\t" + str(customer.totalAmountPaid()))
        print("-------------------------------------")