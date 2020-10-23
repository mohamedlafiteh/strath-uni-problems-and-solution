from PIL import Image


def decode(inFile):
    image = Image.open(inFile)
    str_to_binary = ''

    pixels = image.load()
    # Iterate over pixels of the first row
    for x in range(0, image.width):
        r, g, b = pixels[x, 0]
        # Store LSB of each color channel of each pixel
        str_to_binary += bin(r)[-1]
        str_to_binary += bin(g)[-1]
        str_to_binary += bin(b)[-1]
    # working ok

    def binary_to_decimal(binary):
        string = int(binary, 2)
        return string

    binary_text = str_to_binary

    str_data = ' '

    for i in range(0, len(binary_text), 7):
        tem_d = binary_text[i:i + 7]
        decimal_t = binary_to_decimal(tem_d)
        string_text = string_text + chr(decimal_t)
    # printing the result
    print("The string is :", string_text)


decode("./s1.bmp")
