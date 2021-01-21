# 배열 []
print("배열 ---------------------------------------------")
subway = ["재석", "홍철", "명수"]
print("타있는 사람:", subway)
print("홍철이는 %d번째 칸에 타있다" % subway.index("홍철"))
print("하하 탑승")
subway.append("하하")
print(subway)
print("형돈 탑승")
subway.insert(1, "형돈")
print(subway)
print("%s 하차" % subway.pop())
print(subway)

subway.append("재석")
print(subway.count("재석"), "\n")

print("정렬 ---------------------------------------------")
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)
print("반대 정렬 ---------------------------------------------")
num_list.reverse()
print(num_list)
print("모두 지우기 ---------------------------------------------")
num_list.clear()
print(num_list, "\n")

print("다양한 자료형 함께 사용 ---------------------------------------------")
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]
print(mix_list)
num_list.extend(mix_list)
print(num_list, "\n")

print("사전 자료형 ---------------------------------------------")
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet[6]) # 할당하지 않은 키를 추출하려 하면 에러 발생한다.
print(cabinet.get(5))  # get함수 사용하면 값이 없을때 None 출력
print(cabinet.get(5, "사용 가능"))
print(3 in cabinet)
print(6 in cabinet, "\n")

print("사전 자료형2 ---------------------------------------------")
cabinet2 = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet2)
print("\tA-3의 손님은 %s" % cabinet2["A-3"])
print("\tB-100의 손님은 %s" % cabinet2["B-100"])
print("새 손님: 조세호, 바뀐 승객: 유재석 -> 김종국")
cabinet2["A-3"] = "김종국"
cabinet2["C-20"] = "조세호"
print("\t", cabinet2)
print("간 손님: 김종국")
del cabinet2["A-3"]
print("\t", cabinet2)
print("key들만 출력")
print("\t", cabinet2.keys())
print("value들만 출력")
print("\t", cabinet2.values())
print("key, value 쌍으로 출력")
print("\t", cabinet2.items())
print("캐비넷 안의 모든 값 지우기")
cabinet.clear()
print("\t",cabinet)
