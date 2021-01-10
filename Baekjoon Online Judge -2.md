#### 나머지
- 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성
```
list = []
for _ in range(10):
    num = int(input())
    list.append(num % 42)
list = set(list)
print(len(list))
```

#### 평균
- M을 최댓값이라 하고, 모든 점수를 점수/M*100으로 고쳤다. 이때 새로운 평균을 구하는 프로그램을 작성
```
n = int(input())
score = list(map(int,input().split()))
max_score = max(score)

for i in range(n):
  score[i] = score[i]/max_score*100

avg = sum(score)/n
print("%.2f"%avg)
```

#### OX퀴즈
- 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성
```
num = int(input())
for i in range(num):
  OX = input()
  score = 0
  count = 0
  for i in range(len(OX)):
    if OX[i] == 'O':
      count += 1
      score += count
    elif OX[i] == 'X':
      count = 0
      score += 0
  print(score)  
  ```
 
 #### 평균은 넘겠지
  ```
  num = int(input())

for _ in range(num):
    score = list(map(int, input().split()))
    avg = sum(score[1:]) / score[0]
    count = 0

    for i in score[1:]:
       if i > avg:
          count+=1

    rate = count / score[0] * 100
    print(f'{rate:.3f}%')
```

#### 정수 N개의 합
- 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성
```
def solve(a):
  return sum(a)
```

#### 셀프 넘버
- 생성자가 없는 숫자를 셀프 넘버라고 한다. 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성
```
def SN(n):
    result = n
    for i in list(str(n)):
        result += int(i)
    return result
  
cons = []
for i in range(1,10001):
  cons.append(SN(i))

cons.sort()

for i in range(1, 10001):
  if i in cons:
    continue
  else:
    print(i)
```

#### 한수
- 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성
```
def hansu(n):
    count = 0
    for i in range(1,n+1):
        hansu_list = list(map(int,str(i)))
        if i<100:
            count += 1
        elif hansu_list[0] - hansu_list[1] == hansu_list[1] - hansu_list[2]:
            count += 1
    return count

num = int(input())
print(hansu(num))
```




