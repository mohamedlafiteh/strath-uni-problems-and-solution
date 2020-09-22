"""
3. Write a function that converts a string to an integer, by casting the string to an
integer. If the string is not an integer, then the function should return None. The
function should have one input argument and one return value. The input argument
should be the string that is to be converted to an integer. The input argument should
have the form "1242" or some other numeric value.
The function should use try and except to catch the ValueError exception that is
thrown if the string is not an integer. For example, if the function is provided with
"1242sd" it should return None.

"""


def type_casting(user_input):
    return user_input


if __name__ == "__main__":
    user_input = int(input("Please enter number :"))
    try:
        print(type_casting(user_input))
    except ValueError as e:
        print(e)
        print("Please enter a valid number")
