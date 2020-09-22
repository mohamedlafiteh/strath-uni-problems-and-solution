
numbers_list=["one", "two", "three", "four", "five",
"six", "seven", "eight", "nine", "ten"]


def converter(user_input):
    if user_input in numbers_list:
        return numbers_list.index(user_input) + 1
  
    



#user_input=input("Please write a number :")

user_input=input("Please inter number : ")
print(converter(user_input))