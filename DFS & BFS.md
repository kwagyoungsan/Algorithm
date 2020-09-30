## 그래프 탐색 알고리즘 : DFS / BFS
- 탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

#### 스택 자료구조
- 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조
- 입구와 출구가 동일한 형태

#### 스택 구현 예제
```
# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력

실행 결과
[1, 3, 2, 5]
[5, 2, 3, 1]
```

#### 큐 자료구조
- 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
- 입구와 출구가 모두 뚫려 있는 터널과 같은 형태

#### 큐 구현 예제
```
from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력

실행 결과
deque([3, 7, 1, 4])
deque([4, 1, 7, 3])
```

#### 재귀 함수
- 재귀 함수 : 자기 자신을 다시 호출하는 함수
- 단순한 형태의 재귀함수 예제
   - '재귀 함수를 호출합니다.' 라는 문자열을 무한히 출력
   - 어느 정도 출력하다가 최대 재귀 깊이 초과메시지가 출력
```
def recursive_function():
  print('재귀 함수를 호출합니다.')
  recursive_function()

recursive_function()
```

#### 재귀 함수의 종료 조건
- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 함
- 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있음
  - 종료 조건을 포함한 재귀 함수 예제
```
def recursive_function(i):
  # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
  if i == 100:
    return
  print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
  recursive_function(i + 1)
  print(i, '번째 재귀함수를 종료합니다.')

recursive_function()
```

#### 팩토리얼 구현 예제
- n! = 1 × 2 × ··· × (n - 1) × n
- 수학적으로 0!과 1!의 값 : 1
```
# 반복적으로 구현한 n!
def factorial_iterative(n):
  result = 1
  # 1부터 n까지의 수를 차례대로 곱하기
  for i in range(1, n + 1):
    result += 1
  return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
  if n <= 1: # n이 1 이하인 경우 1을 반환
    return 1
  # n! = n * (n - 1)!를 그대로 코드로 작성
  return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! (n = 5)
print('반복적으로 구현 : ', factorial_iterative(5))
print('재귀적으로 구현 : ', factorial_recursive(5))  
```

## DFS (Depth-First Search)
- 깊이 우선탐색
- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- DFS는 스택 자료구조(혹은 재귀함수)를 이용하며, 구체적인 동작 과정은 다음과 같음
  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 함
  2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리를 함. 방문하지 않은 인접 노드가 없으면 스택에서 최상난 노드를 꺼냄
  3. 더 이상 위 과정을 수행할 수 없을 때까지 반복

#### DFS 소스코드 예제
```
# DFS 메서드 예시
def dfs(grapg, v, visited):
  # 현재 노드를 방문 처리
  visited[v] = True
  print(v, end = ' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]      

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 dfs 호출
dfs(graph, 1, visited)

실행 결과
1 2 7 6 8 3 4 5
```

## BFS (Breadth-Firsg Search)
- 너비 우선 탐색
- 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
- BFS는 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같음


51:23






