# Q16. 모스 부호 해독
"""
문자열 형식으로 입력받은 모스 부호(dot:. dash:-)를 해독하여 영어 문장으로 출력하는 프로그램
을 작성하시오.
- 글자와 글자 사이는 공백 1개, 단어와 단어 사이는 공백 2개로 구분한다.
- 예를 들어 다음 모스 부호는 "HE SLEEPS EARLY"로 해석해야 한다.
.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--
모스 부호 규칙 표
A .-        N -.
B -...      O ---
C -.-.      P .--.
D -..       Q --.-
E .         R .-.
F ..-.      S ...
G --.       T -
H ....      U ..-
I ..        V ...-
J .---      W .--
K -.-       X -..-
L .-..      Y -.--
M --        Z --..
"""

def morse_code() :
    while True :
        inp = input("(모스부호)\n(단어와 단어 사이는 공백 2개, 글자와 글자 사이는 공백 1개)\n.과-만 입력하시오 : ")
        inp_list_2 = inp.split('  ')  # 2개 스페이스
        result = ''  # inp을 변환 시켜주는 결과값
        output = ''
        running = True
        for i, name in enumerate(inp_list_2) :
            inp_list = inp_list_2[i]
            inp_list = inp_list.split(' ')
            for j, name in enumerate(inp_list) :
                result = name
                if result == '.-' :
                    output += 'A'
                elif result == '-...' :
                    output += 'B'
                elif result == '-.-.' :
                    output += 'C'
                elif result == '-..' :
                    output += 'D'
                elif result == '.' :
                    output += 'E'
                elif result == '..-.' :
                    output += 'F'
                elif result == '--.' :
                    output += 'G'
                elif result == '....' :
                    output += 'H'
                elif result == '..' :
                    output += 'I'
                elif result == '.---' :
                    output += 'J'
                elif result == '-.-' :
                    output += 'K'
                elif result == '.-..' :
                    output += 'L'
                elif result == '--' :
                    output += 'M'
                elif result == '-.' :
                    output += 'N'
                elif result == '---' :
                    output += 'O'
                elif result == '.--.' :
                    output += 'P'
                elif result == '--.-' :
                    output += 'Q'
                elif result == '.-.' :
                    output += 'R'
                elif result == '...' :
                    output += 'S'
                elif result == '-' :
                    output += 'T'
                elif result == '..-' :
                    output += 'U'
                elif result == '...-' :
                    output += 'V'
                elif result == '.--' :
                    output += 'W'
                elif result == '-..-' :
                    output += 'X'
                elif result == '-.--' :
                    output += 'Y'
                elif result == '--..' :
                    output += 'Z'
                else :
                    print("잘못된 모스부호입니다. 다시입력해주세요.")
                    print('---------------------------------')
                    running = False
                    break
            if running == False :
                break
            if i != len(inp_list_2)-1 :
                output += ' '
        if running == True :
            print(output)
            break

# morse_code()


# Q.17 기초 메타 문자
"""
다음 중 정규식 a[.]{3,}b과 매치되는 문자열은 무엇일까?
1. acccb
2. a....b
3. aaab
4. a.cccb
"""