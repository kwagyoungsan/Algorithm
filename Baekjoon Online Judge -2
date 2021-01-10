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

