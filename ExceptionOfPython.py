# 예외 처리 (에러 발생시 그에 대한 처리)
try:
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값 입력")
except ZeroDivisionError as err:
    print(err)
except:
    print("알 수 없는 에러 발생")