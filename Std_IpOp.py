# print("Python", "Java", "JavaScript", sep=",", end = "?")
# print("무엇이 더 재밌을까요?")
# # end는 문장의 끝 부분을 물음표로 바꿔달라. 줄바꿈 대신 ? 가 들어간 것이다.
#
# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# 시험 성적
# scores = {"math": 0, "english": 50, "coding": 100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

# 표준 입력
answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) # 사용자 입력을 통해 받으면 항상 문자열 형태로 입력된다.
# print("입력 값은 " + answer + " 입니다. ")