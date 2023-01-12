# import csv
#
# # fields = []
# # row = []
# #
# # with open("hello.csv", "r") as csv_files:
# #     c = csv.reader(csv_files)
# #
# #     for i in next(c):
# #         fields.append(i)
# #
# #     for rows in c:
# #         row.append(rows)
# #
# # print(fields)
# # print(rows)
#
#
# # myDict = [{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
# #          {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
# #          {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
# #          {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
# #          {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
# #          {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]
# #
# # fields = ["name", "branch", "year", "cgpa"]
# #
# # with open("audit.csv", "w") as files:
# #     csv_write = csv.DictWriter(files, fieldnames=fields)
# #
# #     csv_write.writeheader()
# #
# #     csv_write.writerows(myDict)
#
# # with open("spam.csv", "w") as files:
# #     csv_writer = csv.writer(files)
# #     csv_writer.writerow([1, 2, 4, 5, 6])
#
# # a = "good morning class"
# # b = ''
# # i = 1
# # b += a[0].upper()
# # while i < len(a):
# #     if a[i] == " ":
# #         b = b + " " + a[i + 1].upper()
# #         i = i + 2
# #     else:
# #         b += a[i]
# #         i += 1
# #
# # print(b)
#
# # def phishing():
# #     num = int(input("How many times should a word be there to consider the word recurring: "))
# #     m = []
# #     b = []
# #     dict2 = {}
# #     with open("Poem.txt", "r") as files:
# #         s = files.readlines()
# #         for i in s:
# #             a = i.split()
# #             for j in a:
# #                 m.append(j)
# #
# #     for i in m:
# #         if i not in b:
# #             b.append(i)
# #     cnt = 0
# #     for i in b:
# #         for j in range(len(m)):
# #             if i == m[j]:
# #                 cnt += 1
# #         dict2[i] = cnt
# #         cnt = 0
# #
# #     print(dict2)
# #
# #     for i, (j, k) in enumerate(dict2.items()):
# #         if k > num:
# #             print(j, "recurs", k, "times")
# #
# #
# # with open("poem.txt", "r") as files:
# #     s = files.readlines()
# #     for i, j in enumerate(s):
# #         print((i + 1), j)
#
# # def replace():
# #     k = []
# #     with open("savie.txt", "r") as files:
# #         s = files.readlines()
# #         for i in s:
# #             k.append(i.split())
# #
# #     for i in k:
# #         for j in range(len(i)):
# #             if i[j].lower() == "delhi":
# #                 i[j] = "New Delhi"
# #
# #     print(k)
# #
# #     with open("savie.txt", "w") as files:
# #         str1 = ""
# #         for i in k:
# #             for j in i:
# #                 str1 += j + " "
# #             print(str1)
# #             str1 = ""
# #
# #
# # replace()
#
# # a = [['delhi'], ['i', 'live', 'in', 'delhi'], ['capital', 'is', 'delhi']]
# # for i in a:
# #     for j in range(len(i)):
# #         if i[j] == "delhi":
# #             i[j] = "New Delhi"
# #
# # print(a)
#
# # str1 = ""
# # list1 = [['delhi'], ['i', 'live', 'in', 'delhi'], ['capital', 'is', 'delhi']]
# # for i in list1:
# #     for j in i:
# #         str1 += j + " "
# #     print(str1)
# #     str1 = ""
#
# # def replace:
# #     with open("savie.txt", "r") as files:
# #         s = files.readline()
# #         if "delhi" in s:
# #
# #             s.replace("delhi", "New Delhi")
# import pickle
# import os
#
# import csv
# def write():
#     ob=open("student.csv","w")
#     csv_writer=csv.writer(ob)
#     rollno=input("enter a roll no")
#     name=input("enter a name")
#     stream=input("enter a stream")
#     marks=input("enter marks")
#     csv_writer.writerow([rollno,name,stream,marks])
# def read():
#     ob=open("student.csv","r")
#     csv_reader=csv.reader(ob)
#     for i in csv_reader:
#         print(i)
#
# def search():
#     ob=open("student.csv","r")
#     found=0
#     csv_reader=csv.reader(ob)
#     no=input("enter no to search by")
#     for i in csv_reader:
#         if i[0] == no:
#             found=1
#             print(i)
#         else:
#             pass
#     if found==0:
#         print("not found")
#     ob.close()
# search()
#
#
# start = int(input('Enter lower limit: '))
# stop = int(input('Enter upper limit: '))
# while start < stop:
#     b = 2
#     while b < start:
#         if start % b == 0:
#             break
#         b += 1
#     else:
#         print(start)
#     start += 1
#

# def jack(arg):
#     arg = arg.lower()
#     l = arg.split()
#     c1 = l.count("cat")
#     c2 = l.count("dog")
#     if c1 == c2:
#         return "True"
#     else:
#         return "False"
#
#
# b = jack("ca dog cat do d Trip flip cat")
# print(b)

# val = int(input('Enter a number: '))
# fact = 1
# for i in range(1, val + 1):
#     fact *= i
#
# print(fact)
vow = 0
cons = 0
upper = 0
lower = 0
digits = 0

# with open("story.txt", "r") as files:
#     s = files.read()
#     for i in s:
#         if i.isupper():
#             upper += 1
#             if i in "AEIOU":
#                 vow += 1
#             else:
#                 cons += 1
#
#         elif i.islower():
#             lower += 1
#             if i in "aeiou":
#                 vow +=1
#             else:
#                 cons+=1
#
#         elif i.isdigit():
#             digits += 1
#
# print(vow, cons, upper, lower, digits)
# word = 0
# words = 0
# with open("story.txt", "r") as files:
#     s = files.read()
#     k = s.split()
#     for i in k:
#         if "He" == i:
#             word += 1
#         elif "She" in i:
#             words += 1
#
# print(word, words)

obj = open("data.txt"); GG = 0
data = obj.readline()
while data:
    if len(data) < 20:
        GG += len(data.strip())
    data = obj.readline()

print(GG); obj.close()
