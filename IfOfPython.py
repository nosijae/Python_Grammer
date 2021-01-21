print("if 문")
# weather = input("오늘 날씨: ")
#
# if weather == "비" or weather == "눈":
#     print("우산을 챙겨라")
# elif weather == "미세먼지":
#     print("마스크를 챙겨라")
# else:
#     print("준비물 필요 없어요")
temp = int(input("Temperature: "))
if 30 <= temp:
    print("Too Hot")
elif temp >= 10 and temp < 30:
    print("Fine")
elif 0 <= temp < 10:
    print("Cold")
else:
    print("Too Cold")
