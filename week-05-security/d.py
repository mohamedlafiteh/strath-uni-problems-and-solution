from PIL import Image


def decode(inFile):
    image = Image.open(inFile)
    extracted = ''

    pixels = image.load()
    # Iterate over pixels of the first row
    for x in range(0, image.width):
        r, g, b = pixels[x, 0]
        # Store LSB of each color channel of each pixel
        extracted += bin(r)[-1]
        extracted += bin(g)[-1]
        extracted += bin(b)[-1]
    # working ok

    def BinaryToDecimal(binary):
        string = int(binary, 2)
        return string
    bin_data = extracted
    # bin_data = '11010001100101110110011011001101111'
    str_data = ' '
    for i in range(0, len(bin_data), 7):
        temp_data = bin_data[i:i + 7]
        decimal_data = BinaryToDecimal(temp_data)
        str_data = str_data + chr(decimal_data)
    # printing the result
    print("The string is :", str_data)


decode("./s1.bmp")


# # To dencode the text into image


# image = Image.open("s1.bmp")
# extracted = ''

# pixels = image.load()
# # Iterate over pixels of the first row
# for x in range(0, image.width):
#     r, g, b = pixels[x, 0]
#     # Store LSB of each color channel of each pixel
#     extracted += bin(r)[-1]
#     extracted += bin(g)[-1]
#     extracted += bin(b)[-1]

# print(extracted)
# # working ok


# def BinaryToDecimal(binary):
#     string = int(binary, 2)
#     return string


# bin_data = extracted

# # bin_data = '11010001100101110110011011001101111'

# str_data = ' '

# for i in range(0, len(bin_data), 8):

#     temp_data = bin_data[i:i + 8]
#     decimal_data = BinaryToDecimal(temp_data)
#     str_data = str_data + chr(decimal_data)

# # printing the result
# print("The string is :", str_data)
