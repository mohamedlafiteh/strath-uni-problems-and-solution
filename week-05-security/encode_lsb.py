
from PIL import Image


# This function to encode the text from the user


def encode(st, file_name):

    # Getting the size of the string in bytes
    str_size_in_byte = len(st.encode("utf-8"))

    # Getting the size of the string in bits
    str_size_in_bit = str_size_in_byte * 8

    # Getting binary data from a string
    binary_data_from_string = "".join([bin(ord(x))[2:].zfill(8) for x in st])
    # binary_data_from_string_size_in_byte = bin(
    #     str_size_in_byte).replace("0b", "")

    i = 0
    with Image.open(file_name) as img:
        # Getting the size of the image in bytes
        img_size_in_byte = len(img.fp.read())

        if str_size_in_bit < img_size_in_byte:
            # Checking the file format if it is BMP
            format_check = img.format
            if format_check == "BMP":
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
                img.save("s2.bmp")
            else:
                print("Wrong foramt, please enter BMP  format image:")

        else:
            print("Not enough size in the image")


if __name__ == "__main__":

    user_input = input("Enter the text you would like to encode: ")

    text = True

    while text:
        if len(user_input) == 0:
            print("It is empty")
            user_input = input("Please enter valid text: ")

        else:
            encode(user_input, "./s.bmp")
            text = False
