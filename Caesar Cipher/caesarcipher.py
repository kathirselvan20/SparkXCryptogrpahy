def shift_encryption(a, num):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    b = ""
    for k in range(len(a)):
        if a[k].lower() in alphabets:
            for j in range(len(alphabets)):
                try:
                    if a[k].lower() == alphabets[j]:
                        b += alphabets[j + num]

                except IndexError:
                    j = len(alphabets[j:-1])
                    print(j)
                    b += alphabets[(-1 * (j - num)) - 1]
        elif a[k] == " ":
            b += " "

    print(b)


def shift_decryption(a, num):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    b = ""
    for k in range(len(a)):
        if a[k].lower() in alphabets:
            for j in range(len(alphabets)):

                if a[k].lower() == alphabets[j]:
                    b += alphabets[j - num]

        elif a[k] == " ":
            b += " "

    print(b)


while True:
    print("Choose 1. Encrypt 2. Decrypt")
    ch = int(input())
    if ch == 2:
        print("Enter Cipher to decrypt: ")
        text = input()
        print("Do you have the shift key 1. Yes 2. No")
        choice = int(input())
        if choice == 1:
            key = int(input("Enter Shift Key: "))
            shift_decryption(text, key)
            break
        elif choice == 2:
            for i in range(26):
                shift_decryption(text, i)
                print()
            break
    elif ch == 1:
        text = input("Enter Cipher to encrypt: ")
        key = int(input("Enter Shift Key: "))
        shift_encryption(text, key)
        break
    else:
        print()
