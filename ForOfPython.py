# print("for ---------------------------------------")
# for i in range(1, 6):
#     print("대기번호: {0}".format(i))
# print()
#
# cafe = ["audu", "kim", "noh", "won"]
# for i in cafe:
#     print("{0}, 커피가 준비되었습니다.".format(i))
#
# print("\nwhile ---------------------------------------")
# customer = "Thor"
# index = 5
# while index >= 1:
#     print("{0}, coffee ready. {1} left".format(customer, index))
#     if index == 0:
#         print("coffee discard")
#     index -= 1
#
# print("\nwhile_example ---------------------------------------")
# person = "Unknown"
# while person != customer:
#     print("{0}, coffee ready.".format(customer))
#     person = input("name: ")

# continue and break
# absent = [2, 5]
# no_book = [7]
# for i in range(1,11):
#     if i in absent:
#         print("{0}, absent".format(i))
#         continue
#     elif i in no_book:
#         print("Class Done. {0} Follow me".format(i))
#         break
#     print("{0}, read the book".format(i))

# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i + 100 for i in students]
# print(students)
#
# # students to length
# students = ["Iron", "ThorGod", "Groot"]
# students = [len(i) for i in students]
# print(students)

students = ["Iron", "Thor", "Groot"]
students = [i.upper() for i in students]
print(students)