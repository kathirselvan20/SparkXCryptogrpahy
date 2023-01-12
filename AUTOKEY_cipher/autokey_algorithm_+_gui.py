import tkinter
from functools import partial

ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# def main():
#     message = input('enter message:\n')
#     key = input('enter your key:\n')
#     mode = input('encrypt or decrypt\n')
#     ## if len(key) < len(message):
#     ## key = key[0:] + message[:100]
#     #print(key)
#     if mode == 'encrypt':
#         encryptMessage(message, key)
#     elif mode == 'decrypt':
#         decryptMessage(message, key)
#     #print(' message:',  (mode.title()))
#     # print(cipher)


## def encryptMessage (keys, messages):
##     return cipherMessage(keys, messages, 'encrypt')
def encryptMessage(label_result):
    messages = code.get()
    keys = shift_key.get()

    cipher = []
    k_index = 0
    key = keys.upper()
    for i in messages:
        text = ALPHA.find(i.upper())
        ## if text != -1:
        # if mode == 'encrypt':
        text += ALPHA.find(key[k_index])
        key += i.upper()  # add current char to keystream

        # elif mode == 'decrypt':
        #     text -= ALPHA.find(key[k_index])
        #     key += ALPHA[text]  # add current char to keystream
        text %= len(ALPHA)
        ## k_index += -1
        k_index += 1
        ## if k_index == len(key):
        ##     k_index = 0
        ## else:
        cipher.append(ALPHA[text])
    label_result.config(text="Result = {}".format(''.join(cipher)))


## def decryptMessage(keys,messages):
##     return cipherMessage(keys, messages, 'decrypt')
def decryptMessage(label_result):
    messages = code.get()
    keys = shift_key.get()

    cipher = []
    k_index = 0
    key = keys.upper()
    for i in messages:
        text = ALPHA.find(i.upper())
        ## if text != -1:
        # if mode == 'encrypt':
        # text += ALPHA.find(key[k_index])
        # key += i.upper()  # add current char to keystream

        # elif mode == 'decrypt':
        text -= ALPHA.find(key[k_index])
        key += ALPHA[text]  # add current char to keystream
        text %= len(ALPHA)
        ## k_index += -1
        k_index += 1
        ## if k_index == len(key):
        ##     k_index = 0
        ## else:
        cipher.append(ALPHA[text])
    label_result.config(text="Result = {}".format(''.join(cipher)))


#
# ## def cipherMessage (keys, messages, mode):
# def cipherMessage (messages, keys):
#     cipher = []
#     k_index = 0
#     key = keys.upper()
#     for i in messages:
#         text = ALPHA.find(i.upper())
#         ## if text != -1:
#         # if mode == 'encrypt':
#         text += ALPHA.find(key[k_index])
#         key += i.upper()  # add current char to keystream
#
#         # elif mode == 'decrypt':
#         #     text -= ALPHA.find(key[k_index])
#         #     key += ALPHA[text]  # add current char to keystream
#         text %= len(ALPHA)
#         ## k_index += -1
#         k_index += 1
#         ## if k_index == len(key):
#         ##     k_index = 0
#         ## else:
#         cipher.append(ALPHA[text])
#     return ''.join(cipher)

# if __name__ == "__main__":
#     main()

mainWindow = tkinter.Tk()
mainWindow.geometry("500x500")
mainWindow.title("Rail Fence")

code = tkinter.StringVar()
shift_key = tkinter.StringVar()

codeLabel = tkinter.Label(mainWindow, text="Message - ")
codeLabel.grid(row=0, column=0)

shift_keyLabel = tkinter.Label(mainWindow, text="Key - ")
shift_keyLabel.grid(row=1, column=0)

codeEntry = tkinter.Entry(mainWindow, textvariable=code).grid(row=0, column=1)
shift_keyEntry = tkinter.Entry(mainWindow, textvariable=shift_key).grid(row=1, column=1)

labelResult = tkinter.Label(mainWindow)
labelResult.grid(row=7, column=4)

encryptMessage = partial(encryptMessage, labelResult)
decryptMessage = partial(decryptMessage, labelResult)

encryptButton = tkinter.Button(mainWindow, text="Encrypt", command=encryptMessage).grid(row=2, column=3)
decryptButton = tkinter.Button(mainWindow, text="Decrypt", command=decryptMessage).grid(row=2, column=4)

mainWindow.mainloop()
