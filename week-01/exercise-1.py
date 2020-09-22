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

# This function converts the string input and return the index number in the list


def converter(user_input):
    if user_input in numbers_list:
        return numbers_list.index(user_input) + 1


if __name__ == "__main__":
    user_input = input("Please inter number : ")

    # This to check the user input is not empty

    if len(user_input) == 0:
        print("Please enter a valid number")
    else:
        print(converter(user_input))
