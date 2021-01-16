#### 아스키 코드
- 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성
```
a = input()

print(ord(a))
```

#### 숫자의 합
- N개의 숫자가 공백없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성
```
n = int(input())
num = input()
sum = 0

for i in num:
    sum += int(i)
print(sum)
```

#### 알파벳 찾기
- 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성
```
word = input()
alphabet = list(range(97,123))

for x in alphabet :
    print(word.find(chr(x)))
```

#### 문자열 반복
- 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성
```
n = int(input())

for i in range(n):
    count, word = input().split()
    for j in word:
        print(j*int(count), end='')
    print()
```

#### 단어 공부
- 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성. 단, 대문자와 소문자를 구분하지 않는다.
```
words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])
```

#### 단어의 개수
- 영어 대소문자와 띄어쓰기만으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.
```
words = input().split()

print(len(words))
```

#### 상수
- 두 수가 주어지고, 두 수를 거꾸로 돌려서 더 큰 수를 출력하는 프로그램을 작성
```
num1, num2 = input().split()

num1 = int(num1[::-1])
num2 = int(num2[::-1])

if num1 < num2:
    print(num2)
else:
    print(num1)
```

#### 다이얼
```
word = input().upper()
dial_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for i in range(len(word)):
    for j in dial_list:
        if word[i] in j:
            time += dial_list.index(j) + 3
print(time)
```

#### 크로아티아 알파벳
```
cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] 
word = input()
num = 0

for i in cro_alpha:
    word = word.replace(i,'a')

print(len(word))
```
