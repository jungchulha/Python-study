
# 틀린 문자 찾기
#
# 두 개의 문자열이 주어집니다. 이때 두번째 문자열은 첫번째 문자열에 하나의 문자를 추가 한 후, 그 순서를 랜덤하게 뒤섞은 문자입니다. 이때 추가된 문자를 찾아 보도록 합시다.
#
# 예를 들어서, apple 과 azlppe 가 주어졌을 경우 추가된 문자는 z입니다.
#  • 추가된 문자는 하나라고 가정해도 좋습니다.
#  • 추가된 문자가 이미 리스트에 존재하던 문자 일 수도 있습니다.

def findDifference(str1, str2):
    chHash = {}
    for ch in str2:
        if ch in chHash:
            chHash[ch] += 1
        else:
            chHash[ch] = 1

    for ch in str1:
        if ch in chHash:
            chHash[ch] -= 1

    for ch in str2:
        if chHash[ch] == 1:
            return ch

    return -1


def main():
    print(findDifference('apple', 'azlppe'))
    print(findDifference('student', 'students'))


if __name__ == "__main__":
    main()


