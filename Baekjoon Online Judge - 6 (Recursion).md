#### 팩토리얼
- 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성
```
import math

n = int(input())

print(math.factorial(n))
```

#### 피보나치 수
- n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성
```
import math

n = int(input())

arr=[]
arr.append(0)
arr.append(1)

for i in range(2,n+1):
    arr.append(arr[i-2] + arr[i-1])

print(arr[n])
```

#### 별 찍기
```
def stars(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return(list(matrix))

star = ["***", "* *", "***"]

n = int(input())
k = 0
while n != 3:
    n = int(n / 3)
    k += 1

for i in range(k):
    star = stars(star)
for i in star:
    print(i)
```

#### 하노이 탑 이동 순서
```
n = int(input())

def hanoi(disk, start, mid, end):
    if disk == 1:
        print(start, end)
    else:
        hanoi(disk - 1, start, end, mid)
        print(start, end)
        hanoi(disk - 1, mid, start, end)
print(2**n-1)
hanoi(n, 1, 2, 3)
```
