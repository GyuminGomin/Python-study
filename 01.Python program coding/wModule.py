def repeatWhile(n) :
    while True:
        try:
            N = int(input("첫 번째 리스트 크기 1<={0}<=100을 입력하세요. : ".format(n)))
            if N < 1 or N > 100:
                print("{}의 범위는 1 이상 100 이하 입니다.".format(n))
                continue
        except ValueError:
            print("숫자를 입력해 주세요.")
            continue
        else:
            break
    return N