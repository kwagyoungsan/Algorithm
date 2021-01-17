#### 손익분기점
- A : 고정 비용, B : 가변 비용, C : 가격 / A, B, C가 주어졌을 때, 손익분기점을 구하는 프로그램을 작성
```
fix, var, price = map(int, input().split())
i = 0
if var >= price:
    i = -1
else:
    i = fix // (price - var) + 1
print(i)
```

#### 벌집
- 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성
```
num = int(input())
n = 0
result = 1
loop = 1

while(1):
    if num > result:
        n += 6
        result = result + n
        loop += 1
    else:
        break

print(loop)
```

#### 분수 찾기
- 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 한다. X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성
```
num = int(input())

line = 1
while num > line:
    num -= line
    line += 1

if line % 2 == 0:
    a = num
    b = line - num + 1
else:
    a = line - num + 1
    b = num

print(a, '/', b, sep='')
```

#### 달팽이는 올라가고 싶다
- 높이 : V, 낮에 올라갈 수 있는 거리 : A, 밤에 미끄러지는 거리 : B, 정상에 올라가라면 며칠이 걸리는지 구하는 프로그램을 작성
```
import math

up, down, h = map(int, input().split())
height = math.ceil((h-down)/(up-down))
print(height)
```

#### ACM 호텔
```
import math

num = int(input())

for i in range(num):
    H, W, N = map(int, input().split())
    floor = N % H
    room_num = math.floor(N / H) + 1
    if floor == 0:
        result = H * 100 + room_num-1
    else:
        result = floor * 100 + room_num
    print(result)
```

#### 부녀회장이 될테야




