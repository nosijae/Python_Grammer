sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """     # 이렇게 한 줄 띄고 출력할 시에 한 줄 띄고 출력된다. 
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

print("Slicing--------------------------------------")
jumin = "971116-1020100"
print("성별: " + jumin[7])
print("연: " + jumin[0:2])  # 0 부터 2 직전까지
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])
print("생년월일: " + jumin[:6])  # 처음부터 6까지
print("주민번호 뒤 7자리: " + jumin[7:])  # 7부터 끝까지
print("뒤 7자리(뒤에부터) : " + jumin[-7:] + "\n")

print("문자열 처리 함수-------------------------------------")
text = "Python is Amazing"
print(text.lower())
print(text.upper())
print(text[0].isupper())  # 설정한 인덱스 값에 위치한 문자가 대문자인가?
print(len(text))
print(text.replace("Python", "Java"))  # 찾고 싶은 문자를 찾아서 변환
index = text.index("n")  # text변수에서 n 이라는 문자가 몇번째 인덱스에 있는가?
print(index)
print(text.index("n", index + 1))  # n이라는 문자가 두번째로 어디에 위치해있는가?
print(text.find("Java"))  # find에서는 문장에 오류가 있으면 -1 출력
# print(text.index("Java"))  이문장 에러난다. 인덱스에서 원하는 값이 없으면 오류 출력
print(text.count("n"), "\n")  # n이라는 문자가 몇개 들어가 있는가?

print("문자열 포맷 -------------------------------------")
print("a" + "b")
print("a", "b")
print("방법 1 -------------------------------------")
print("\t나는 %d살입니다." % 25)
print("\t나는 %s를 좋아해요." % "파이썬")
print("\tApple은 %c로 시작해요." % "A")
# %s로 쓰면 정수, 문자 다 출력가능
print("\t나는 %s살입니다." % 25)
print("\t나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
print("방법 2 -------------------------------------")
print("\t나는 {}살입니다.".format(20))
print("\t나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("\t나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
print("방법 3 -------------------------------------")
print("\t나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("방법 4 -------------------------------------")
age = 20
color = "빨간"
print(f"\t나는 {age}살이며, {color}색을 좋아해요.\n")

print("탈출 포맷 -------------------------------------")
print("백문이 불여일견\n백견이 불여일타")
print("저는 \"나도코딩\"입니다.")
print("6\\2 = 3")
print("Red Apple\rPine")
print("Redd\bApple")    # \b 는 백슬레쉬
print("Red\tApple")
