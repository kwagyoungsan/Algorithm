#### 소수 찾기 1
- 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성
```
n = int(input())
num = map(int, input().split())
cnt = 0
for i in num:
    error = 0
    if i > 1 :
        for j in range(2, i):
            if i % j == 0:
                error += 1  
        if error == 0:
            cnt += 1 
print(cnt)
```

#### 소수의 합과 최솟값 찾기
- 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성
```
num1 = int(input())
num2 = int(input())

num_list = []

for i in range(num1, num2+1):
    err = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                err += 1
                break
        if err == 0:
            num_list.append(i)

if len(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))
  
```

#### 소인수분해
- 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성
```
n = int(input())
num = 2

while(1):
    
    if n % num == 0:
        print(num)
        n /= num
    else:
        num += 1
    if n == 1:
      break
```

#### 소수 구하기
- M이상 N이하의 소수를 모두 출력하는 프로그램을 작성
```
import math

num1, num2 = map(int, input().split())

def prime(m, n):
    n += 1

    isPrime = [True] * n
    max_length = math.ceil(math.sqrt(n))

    for i in range(2, max_length):
        if isPrime[i]:
            for j in range(i+i, n, i):
                isPrime[j] = False

    for i in range(m, n):
        if i > 1:
            if isPrime[i] == True:
                print(i)

prime(num1, num2)
```

#### 베르트랑 공준
- 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성
```
import math

N = 123456 * 2 + 1

prime = [True] * N
for i in range(2, math.ceil(math.sqrt(N))+1):
    if prime[i]:
        for j in range(2*i, N, i):
            prime[j] = False

def prime_cnt(value):
    cnt = 0
    for i in range(value + 1, value * 2 + 1):
        if prime[i]:
            cnt += 1
    print(cnt)

while True:
    value = int(input())
    if value == 0:
        break
    prime_cnt(value)
```

#### 골드바흐의 추측
- 골드바흐의 수 : 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것. 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력
```
prime_list = [False, False] + [True] * 10002

for i in range(2, 10002):
    if prime_list[i]:
        for j in range(2 * i, 10002, i):
            prime_list[j] = False

num = int(input())

for i in range(num):
    n = int(input())
    a = n // 2
    b = a
    while a > 0:
        if prime_list[a] and prime_list[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1

```

#### 직사각형에서 탈출
```
import math
x, y, w, h = map(int, input().split())

a = int(math.fabs(x-w))
b = int(math.fabs(y-h))

arr = [a, b, x, y]

print(min(arr))
```

#### 네 번째 점
- 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성
```
x_arr = []
y_arr = []
for i in range(3):
        x, y = map(int, input().split())
        x_arr.append(x)
        y_arr.append(y)
for i in range(3):
        if x_arr.count(x_arr[i]) == 1:
                x = x_arr[i]
        if y_arr.count(y_arr[i]) == 1:
                y = y_arr[i]
print(x, y)
```

#### 직각삼각형
- 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하는 프로그램을 작성
```
while True:
    a = list(map(int, input().split()))
    max_num = max(a)
    if sum(a) == 0:
        break
    a.remove(max_num)
    if a[0] ** 2 + a[1] ** 2 == max_num ** 2:
         print('right')
    else:
         print('wrong')
```

#### 택시 기하학
- 반지름 R이 주어졌을 때, 유클리드 기하학에서 원의 넓이와, 택시 기하학에서 원의 넓이를 구하는 프로그램을 작성
```
import math

r = int(input())

print(r*r*math.pi)
print(2*r*r)
```

#### 터렛
- a좌표 (x1, y1)와 좌표 b(x2, y2)가 주어지고, a와 c의 거리 r1과 b와 c의 거리 r2가 주어졌을 때, c가 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성
```
import math

n = int(input())

for _ in range(n):
    ax, ay, r1, bx, by, r2 = map(int, input().split())
    
  
    xsum = abs(ax-bx)
    ysum = abs(ay-by)
    dis = math.sqrt(xsum**2 + ysum**2)
    rsum = r1+r2
    rminus = abs(r1-r2)
    
    if dis == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if dis == rsum or dis == rminus:
            print(1)
        elif dis < rsum and dis > rminus:
            print(2)
        else:
            print(0)
```



