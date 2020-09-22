"""
2. Write a function that returns the average value of input floating point values that
are provided in a list. The function should have one input argument and one return
value. The input argument should be the list and return value should be the average.
If the input list is empty, then the function should return None.
"""


# This function only return the average number
def find_averave(numbers_list):
    return sum(numbers_list) / len(numbers_list)


if __name__ == "__main__":

    numbers_list = [2.4, 24.5, 5.1, 44.5, 6.4]
    print(find_averave(numbers_list))