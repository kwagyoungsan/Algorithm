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



