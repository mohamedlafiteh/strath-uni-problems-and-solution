
import csv


my_dic = {}


def read_csv(file_name):
    c_csv_file = open(file_name, "r", newline='')
    csv_reader = csv.reader(c_csv_file, delimiter=',', quotechar='"')
    for rows in csv_reader:
        k = rows[0]
        v = rows[1]
        z = rows[3]
        print(k, v)
        my_dic = {rows[0]: rows[1] for rows in csv_reader}
    c_csv_file.close()

    p_csv_file = open(file_name, "r", newline='')
    csv_reader = csv.reader(p_csv_file, delimiter=',', quotechar='"')
    for rows in csv_reader:
        k = rows[1]
        v = rows[2]
        print(k, v)

    p_csv_file.close()

    return my_dic


read_csv("Purchases.csv")
