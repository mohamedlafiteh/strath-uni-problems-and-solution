"""
5. An input text string contains newline characters and additional spaces, together with
commas. Write a function that:
• Removes the newline characters.
• Splits the string using the comma character.
• Removes any leading and trailing white space from the resulting substrings.
• Returns the resulting list of values.
Create a test text string to demonstrate that the function works as expected.
The function should have one input argument and one return value. The input
argument should be in the input string, whereas the return value should be the
resulting list.

"""


def string_format(string_text):
    # This code removes the newline characters.
    remove_newline_characters = string_text.replace("\n", "")

    # Removes any leading and trailing white space from the resulting substrings.
    remove_space = remove_newline_characters.replace(" ", "")

    # This code Splits the string using the comma character.
    split_string = remove_space.split(",")

    # Returns the resulting list of values
    return split_string


if __name__ == "__main__":
    string_text = "Hell world \n ,welcome to Python class \n ,enjoy the learing"

    string_format(string_text)