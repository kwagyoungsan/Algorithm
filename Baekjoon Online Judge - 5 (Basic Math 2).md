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
