import sys

option = sys.argv[1]

if option == '-a' :
    memo = sys.argv[2]
    f = open('memo.txt', 'a', encoding='UTF-8')
    f.write(memo)
    f.write("\n")
    f.close()
elif option == '-v' :
    f = open('memo.txt', 'r', encoding='UTF-8')
    memo = f.read()
    f.close()
    print(memo)