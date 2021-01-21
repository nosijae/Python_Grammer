print("집합(중복 안됨, 순서 없음)")
my_set = {1,2,3,3,3}
print(my_set, "\n")   # 중복 허용하지 않기 때문에 3이 3개임에도 불구하고 1개만 출력

java = {"you", "kim", "yang"}
python = set(["you", "park"])
# 교집합 (java, python 모두 가능)
print(java & python)
print(java.intersection(python), "\n")

# 합집합 (java 할 수 있고, python도 할 수 있는 개발자)
print(java | python)
print(java.union(python), "\n")

# 차집합 (java는 할 수 있지만, python은 못하는 개발자)
print(java-python)
print(java.difference(python), "\n")

# python 가능자가 늘어남
python.add("Kim")
print(python)

# java 까먹음
java.remove("kim")

