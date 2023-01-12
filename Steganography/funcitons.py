from PIL import Image

img = Image.open(r"C:\Users\OWNER\Downloads\test.png", "r")
# img.show()
pixel = list(img.getdata())

cipher = img.copy()
# cipher.show()


new_data = []


def data_binary(data):  # convert data to encrypt into binary code
    for m in data:
        new_data.append(format(ord(m), "08b"))


data_binary("Hii")


def pixies():
    pixels = iter(pixel)
    for i in range(len(new_data)):
        frames = pixels.__next__()[:3] + pixels.__next__()[:3] + pixels.__next__()[:3]

        for j in range(8):
            if new_data[i][j] == "0":
                if frames[j] % 2 != 0:
                    frames[j] -= 1
                else:
                    pass
            elif new_data[i][j] == "1":
                if frames[j] % 2 == 0:
                    if frames[j] != 0:
                        frames[j] -= 1
                    else:
                        frames[j] += 1

        if i == (len(new_data) - 1):
            if frames[-1] % 2 == 0:
                if frames[-1] != 0:
                    frames[-1] -= 1
                else:
                    frames[-1] += 1

        else:
            if frames[-1] % 2 != 0:
                frames[-1] -= 1

        frames = tuple(frames)
        yield frames[0:3]
        yield frames[3:6]
        yield frames[6:9]


def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel123 in pixies():

        # Putting modified pixels in the new image
        newimg.putpixel((x, y), pixel123)
        if x == (w - 1):
            x = 0
            y += 1
        else:
            x += 1


# Encode data into image
def encode():
    img123 = input("Enter image name(with extension) : ")
    image = Image.open(img123, 'r')

    data = input("Enter data to be encoded : ")
    if len(data) == 0:
        raise ValueError('Data is empty')

    new_img = image.copy()
    encode_enc(new_img, data)

    new_img_name = input("Enter the name of new image(with extension) : ")
    new_img.save(new_img_name, str(new_img_name.split(".")[1].upper()))


# Decode the data in the image
def decode():
    img = input("Enter image name(with extension) : ")
    image = Image.open(img, 'r')

    data = ''
    imgdata = iter(image.getdata())

    while True:
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]

        # string of binary data
        binstr = ''

        for i in pixels[:8]:
            if i % 2 == 0:
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if pixels[-1] % 2 != 0:
            return data


# Main Function
def main():
    a = int(input(":: Welcome to Steganography ::\n"
                  "1. Encode\n2. Decode\n"))
    if a == 1:
        encode()

    elif a == 2:
        print("Decoded Word :  " + decode())
    else:
        raise Exception("Enter correct input")


# Driver Code
if __name__ == '__main__':

    # Calling main function
    main()