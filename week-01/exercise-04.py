import math

"""
4. Write a function to compute the sample standard deviation of floating point input
values that are provided in a list. The function should have one input argument and
one return value. The input argument should be a list of input values and the return
argument should be the sample standard deviation.
The sample standard deviation is defined as:

The function should return None when the input list contains zero or one element. If
the input list contains two or more values, then it should return the sample standard
deviation.
"""

# This function just returns the average number of the list


def mean(numbers_list):
    average_number = sum(numbers_list) / len(numbers_list)
    return average_number


# T his function is the standard deviation


def stnDev(numbers_list):
    length = len(numbers_list)
    average = mean(numbers_list)
    total_sum = 0
    for i in numbers_list:
        total_sum += (i - average) ** 2
        root = total_sum / length
    return math.sqrt(root)


if __name__ == "__main__":
    numbers_list = [3.4, 6.5, 8.9, 2.5, 8, 4]
    if len(numbers_list) == 0:
        print("none")
    else:
        print(stnDev(numbers_list))
