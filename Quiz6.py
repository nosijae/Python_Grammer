# 표준 체중 구하기

# def std_weight(height, gender):
#     if gender == "man":
#         weight = round(float(height * height * 22/10000), 2)
#     elif gender == "woman":
#         weight = round(float(height * height * 21/10000), 2)
#     result = "키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight)
#     return result
#
# info = input().split()
# result = std_weight(int(info[0]), info[1])
# print(result)

def std_weight(height, gender):  # 키는 m단위 (실수)
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21


height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight, 2))
