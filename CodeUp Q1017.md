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
