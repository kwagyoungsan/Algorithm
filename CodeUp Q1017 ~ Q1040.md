##### Q1017
- int형 정수 1개를 입력받아 공백을 사이에 두고 3번 출력
    - a = int(input())
    - print(a, a, a, sep=" ")

##### Q1018
- 어떤 형식에 맞추어 시간이 입력될 때, 그대로 출력 (:으로 구분)
    - hour, minute = input().split(":")
    - print(hour, minute, sep=":")

##### Q1019
- 년, 월, 일을 입력받아 지정된 형식으로 출력 (.으로 구분)
    - year, month, day = input().split('.')

    - print('%04d' % int(year), end='.')
    - print('%02d' % int(month), end='.')
    - print('%02d' % int(day))
    
##### Q1020
- 주민번호를 XXXXXX-XXXXXXX와 같은 형태로 입력받아 XXXXXXXXXXXXX로 출력
    - a, b = input().split('-')

    - print(a, end='')
    - print(b)
    
##### Q1021
- 1개의 단어를 입력받아 그대로 출력
    - word = input()

    - print(word)
    
##### Q1022
- 공백 문자가 포함되어 있는 문장을 입력받고 그대로 출력
    - str = input()

    - print(str)
    
##### Q1023
- 실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력
    - a, b = input().split('.')

    - print(a)
    - print(b)
    
##### Q1024
- 영단어 1개를 입력 받고, 입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력
    - a = input()

    - for c in a:
    - print("'"+c+"'")
    
##### Q1025
- 다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력
    - a = input()

    - print("[" + str(int(a[0]) * 10000) + "]")
    - print("[" + str(int(a[1]) * 1000) + "]")
    - print("[" + str(int(a[2]) * 100) + "]")
    - print("[" + str(int(a[3]) * 10) + "]")
    - print("[" + str(int(a[4])) + "]")
    
##### Q1026
- 입력되는 시:분:초에서 분만 출력
    - a, b, c = input().split(':')

    - print(int(b))
    
##### Q1027
- yyyy.mm.dd를 입력 받아 dd-mm-yyyy로 출력
    - year, month, day = input().split('.')

    - print('%02d' % int(day), end = '-')
    - print('%02d' % int(month), end = '-')
    - print('%04d' % int(year))
    
##### Q1028
- 정수 1개를 입력받아 그대로 출력 (정수의 범위 : 0 ~ 4,294,967,295)
    - a = input()

    - print(a)

##### Q1029
- 실수 1개를 입력받아 그대로 출력
    - a = float(input())

    - print('%.11f' % a)
    
##### Q1030
- 정수 1개를 입력 받아 그대로 출력 (정수의 범위 : -9,223,372,036,854,775,808 ~ +9,223,372,036,854,775,807)
    - a = input()

    - print(a)
    
##### Q1031
- 10진수를 입력받아 8진수로 출력
    - a = int(input())

    - print('%o' % a)
    
##### Q1032
- 10진수를 입력받아 16진수로 소문자로 출력
    - a = int(input())

    - print('%x' % a)
    
##### Q1033
- 10진수를 입력받아 16진수로 대문자로 출력
    - a = int(input())

    - print('%X' % a)

##### Q1034
- 8진수로 입력된 정수 1개를 10진수로 바꾸어 출력해보자
    - a = int(input(),8)

    - print(a)

##### Q1035
- 16진수로 입력된 정수 1개를 8진수로 바꾸어 출력
    - a = int(input(),16)

    - print('%o' % a)
    
##### Q1036
- 영문자 1개를 입력받아 아스키 코드표의 10진수 값으로 출력
    - a = ord(input())

    - print(a)
    
##### Q1037
- 10진 정수 1개를 입력받아 아스키 문자로 출력
    - a = int(input())

    - print(chr(a))
    
##### Q1038
- 정수 2개를 입력받아 합을 출력 (공백으로 구분되어 입력)
    - a, b = input().split()
    - a = int(a)
    - b = int(b)
    - print(a + b)
    
##### Q1040
- 입력된 정수의 부호를 바꿔 출력
    - a = int(input())

    - print(-a)
