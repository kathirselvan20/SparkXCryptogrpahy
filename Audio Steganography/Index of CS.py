def reading():
    print()
    with open("BOOK.txt", "r") as files:
        print(files.read())


def copies():
    print()
    with open("BOOK.txt", "r") as files:
        a = files.readlines()
        for i in a:
            b = ""
            if i[0] == "A" or i[0] == "E":
                b += i
                with open("BOOKCOPY.txt", ""
                                          "no") as files2:
                    files2.write(b)


def greater():
    print()
    with open("BOOK.txt", "r") as files:
        s = files.read()
        k = s.split()
        for i in k:
            if len(i) > 6:
                print(i)
            else:
                pass


def counting():
    print()
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    with open("BOOK.txt", "r") as files:
        a = files.read()
        for i in range(len(a)):
            if a[i].isdigit():
                cnt1 += 1
            elif a[i].isalpha():
                cnt2 += 1
            elif a[i] == " ":
                cnt3 += 1
            else:
                pass

    print("Number of digits = {}".format(cnt1))
    print("Number of alphabets = {}".format(cnt2))
    print("Number of spaces = {}".format(cnt3))


while True:
    print("1. Display \n2. To copy the lines which start with ‘A’ or ‘E’"
          "\n3. To display the words greater than 6 letters"
          "\n4. To count the number of digits, alphabets and spaces. \n0. Quit")
    ch = int(input("Enter a Choice: "))

    if ch == 1:
        reading()
        print()
    elif ch == 2:
        copies()
        print()
    elif ch == 3:
        greater()
        print()
    elif ch == 4:
        counting()
        print()
    elif ch == 0:
        break
    else:
        print()
        print("Invalid Choice")
        print()