"""1. Write a function that converts one of {"one", "two", "three", "four", "five",
"six", "seven", "eight", "nine", "ten"} into a corresponding integer value.
For example, the function should return 1 when it is given "one".
The function should have one input argument and one return value. The input
argument should be a string and the return value should be an integer.
"""

numbers_list = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
]


def converter(user_input):
    if user_input in numbers_list:
        return numbers_list.index(user_input) + 1


# user_input=input("Please write a number :")
if __name__ == "__main__":
    user_input = input("Please inter number : ")
    if len(user_input) == 0:
        print("Please enter a valid number")
    else:
        print(converter(user_input))
