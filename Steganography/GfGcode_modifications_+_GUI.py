
    # Python program implementing Image Steganography

    # PIL module is used to extract
    # pixels of image and modify it
import tkinter
from PIL import Image, ImageTk
from functools import partial

def enc():
    # Convert encoding data into 8-bit binary
    # form using ASCII value of characters
    def binary_data(data):

        # list of binary codes
        # of given data
        new_data = []

        for i in data:
            new_data.append(format(ord(i), '08b'))
        return new_data


    # Pixels are modified according to the
    # 8-bit binary data and finally returned
    def pixel_values(pix, data):

        data_list = binary_data(data)
        frames = iter(pix)

        for i in range(len(data_list)):

            # Extracting 3 pixels at a time
            pix = [value for value in frames.__next__()[:3] +
                   frames.__next__()[:3] +
                   frames.__next__()[:3]]

            # Pixel value should be made
            # odd for 1 and even for 0
            for j in range(0, 8):
                if data_list[i][j] == '0' and pix[j] % 2 != 0:
                    pix[j] -= 1

                elif data_list[i][j] == '1' and pix[j] % 2 == 0:
                    if pix[j] != 0:
                        pix[j] -= 1
                    else:
                        pix[j] += 1
                    # pix[j] -= 1

            # Eighth pixel of every set tells
            # whether to stop ot read further.
            # 0 means keep reading; 1 means the
            # message is over.
            if i == (len(data_list) - 1):
                if pix[-1] % 2 == 0:
                    if pix[-1] != 0:
                        pix[-1] -= 1
                    else:
                        pix[-1] += 1

            else:
                if pix[-1] % 2 != 0:
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]


    def pixel_gen(new_img, data):
        w = new_img.size[0]
        (x, y) = (0, 0)

        for pixel in pixel_values(new_img.getdata(), data):

            # Putting modified pixels in the new image
            new_img.putpixel((x, y), pixel)
            if x == (w - 1):
                x = 0
                y += 1
            else:
                x += 1


    # Encode data into image
    def encrypt():
        img = img1.get()
        image = Image.open(img, 'r')

        data = data1.get()
        if len(data) == 0:
            raise ValueError('Data is empty')

        new_img = image.copy()
        pixel_gen(new_img, data)

        new_img_name = new_img1.get()
        new_img.save(new_img_name, str(new_img_name.split(".")[1].upper()))


    # Decode the data in the image
    # def decrypt(label_result):
    #     img = new_img_2_1.get()
    #     image = Image.open(img, 'r')
    #
    #     data = ''
    #     frames = iter(image.getdata())
    #
    #     while True:
    #         pixels = [value for value in frames.__next__()[:3] +
    #                   frames.__next__()[:3] +
    #                   frames.__next__()[:3]]
    #
    #         # string of binary data
    #         binary_string = ''
    #
    #         for i in pixels[:8]:
    #             if i % 2 == 0:
    #                 binary_string += '0'
    #             else:
    #                 binary_string += '1'
    #
    #         data += chr(int(binary_string, 2))
    #         if pixels[-1] % 2 != 0:
    #             label_result.config(text="Result = {}".format(data))
    #             return

    def display():
        img = new_img1.get()
        name = Image.open(img)
        img_1 = ImageTk.PhotoImage(name)
        photo_label = tkinter.Label(new5, image=img_1)
        photo_label.image = img_1
        photo_label.grid(row=15, column=1)


    # Main Function
    # def main():
    #     a = int(input(":: Welcome to Steganography ::\n"
    #                   "1. Encode\n2. Decode\n"))
    #     if (a == 1):
    #         encode()
    #
    #     elif (a == 2):
    #         print("Decoded Word :  " + decode())
    #     else:
    #         raise Exception("Enter correct input")
    #
    # # Driver Code
    # if __name__ == '__main__' :
    #
    #     # Calling main function
    #     main()


    new5 = tkinter.Toplevel(root7)
    new5.geometry("700x700")
    new5.title("Steganography")

    labelResult = tkinter.Label(new5)
    labelResult.grid(row=7, column=2)

    photoLabel = tkinter.Label(new5)
    photoLabel.grid(row=0, column=0)


    # def display(photo_label):


    img1 = tkinter.StringVar()
    data1 = tkinter.StringVar()
    new_img1 = tkinter.StringVar()
    # new_img_2_1 = tkinter.StringVar()

    img_Entry = tkinter.Entry(new5, textvariable=img1)
    img_Entry.grid(row=0, column=1)
    data_Entry = tkinter.Entry(new5, textvariable=data1)
    data_Entry.grid(row=1, column=1)
    new_img_Entry = tkinter.Entry(new5, textvariable=new_img1)
    new_img_Entry.grid(row=2, column=1)
    # new_img_2_Entry = tkinter.Entry(new5, textvariable=new_img_2_1)
    # new_img_2_Entry.grid(row=4, column=1)


    img_Label = tkinter.Label(new5, text="Enter name with extension: ")
    img_Label.grid(row=0, column=0, sticky="e")
    data_Label = tkinter.Label(new5, text="Enter data to be encoded: ")
    data_Label.grid(row=1, column=0, sticky="e")
    new_img_Label = tkinter.Label(new5, text="Enter name of new image with extension: ")
    new_img_Label.grid(row=2, column=0, sticky="e")
    # new_img_2_Label = tkinter.Label(new5, text="Enter name to decrypt with extension: ")
    # new_img_2_Label.grid(row=4, column=0, sticky="e")

    # decrypt = partial(decrypt, labelResult)

    encrypt_Button = tkinter.Button(new5, text="Encrypt", command=encrypt)
    encrypt_Button.grid(row=6, column=4)

    # decrypt_Button = tkinter.Button(new5, text="Decrypt", command=decrypt)
    # decrypt_Button.grid(row=6, column=5)

    display_Button = tkinter.Button(new5, text="Display", command=display)
    display_Button.grid(row=6, column=6)

    new5.mainloop()


def dec():
    # Convert encoding data into 8-bit binary
    # form using ASCII value of characters
    def binary_data(data):

        # list of binary codes
        # of given data
        new_data = []

        for i in data:
            new_data.append(format(ord(i), '08b'))
        return new_data


    # Pixels are modified according to the
    # 8-bit binary data and finally returned
    def pixel_values(pix, data):

        data_list = binary_data(data)
        frames = iter(pix)

        for i in range(len(data_list)):

            # Extracting 3 pixels at a time
            pix = [value for value in frames.__next__()[:3] +
                   frames.__next__()[:3] +
                   frames.__next__()[:3]]

            # Pixel value should be made
            # odd for 1 and even for 0
            for j in range(0, 8):
                if data_list[i][j] == '0' and pix[j] % 2 != 0:
                    pix[j] -= 1

                elif data_list[i][j] == '1' and pix[j] % 2 == 0:
                    if pix[j] != 0:
                        pix[j] -= 1
                    else:
                        pix[j] += 1
                    # pix[j] -= 1

            # Eighth pixel of every set tells
            # whether to stop ot read further.
            # 0 means keep reading; 1 means the
            # message is over.
            if i == (len(data_list) - 1):
                if pix[-1] % 2 == 0:
                    if pix[-1] != 0:
                        pix[-1] -= 1
                    else:
                        pix[-1] += 1

            else:
                if pix[-1] % 2 != 0:
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]


    def pixel_gen(new_img, data):
        w = new_img.size[0]
        (x, y) = (0, 0)

        for pixel in pixel_values(new_img.getdata(), data):

            # Putting modified pixels in the new image
            new_img.putpixel((x, y), pixel)
            if x == (w - 1):
                x = 0
                y += 1
            else:
                x += 1


    # Encode data into image
    # def encrypt():
    #     img = img1.get()
    #     image = Image.open(img, 'r')
    #
    #     data = data1.get()
    #     if len(data) == 0:
    #         raise ValueError('Data is empty')
    #
    #     new_img = image.copy()
    #     pixel_gen(new_img, data)
    #
    #     new_img_name = new_img1.get()
    #     new_img.save(new_img_name, str(new_img_name.split(".")[1].upper()))


    # Decode the data in the image
    def decrypt(label_result):
        img = new.get()
        image = Image.open(img, 'r')

        data = ''
        frames = iter(image.getdata())

        while True:
            pixels = [value for value in frames.__next__()[:3] +
                      frames.__next__()[:3] +
                      frames.__next__()[:3]]

            # string of binary data
            binary_string = ''
        
            for i in pixels[:8]:
                if i % 2 == 0:
                    binary_string += '0'
                else:
                    binary_string += '1'

            data += chr(int(binary_string, 2))
            if pixels[-1] % 2 != 0:
                label_result.config(text="Result = {}".format(data))
                return

    def display():
        img = new.get()
        name = Image.open(img)
        img_1 = ImageTk.PhotoImage(name)
        photo_label = tkinter.Label(new5, image=img_1)
        photo_label.image = img_1
        photo_label.grid(row=15, column=1)


        # Main Function
        # def main():
        #     a = int(input(":: Welcome to Steganography ::\n"
        #                   "1. Encode\n2. Decode\n"))
        #     if (a == 1):
        #         encode()
        #
        #     elif (a == 2):
        #         print("Decoded Word :  " + decode())
        #     else:
        #         raise Exception("Enter correct input")
        #
        # # Driver Code
        # if __name__ == '__main__' :
        #
        #     # Calling main function
        #     main()


    new5 = tkinter.Toplevel(root7)
    new5.geometry("700x700")
    new5.title("Steganography")

    labelResult = tkinter.Label(new5)
    labelResult.grid(row=7, column=2)

    photoLabel = tkinter.Label(new5)
    photoLabel.grid(row=0, column=0)


    # def display(photo_label):


    # img1 = tkinter.StringVar()
    # data1 = tkinter.StringVar()
    # new_img1 = tkinter.StringVar()
    new = tkinter.StringVar()

    # img_Entry = tkinter.Entry(new5, textvariable=img1)
    # img_Entry.grid(row=0, column=1)
    # data_Entry = tkinter.Entry(new5, textvariable=data1)
    # data_Entry.grid(row=1, column=1)
    # new_img_Entry = tkinter.Entry(new5, textvariable=new_img1)
    # new_img_Entry.grid(row=2, column=1)
    new_img_2_Entry = tkinter.Entry(new5, textvariable=new)
    new_img_2_Entry.grid(row=4, column=1)


    # img_Label = tkinter.Label(new5, text="Enter name with extension: ")
    # img_Label.grid(row=0, column=0, sticky="e")
    # data_Label = tkinter.Label(new5, text="Enter data to be encoded: ")
    # data_Label.grid(row=1, column=0, sticky="e")
    # new_img_Label = tkinter.Label(new5, text="Enter name of new image with extension: ")
    # new_img_Label.grid(row=2, column=0, sticky="e")
    new_img_2_Label = tkinter.Label(new5, text="Enter name to decrypt with extension: ")
    new_img_2_Label.grid(row=4, column=0, sticky="e")

    decrypt = partial(decrypt, labelResult)

    # encrypt_Button = tkinter.Button(new5, text="Encrypt", command=encrypt)
    # encrypt_Button.grid(row=6, column=4)

    decrypt_Button = tkinter.Button(new5, text="Decrypt", command=decrypt)
    decrypt_Button.grid(row=6, column=5)

    display_Button = tkinter.Button(new5, text="Display", command=display)
    display_Button.grid(row=6, column=6)

    new5.mainloop()


root7 = tkinter.Tk()
root7.geometry("500x500")

but = tkinter.Button(root7, text="Encrypt", command=enc)
but.grid(row=0, column=0)

but1 = tkinter.Button(root7, text="Decrypt", command=dec)
but1.grid(row=1, column=0)


root7.mainloop()
