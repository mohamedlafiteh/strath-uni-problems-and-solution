
from PIL import Image


# This function to encode the text from the user
def encode(st, file_name):

    # get length of the message - pad with 0 so always same length
    msg_len = str(len(st)).rjust(5, '0')
    # append length and pad to start of message
    st = msg_len + st
   # Getting the size of the string in bytes
    str_size_in_byte = len(st.encode("utf-8"))
    str_size_in_bit = str_size_in_byte * 8

    #binary_data_from_string = "".join(format(ord(x), 'b') for x in st)
    binary_data_from_string = "".join([bin(ord(x))[2:].zfill(8) for x in st])
    i = 0
    with Image.open(file_name) as img:
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
                img.save("cover_image2.bmp")
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
            encode(user_input, "./cover_image1.bmp")
            text = False
