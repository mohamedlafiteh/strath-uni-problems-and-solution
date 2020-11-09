from PIL import Image


def decode(inFile):
    image = Image.open(inFile)
    st_to_bin = ''
    pixels = image.load()

    # Loop over pixels of the first row
    for x in range(0, image.width):
        r, g, b = pixels[x, 0]
        # Store LSB of each color of each pixel
        st_to_bin += bin(r)[-1]
        st_to_bin += bin(g)[-1]
        st_to_bin += bin(b)[-1]

    def binary_to_decimal(binary):
        dec_n = int(binary, 2)
        return dec_n

    binary_text = st_to_bin
    string_text = ' '

    for i in range(0, len(binary_text), 8):
        tem_d = binary_text[i:i + 8]
        decimal_n = binary_to_decimal(tem_d)
        string_text = string_text + chr(decimal_n)
    # check message for length header
    msg_length = slice(0, 6)
    # combine header and message length
    slice_param = 6 + int(string_text[msg_length])
    slice_object = slice(6, slice_param)
    # slice string - remove header and tail,only keep encoded message
    string_text = string_text[slice_object]
    print("The string is :", string_text)


decode("./cover_image2.bmp")
