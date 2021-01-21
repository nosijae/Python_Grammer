# 비밀번호 자동 생성기

site = "http://naver.com"
# modified_site = site[site.index("/") + 2:site.index(".")]
# print("생성된 비밀번호 : %s" % modified_site[:3] + str(len(modified_site)) + str(modified_site.count('e')) + "!")

modified_site = site.replace("http://", "")
modified_site = modified_site[:modified_site.index(".")]
password = modified_site[:3] + str(len(modified_site)) + str(modified_site.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(site, password))
