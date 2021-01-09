#### 구구단을 여러번 출력하는 문제
- N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성
```
a = int(input())

for i in range(1,10):
  print(a, "*", i, "=", a*i)
```

#### A+B를 여러번 출력하는 문제
- 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성
```
n = int(input())

for i in range(n):
  a, b = map(int, input().split())
  print(a+b)
```

#### 1부터 N까지의 합을 구하는 문제
- n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성
```
n = int(input())
temp=0
for i in range(n+1):
  temp =temp+i
print(temp)
```

#### N찍기
- 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성
```
n = int(input())

for i in range(1, n+1):
  print(i)
```

#### 반대로 N찍기
- 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 반대로 출력하는 프로그램을 작성
```
n = int(input())

for i in range(n, 0,-1):
  print(i)
```

#### 별 찍기
- 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
```
n = int(input())

for i in range(1,n+1):
  print("*"*i)
```

#### 오른쪽부터 별 찍기
- 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제. 단, 오른쪽부터 채워지도록 작성
```
n = int(input())

for i in range(1,n+1):
  print(" "*(n-i)+"*"*i)
```

#### X보다 작은 수
- 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성
```
a, b = map(int, input().split())
c=list(map(int, input().split()))

for i in range(a):
  if c[i]<b:
    print(c[i], end=' ')
```

#### A+B
- 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성
```
a, b = map(int, input().split())

while(a!=0 and b!=0):
  print(a+b)
  a, b = map(int, input().split())
```

#### A+B
- 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성
```
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
```

#### 더하기 사이클
- 보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다
- N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성
```
tmp = inp = int(input())
count = 0
while True:
    ten = tmp//10
    one = tmp%10
    res = ten + one
    count += 1
    tmp = int(str(tmp%10)+str(res%10))
 
    if (inp==tmp):
        break
print(count)
```

#### 최소, 최대
- N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성
```
a = int(input())
b = list(map(int, input().split()))
min = b[0]
max = b[0]
  

for i in b:
  if min > i:
    min = i
  elif max < i:
    max = i

print(min, max)
```

#### 최댓값
- 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성
```
a = []

for i in range(9):
  a.append(int(input()))

print(max(a))
print(a.index(max(a))+1)
```

#### 숫자의 개수
- 세 개의 자연수 A, B, C가 주어질 때 A×B×C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성
```
a = int(input())
b = int(input())
c = int(input())

num = list(str(a * b * c))
for i in range(10):
    print(num.count(str(i)))
```






