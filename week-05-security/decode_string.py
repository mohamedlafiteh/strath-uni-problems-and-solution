# what the program does is
# To encode the text into image

# 1-loads an image and looks at each pixels in hexadecimal value
# 2-converts secret text into bits and stores them in LSB of pixel bits
# 3-a delimiter is added to the end of the edited pixel values
# 4- while retrieving all the 0 and 1 extracted until delimiter is found.
# Exracted bits are converted into string(secret message)

# To dncode the text into image
