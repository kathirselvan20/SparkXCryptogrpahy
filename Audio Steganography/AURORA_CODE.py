# We will use wave package available in native Python installation to read and write .wav audio file
import wave
import tkinter
from functools import partial


def e():
    def encode(label_result):
        a = img.get()
        string = message.get()
        c = new_img.get()

        # read wave audio file
        song = wave.open(a, mode='rb')
        # Read frames and convert to byte array
        frame_bytes = bytearray(list(song.readframes(song.getnframes())))

        # The "secret" text message
        # string='Peter Parker is the Spiderman!'
        # Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters.
        string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
        # Convert text to bit array
        bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))

        # Replace LSB of each byte of the audio data by one bit from the text bit array
        for i, bit in enumerate(bits):
            frame_bytes[i] = (frame_bytes[i] & 254) | bit
        # Get the modified bytes
        frame_modified = bytes(frame_bytes)

        # Write bytes to a new wave audio file
        with wave.open(c, 'wb') as fd:
            fd.setparams(song.getparams())
            fd.writeframes(frame_modified)
        label_result.config(text="Successfully Encrypted")
        song.close()

    def play():
        s = img.get()
    # def decode(label_result):
    #     song = wave.open("song_embedded.wav", mode='rb')
    #     # Convert audio to byte array
    #     frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    #
    #     # Extract the LSB of each byte
    #     extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    #     # Convert byte array back to string
    #     string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
    #     # Cut off at the filler characters
    #     decoded = string.split("###")[0]
    #
    #     # Print the extracted text
    #     print("Sucessfully decoded: " + decoded)
    #     song.close()


    mainWindow = tkinter.Toplevel(root)
    mainWindow.geometry("500x500")
    mainWindow.configure(background="black")

    img = tkinter.StringVar()
    message = tkinter.StringVar()
    new_img = tkinter.StringVar()

    imgLabel = tkinter.Label(mainWindow, text="Enter name of audio file - ", bg="black", fg="green"
                             , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    imgLabel.grid(row=0, column=0)

    messageLabel = tkinter.Label(mainWindow, text="Enter message to be encoded - ", bg="black", fg="green"
                                 , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    messageLabel.grid(row=1, column=0)

    new_imgLabel = tkinter.Label(mainWindow, text="Enter a new name to save audio file - ", bg="black", fg="green"
                                 , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    new_imgLabel.grid(row=2, column=0)

    imgEntry = tkinter.Entry(mainWindow, textvariable=img, bg="black", fg="green"
                             , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    imgEntry.grid(row=0, column=1)

    messageEntry = tkinter.Entry(mainWindow, textvariable=message, bg="black", fg="green"
                                 , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    messageEntry.grid(row=1, column=1)

    new_imgEntry = tkinter.Entry(mainWindow, textvariable=new_img, bg="black", fg="green"
                                 , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    new_imgEntry.grid(row=2, column=1)

    labelResult = tkinter.Label(mainWindow, bg="black", fg="green"
                                , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    labelResult.grid(row=4, column=4)

    encode = partial(encode, labelResult)
    # decode = partial(decode, labelResult)

    e_Button = tkinter.Button(mainWindow, text="Encrypt", command=encode, bg="black", fg="green"
                              , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    e_Button.grid(row=3, column=3)

    mainWindow.attributes("-fullscreen", True)

    mainWindow.mainloop()


def d():
    # def encode(label_result):
    #     # read wave audio file
    #     song = wave.open("The One and Only Paradise 21 guns Still Breathing.wav", mode='rb')
    #     # Read frames and convert to byte array
    #     frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    #
    #     # The "secret" text message
    #     string='Peter Parker is the Spiderman!'
    #     # Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters.
    #     string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
    #     # Convert text to bit array
    #     bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
    #
    #     # Replace LSB of each byte of the audio data by one bit from the text bit array
    #     for i, bit in enumerate(bits):
    #         frame_bytes[i] = (frame_bytes[i] & 254) | bit
    #     # Get the modified bytes
    #     frame_modified = bytes(frame_bytes)
    #
    #     # Write bytes to a new wave audio file
    #     with wave.open('song_embedded.wav', 'wb') as fd:
    #         fd.setparams(song.getparams())
    #         fd.writeframes(frame_modified)
    #     label_result.config(text="Successfully Encrypted")
    #     song.close()

    def decode(label_result):
        a = img.get()
        song = wave.open(a, mode='rb')
        # Convert audio to byte array
        frame_bytes = bytearray(list(song.readframes(song.getnframes())))

        # Extract the LSB of each byte
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        # Convert byte array back to string
        string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
        # Cut off at the filler characters
        decoded = string.split("###")[0]

        # Print the extracted text
        label_result.config(text="Sucessfully decoded: {}".format(decoded))
        song.close()

    mainWindow = tkinter.Toplevel(root)
    mainWindow.geometry("500x500")
    mainWindow.configure(background="black")
    mainWindow.attributes("-fullscreen", True)

    img = tkinter.StringVar()

    imgLabel = tkinter.Label(mainWindow, text="Enter name of audio file - ", bg="black", fg="green"
                             , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    imgLabel.grid(row=0, column=0, sticky="w")

    imgEntry = tkinter.Entry(mainWindow, textvariable=img, bg="black", fg="green"
                             , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    imgEntry.grid(row=0, column=1, sticky="w")

    labelResult = tkinter.Label(mainWindow, bg="black", fg="green"
                                , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    labelResult.grid(row=4, column=0, sticky="w")

    # encode = partial(encode, labelResult)
    decode = partial(decode, labelResult)

    d_Button = tkinter.Button(mainWindow, text="Decrypt", command=decode, bg="black", fg="green"
                              , font=("ALGERIAN", 20, "bold"), relief="raised", borderwidth=5)
    d_Button.grid(row=3, column=3, sticky="w")

    mainWindow.mainloop()


root = tkinter.Tk()
root.geometry("500x500")
root.configure(background="black")

e_Button = tkinter.Button(root, text="Encrypt", command=e, bg="black", fg="green"
                          , font=("ALGERIAN", 24, "bold"), relief="raised", borderwidth=15)
e_Button.grid(row=0, column=0)

d_Button = tkinter.Button(root, text="Decrypt", command=d, bg="black", fg="green"
                          , font=("ALGERIAN", 24, "bold"), relief="raised", borderwidth=15)
d_Button.grid(row=1, column=0)

root.mainloop()
