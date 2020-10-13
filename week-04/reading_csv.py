
import csv


my_dic = {}


def read_csv(purchases_file, customers_file):
    c_csv_file = open(customers_file, "r", newline='')
    csv_reader = csv.reader(c_csv_file, delimiter=',', quotechar='"')

    dataTable = {}
    columnNames = []
    numberOfColumns = 0

    for row in csv_reader:
        if len(columnNames) == 0:
            columnNames += row
            numberOfColumns = len(columnNames)
            for columnName in row:
                dataTable[columnName] = []
            continue
        for i in range(numberOfColumns):
            if i >= len(row):
                break
            dataTable[columnNames[i]] += [row[i]]

    c_csv_file.close()

    p_csv_file = open(purchases_file, "r", newline='')
    csv_reader = csv.reader(p_csv_file, delimiter=',', quotechar='"')
    for rows in csv_reader:
        pass
    p_csv_file.close()
    print(dataTable)
    return my_dic


read_csv("Purchases.csv", "Customers.csv")
