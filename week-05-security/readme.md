# What the program does is encoding a text into image.

1-Loads an image and looks at each pixels.

2-Converts secret text into bits and stores them in LSB of pixel bits.

3-Then extract the the text from the cover image.

# How you run the program ?

1- First run the encode Python file from the terminal by typing python3 encode.py

2- It will ask for the user input text, then press enter

3- The program will create a new image with hidden secret message

4- To get the hidden text run the decode Python file from the terminal by typing python3 decode.py

5-The secret message will be printed.
