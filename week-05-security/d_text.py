# what the program does is
# To encode the text into image

# 1-loads an image and looks at each pixels in hexadecimal value
# 2-converts secret text into bits and stores them in LSB of pixel bits
# 3-a delimiter is added to the end of the edited pixel values
# 4- while retrieving all the 0 and 1 extracted until delimiter is found.
# Exracted bits are converted into string(secret message)


from PIL import Image

# Creating an Image Object
enc_img = Image.open('s1.bmp')

# Loading pixel values of original image, each entry is pixel value ie., RGB values as sublist
enc_pixelMap = enc_img.load()

# Creating an empty String for our hidden message
msg = ""
msg_index = 0

# Traversing through the pixel values
for row in range(enc_img.size[0]):
    for col in range(enc_img.size[1]):
        # Fetching RGB value a pixel to sublist
        # ----------------
        list1 = enc_pixelMap[row, col]

        r = list1[0]
  # R value
        if col == 0 and row == 0:		# 1st pixel was used to store the length of message
            msg_len = r

        elif msg_len > msg_index:		# Reading the message from R value of pixel
            msg = msg + chr(r)
            # Converting to character
            msg_index = msg_index+1
    enc_img.close()
print("The hidden message is :", msg)
