from PIL import Image

# Creating a image object
org_img = Image.open('s.bmp')


# Loading pixel values of original image, each entry is pixel value ie., RGB values as sublist
org_pixelMap = org_img.load()


# Creating new image object with image mode and dimensions as that of original image
enc_img = Image.new(org_img.mode, org_img.size)
enc_pixelsMap = enc_img.load()

# Reading message to be encrypted from user
msg = input("Enter the message :\t")
msg_index = 0

# Finding the length of message
msg_len = len(msg)

# Traversing through the pixel values
for row in range(org_img.size[0]):

    for col in range(org_img.size[1]):

        # Fetching RGB value a pixel to sublist

        # ----------------
        list1 = org_pixelMap[row, col]
       # print("======>", list1)

        r = list1[0]  # R value
        g = list1[1]  # G value
        b = list1[2]  # B value

        if row == 0 and col == 0:		# 1st pixel is used to store the length of message
            ascii = msg_len

            enc_pixelsMap[row, col] = (ascii, g, b)
        elif msg_index <= msg_len:  # Hiding our message inside the R values of the pixels
            c = msg[msg_index-1]

            ascii = ord(c)

            enc_pixelsMap[row, col] = (ascii, g, b)
        else:				# Assigning the pixel values of old image to new image
            enc_pixelsMap[row, col] = (r, g, b)
        msg_index += 1
org_img.close()

# Display the image
# enc_img.show()

# Save the image
enc_img.save("s1.bmp")
enc_img.close()
