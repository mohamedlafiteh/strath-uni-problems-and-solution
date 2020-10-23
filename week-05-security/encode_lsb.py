
from PIL import Image

# This function to encode the text from the user


def encode(st, file_name):
    binary_data_from_string = "".join(format(ord(x), 'b') for x in st)
    i = 0
    with Image.open(file_name) as img:
        width, height = img.size
        for y in range(0, height):
            for x in range(0, width):
                pixels = list(img.getpixel((x, y)))
                for n in range(0, 3):
                    if(i < len(binary_data_from_string)):
                        pixels[n] = pixels[n] & ~1 | int(
                            binary_data_from_string[i])
                        i += 1
                img.putpixel((x, y), tuple(pixels))
        img.save("s1.bmp")


if __name__ == "__main__":

    user_input = input("Enter the text you would like to encode: ")

    text = True

    while text:
        if len(user_input) == 0:
            print("Please enter valid text")
        else:
            encode(user_input, "./s.bmp")

        print("if you like to encode another text please enter  yes or no :")
        user_input2 = input("Enter yes or no: ")
        if user_input2.lower() == "yes":
            user_input3 = input("Enter the text you would like to encode: ")
            if len(user_input) == 0:
                print("Please enter valid text")
            else:
                encode(user_input3, "./s.bmp")
        elif user_input2.lower() == "no":
            text = False
            print("Thanks you!")
