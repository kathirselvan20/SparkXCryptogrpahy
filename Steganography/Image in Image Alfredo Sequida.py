import tkinter
from PIL import Image
from functools import partial


MAX_COLOR_VALUE = 256
MAX_BIT_VALUE = 8


def enc():
    def make_image(data, resolution):
        image = Image.new("RGB", resolution)
        image.putdata(data)

        return image

    def remove_n_least_significant_bits(value, n):
        value = value >> n
        return value << n

    def get_n_least_significant_bits(value, n):
        value = value << MAX_BIT_VALUE - n
        value = value % MAX_COLOR_VALUE
        return value >> MAX_BIT_VALUE - n

    def get_n_most_significant_bits(value, n):
        return value >> MAX_BIT_VALUE - n

    def shit_n_bits_to_8(value, n):
        return value << MAX_BIT_VALUE - n

    def encode(label_result):
        image_to_hide = Image.open(img1.get())
        image_to_hide_in = Image.open(data1.get())
        n_bits = 2
        encoded_image_path = new_img1.get()
        width, height = image_to_hide.size

        hide_image = image_to_hide.load()
        hide_in_image = image_to_hide_in.load()

        data = []

        for y in range(height):
            for x in range(width):

                # (107, 3, 10)
                # most sig bits
                r_hide, g_hide, b_hide = hide_image[x,y]

                r_hide = get_n_most_significant_bits(r_hide, n_bits)
                g_hide = get_n_most_significant_bits(g_hide, n_bits)
                b_hide = get_n_most_significant_bits(b_hide, n_bits)

                # remove lest n sig bits
                r_hide_in, g_hide_in, b_hide_in = hide_in_image[x,y]

                r_hide_in = remove_n_least_significant_bits(r_hide_in, n_bits)
                g_hide_in = remove_n_least_significant_bits(g_hide_in, n_bits)
                b_hide_in = remove_n_least_significant_bits(b_hide_in, n_bits)

                data.append((r_hide + r_hide_in,
                             g_hide + g_hide_in,
                             b_hide + b_hide_in))

        label_result.config(text="Successfully Created")
        return make_image(data, image_to_hide.size).save(encoded_image_path)

    # def decode(image_to_decode, n_bits):
    #     width, height = image_to_decode.size
    #     encoded_image = image_to_decode.load()
    #
    #     data = []
    #
    #     for y in range(height):
    #         for x in range(width):
    #
    #             r_encoded, g_encoded, b_encoded = encoded_image[x,y]
    #
    #             r_encoded = get_n_least_significant_bits(r_encoded, n_bits)
    #             g_encoded = get_n_least_significant_bits(g_encoded, n_bits)
    #             b_encoded = get_n_least_significant_bits(b_encoded, n_bits)
    #
    #             r_encoded = shit_n_bits_to_8(r_encoded, n_bits)
    #             g_encoded = shit_n_bits_to_8(g_encoded, n_bits)
    #             b_encoded = shit_n_bits_to_8(b_encoded, n_bits)
    #
    #             data.append((r_encoded, g_encoded, b_encoded))
    #
    #     return make_image(data, image_to_decode.size)
    #
    # if "__main__":
    #     image_to_hide_path = "test.png"
    #     image_to_hide_in_path = "test0.png"
    #     encoded_image_path = "test991.png"
    #     decoded_image_path = "data0.png"
    #     n_bits = 2
    #
    #     # image_to_hide = Image.open(image_to_hide_path)
    #     # image_to_hide_in = Image.open(image_to_hide_in_path)
    #     #
    #     # encode(image_to_hide, image_to_hide_in, n_bits).save(encoded_image_path)
    #
    #     image_to_decode = Image.open(encoded_image_path)
    #     decode(image_to_decode, n_bits).save(decoded_image_path)

    new5 = tkinter.Toplevel(root7)
    new5.geometry("700x700")
    new5.title("Steganography")
    new5.configure(background="black")
    new5.attributes("-fullscreen", True)

    labelResult = tkinter.Label(new5, bg="black", fg="green"
                                , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    labelResult.grid(row=7, column=1, sticky="w")

    # photoLabel = tkinter.Label(new5)
    # photoLabel.grid(row=0, column=0)


    # def display(photo_label):


    img1 = tkinter.StringVar()
    data1 = tkinter.StringVar()
    new_img1 = tkinter.StringVar()
    # new_img_2_1 = tkinter.StringVar()

    img_Entry = tkinter.Entry(new5, textvariable=img1, bg="black", fg="green"
                              , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    img_Entry.grid(row=0, column=1)
    data_Entry = tkinter.Entry(new5, textvariable=data1, bg="black", fg="green"
                               , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    data_Entry.grid(row=1, column=1)
    new_img_Entry = tkinter.Entry(new5, textvariable=new_img1, bg="black", fg="green"
                                  , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    new_img_Entry.grid(row=2, column=1)
    # new_img_2_Entry = tkinter.Entry(new5, textvariable=new_img_2_1)
    # new_img_2_Entry.grid(row=4, column=1)


    img_Label = tkinter.Label(new5, text="Enter image to hide with extension: ", bg="black", fg="green"
                              , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    img_Label.grid(row=0, column=0, sticky="e")
    data_Label = tkinter.Label(new5, text="Enter image to hide in with extension: ", bg="black", fg="green"
                               , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    data_Label.grid(row=1, column=0, sticky="e")
    new_img_Label = tkinter.Label(new5, text="Enter name of the image to save with extension: ", bg="black", fg="green"
                                  , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    new_img_Label.grid(row=2, column=0, sticky="e")
    # new_img_2_Label = tkinter.Label(new5, text="Enter name to decrypt with extension: ")
    # new_img_2_Label.grid(row=4, column=0, sticky="e")

    # decrypt = partial(decrypt, labelResult)
    encode = partial(encode, labelResult)
    encrypt_Button = tkinter.Button(new5, text="Encrypt", command=encode, bg="black", fg="green"
                                    , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    encrypt_Button.grid(row=6, column=4)

    # decrypt_Button = tkinter.Button(new5, text="Decrypt", command=decrypt)
    # decrypt_Button.grid(row=6, column=5)

    # display_Button = tkinter.Button(new5, text="Display", command=display)
    # display_Button.grid(row=6, column=6)

    new5.mainloop()


def dec():
    def make_image(data, resolution):
        image = Image.new("RGB", resolution)
        image.putdata(data)

        return image

    def remove_n_least_significant_bits(value, n):
        value = value >> n
        return value << n

    def get_n_least_significant_bits(value, n):
        value = value << MAX_BIT_VALUE - n
        value = value % MAX_COLOR_VALUE
        return value >> MAX_BIT_VALUE - n

    def get_n_most_significant_bits(value, n):
        return value >> MAX_BIT_VALUE - n

    def shit_n_bits_to_8(value, n):
        return value << MAX_BIT_VALUE - n

    # def encode(image_to_hide, image_to_hide_in, n_bits):
    #
    #     width, height = image_to_hide.size
    #
    #     hide_image = image_to_hide.load()
    #     hide_in_image = image_to_hide_in.load()
    #
    #     data = []
    #
    #     for y in range(height):
    #         for x in range(width):
    #
    #             # (107, 3, 10)
    #             # most sig bits
    #             r_hide, g_hide, b_hide = hide_image[x,y]
    #
    #             r_hide = get_n_most_significant_bits(r_hide, n_bits)
    #             g_hide = get_n_most_significant_bits(g_hide, n_bits)
    #             b_hide = get_n_most_significant_bits(b_hide, n_bits)
    #
    #             # remove lest n sig bits
    #             r_hide_in, g_hide_in, b_hide_in = hide_in_image[x,y]
    #
    #             r_hide_in = remove_n_least_significant_bits(r_hide_in, n_bits)
    #             g_hide_in = remove_n_least_significant_bits(g_hide_in, n_bits)
    #             b_hide_in = remove_n_least_significant_bits(b_hide_in, n_bits)
    #
    #             data.append((r_hide + r_hide_in,
    #                          g_hide + g_hide_in,
    #                          b_hide + b_hide_in))
    #
    #     return make_image(data, image_to_hide.size)

    def decode(label_result):
        image_to_decode = Image.open(new.get())
        n_bits = 2
        width, height = image_to_decode.size
        encoded_image = image_to_decode.load()
        decoded_image_path = tab.get()
        data = []

        for y in range(height):
            for x in range(width):

                r_encoded, g_encoded, b_encoded = encoded_image[x,y]

                r_encoded = get_n_least_significant_bits(r_encoded, n_bits)
                g_encoded = get_n_least_significant_bits(g_encoded, n_bits)
                b_encoded = get_n_least_significant_bits(b_encoded, n_bits)

                r_encoded = shit_n_bits_to_8(r_encoded, n_bits)
                g_encoded = shit_n_bits_to_8(g_encoded, n_bits)
                b_encoded = shit_n_bits_to_8(b_encoded, n_bits)

                data.append((r_encoded, g_encoded, b_encoded))

        label_result.config(text="Successfully Decrypted")
        return make_image(data, image_to_decode.size).save(decoded_image_path)

    # if "__main__":
    #     image_to_hide_path = "test.png"
    #     image_to_hide_in_path = "test0.png"
    #     encoded_image_path = "test991.png"
    #     decoded_image_path = "data0.png"
    #     n_bits = 2
    #
    #     # image_to_hide = Image.open(image_to_hide_path)
    #     # image_to_hide_in = Image.open(image_to_hide_in_path)
    #     #
    #     # encode(image_to_hide, image_to_hide_in, n_bits).save(encoded_image_path)
    #
    #     image_to_decode = Image.open(encoded_image_path)
    #     decode(image_to_decode, n_bits).save(decoded_image_path)

    new5 = tkinter.Toplevel(root7)
    new5.geometry("700x700")
    new5.title("Steganography")
    new5.configure(background="black")
    new5.attributes("-fullscreen", True)

    labelResult = tkinter.Label(new5, bg="black", fg="green"
                                , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    labelResult.grid(row=7, column=1, sticky="w")

    # photoLabel = tkinter.Label(new5)
    # photoLabel.grid(row=0, column=0)


    # def display(photo_label):


    # img1 = tkinter.StringVar()
    # data1 = tkinter.StringVar()
    # new_img1 = tkinter.StringVar()
    new = tkinter.StringVar()
    new7 = tkinter.StringVar()

    # img_Entry = tkinter.Entry(new5, textvariable=img1)
    # img_Entry.grid(row=0, column=1)
    # data_Entry = tkinter.Entry(new5, textvariable=data1)
    # data_Entry.grid(row=1, column=1)
    # new_img_Entry = tkinter.Entry(new5, textvariable=new_img1)
    # new_img_Entry.grid(row=2, column=1)
    new_img_2_Entry = tkinter.Entry(new5, textvariable=new, bg="black", fg="green"
                                    , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    new_img_2_Entry.grid(row=4, column=1)

    tab = tkinter.Entry(new5, textvariable=new7, bg="black", fg="green"
                        , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    tab.grid(row=5, column=1)

    # img_Label = tkinter.Label(new5, text="Enter name with extension: ")
    # img_Label.grid(row=0, column=0, sticky="e")
    # data_Label = tkinter.Label(new5, text="Enter data to be encoded: ")
    # data_Label.grid(row=1, column=0, sticky="e")
    # new_img_Label = tkinter.Label(new5, text="Enter name of new image with extension: ")
    # new_img_Label.grid(row=2, column=0, sticky="e")
    new_img_2_Label = tkinter.Label(new5, text="Enter image to decrypt with extension: ", bg="black", fg="green"
                                    , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    new_img_2_Label.grid(row=4, column=0, sticky="e")
    tab_label = tkinter.Label(new5, text="Enter name to save decrypted image with extension: ", bg="black", fg="green"
                              , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    tab_label.grid(row=5, column=0, sticky="e")

    decode = partial(decode, labelResult)

    # encrypt_Button = tkinter.Button(new5, text="Encrypt", command=encrypt)
    # encrypt_Button.grid(row=6, column=4)

    decrypt_Button = tkinter.Button(new5, text="Decrypt", command=decode, bg="black", fg="green"
                                    , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    decrypt_Button.grid(row=6, column=5, sticky="ew")

    # display_Button = tkinter.Button(new5, text="Display", command=display)
    # display_Button.grid(row=6, column=6)

    new5.mainloop()

root7 = tkinter.Tk()
root7.geometry("500x500")
root7.configure(background="black")

but = tkinter.Button(root7, text="Encrypt", command=enc, bg="black", fg="green"
                     , font=("ALGERIAN", 24, "bold"), relief="raised", borderwidth=15)
but.grid(row=0, column=0)

but1 = tkinter.Button(root7, text="Decrypt", command=dec, bg="black", fg="green"
                      , font=("ALGERIAN", 24, "bold"), relief="raised", borderwidth=15)
but1.grid(row=1, column=0)


root7.mainloop()
