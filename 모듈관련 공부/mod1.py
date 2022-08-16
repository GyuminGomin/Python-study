def add(a,b) :
    return a+b
def sub(a,b) :
    return a-b

if __name__ == "__main__" :
    print(add(1, 4))
    print(sub(4, 2))
    # 직접 이 파일을 실행했을 때는 if문이 참이되어 아랫 문장이 실행된다.
    # 대화형 인터프리터나 다른 파일에서 이 모듈을 불러올때는 거짓이 되어 실행되지 않는다.
