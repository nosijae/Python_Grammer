# with open("study.txt", "w", encoding = "utf8") as study_file:
#     study_file.write(("파이썬을 열심히 공부하고 있어"))


for i in range(1, 51):
    with open("{0} 주차.txt".format(i), "w", encoding="utf8") as Week_file:
        Week_file.write("- {0} 주차 주간보고 -".format(i))
        Week_file.write("\n부서 : ")
        Week_file.write("\n이름 : ")
        Week_file.write("\n업무 요약 : ")
