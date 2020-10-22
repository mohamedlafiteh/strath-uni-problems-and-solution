

from PIL import Image


def encode(st, inFile):
    data = "".join(format(ord(x), 'b') for x in st)
    # change it to binary
    i = 0
    # it seems ok
    with Image.open(inFile) as img:
        width, height = img.size
        for y in range(0, height):
            for x in range(0, width):
                pixel = list(img.getpixel((x, y)))
                for n in range(0, 3):
                    if(i < len(data)):
                        pixel[n] = pixel[n] & ~1 | int(data[i])
                        i += 1
                img.putpixel((x, y), tuple(pixel))
        img.save("s1.bmp")


user_input = input("Enter the text you would like to encode: ")

if len(user_input) == 0:
    print("please enter text ")
else:
    encode(user_input, "./s.bmp")


# from PIL import Image

# # working correct
# st = "hello"
# # change it to binary
# data = "".join(format(ord(x), 'b') for x in st)
# print(data)
# i = 0
# # it seems ok
# with Image.open("s.bmp") as img:
#     width, height = img.size
#     for y in range(0, height):
#         for x in range(0, width):
#             pixel = list(img.getpixel((x, y)))
#             for n in range(0, 3):
#                 if(i < len(data)):
#                     pixel[n] = pixel[n] & ~1 | int(data[i])
#                     i += 1
#             img.putpixel((x, y), tuple(pixel))
#     img.save("s1.bmp")
