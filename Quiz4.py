from random import *

comment = range(1,21)   # 1부터 20까지 숫자 생성
comment = list(comment)
print(type(comment), "\n")

shuffle(comment)
winners = sample(comment, 4)

print(" --당첨자 발표-- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" --축하합니다-- ")
