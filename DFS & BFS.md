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
def dfs(graph, v, visited):
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
   1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 함
   2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 함
   3. 더 이상 위 과정을 수행할 수 없을 때까지 반복
   
#### BFS 소스코드 예제
```
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
  # 큐 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  # 현재 노드를 방문 처리
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력하기
    v = queue.popleft()
    print(v, end = ' ')
    # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
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

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

실행 결과
1 2 3 8 7 4 5 6 
```

### 문제 1) N × M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 
### 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 이 때 얼음 틀의 모양이 주어 졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라.

### 입력 조건
#### 세로 길이 : N, 가로 길이 : M (1 <= N, M <= 1000)
#### 두 번째 줄 부터 N + 1번째 줄까지 얼음 틀의 형태가 주어짐
#### 이 때 구멍이 뚫려 있는 부분은 0, 그렇지 않은 부분은 1

### 출력 조건
#### 한번에 만들 수 있는 아이스크림 개수를 출력

- 문제 해결 아이디어
   - DFS로 해결 
   - 얼음을 얼릴 수 있는 공간이 상, 하, 좌, 우로 연결되어 있다고 표현할 수 있으므로 그래프 형태로 모델링 가능하다
   - 알고리즘
      1. 특정한 지점의 주변 상, 하, 좌, 우를 상펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문
      2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 진행하는 과정을 반복하면, 연결된 모든 지점을 방문할 수 있음
      3. 모든 노드에 대하여 1 ~ 2번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트함
      
- 정답
```
# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
  # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False 

  # N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input.split())

  # 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
        graph.append(list(map(int, input())))   

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 DFS 수행
    if dfs(i, j) == True:
      result += 1

print(result)
```

### 문제 2) N × M 크기의 직사각형 형태의 미로에 갇혔다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
### 내 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 이 때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다.
### 이 때 내가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

### 입력 조건
#### 첫째 줄에 두 정수 N, M(4 ≤ N, M ≤ 200)이 주어짐. 다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어짐.
#### 각각의 수들은 공백 없이 붙어서 입력으로 제시됨. 또한 시작 칸과 마지막 칸은 항상 1

### 출력 조건
#### 첫째 줄에 최소 이동 칸의 개수를 출력
   
- 문제 해결 아이디어
   - BFS로 해결 
   - 상, 하, 좌, 우로 연결된 모든 노드로의 거리가 1로 동일하다
      - (1, 1) 지점부터 BFS를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결할 수 있다

- 정답
```
# BFS 소스코드 구현
def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        #현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if graph[nx][ny] == 1:
                  graph[nx][ny] = graph[x][y] + 1
                  queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

from collections import deque

# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
```

### 문제 3) 어떤 나라에는 1 ~ N번 까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1
### 이 때, 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램을 작성하시오. 또한, 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

### 입력 조건
#### 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어짐.
#### (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N)
#### 둘째 줄 부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 주어지며, 각 자연수는 공백으로 구분
#### 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미

### 출력 조건
#### X로부터 출발하여 도달할 수 있는 도시중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력
#### 이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력

- 문제 해결 아이디어
   - 모든 간선의 비용은 1이다.
   - 따라서 BFS를 이용하여 최단 거리를 계산할 수 있다.
      - 먼저 특정한 도시 X를 시작점으로 BFS를 수행하여 모든 도시까지의 최단 거리를 계산한다.
      - 이후에 각 노드로의 최단 거리를 하나씩 확인하며 그 값이 K인 경우에 해당 도시의 번호를 출력한다.
      
- 정답
```
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# BFS 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)        
```

### 문제 4) N × N 크기의 시험관이 있다. 시험관은 1 × 1 크기의 칸으로 나누어지며, 특정한 위치에는 바이러스가 존재할 수 있다. 바이러스의 종류는 1 ~ K번까지 K가지가 있으며 모든 바이러스는 이 중 하나에 속한다
### 시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식하는데, 매 초 번호가 낮은 종류의 바이러스부터 먼저 증식한다. 또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 있다면, 그곳에는 다른 바이러스가 들어갈 수 없다.
### 시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후에 (X, Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성

### 입력 조건
#### 첫째 줄에 자연수 N, K가 주어지며, 각 자연수는 공백으로 구분 (1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000)
#### 둘째 줄부터 N개의 줄에 걸쳐서 시험관의 정보가 주어짐. 단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어짐. 또한 모든 바이러스의 번호는 K이하의 자연수로만 주어짐.
#### N + 2번째 줄에는 S, X, Y가 주어지며 공백으로 구분함. (0 ≤ 10,000, 1 ≤ X, Y ≤ N)

### 출력 조건
#### S초 뒤에 (X, Y)에 존재하는 바이러스의 종류를 출력함. 만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력함.

- 문제 해결 아이디어
   - 모든 간선의 비용은 1이다.
   - BFS를 이용하여 최단 거리를 계산할 수 있다.
      - 다만 바이러스가 낮은 번호부터 증식한다는 점이 특징이다.
      - 따라서 초기 큐에 원소를 삽입할 때 낮은 바이러스의 번호부터 삽입한다.
      
- 정답
```
from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 버져나갈 수 있는 4가지의 위치
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x -1][target_y -1])                
```

### 문제 5) N × N 크기의 복도가 있다. 이 복도는 1 × 1 크기의 칸으로 나누어지며 ㅌ늑정한 위치에는 선생님, 학생 혹은 장애물이 있다
### 각 선생님은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로 감시를 진행한다. 단, 복도에 장애물이 있으면 선생님은 장애물 뒤편에 숨어 있는 학생을 볼 수 없다.
### 또한, 선생님은 아무리 멀리 있더라도 장애물로 막히기 전까지 4가지 방향으로 학생을 모두 볼 수 있다.
### N × N 크기의 복도에서 학생과 선생님의 위치가 주어졌을 때, 복도의 빈 칸 중에서 장애물을 정확히 3개 설치하여 모든 학생이 선생님의 감시를 피할 수 있는지 출력하는 프로그램을 작성

### 입력 조건
#### 첫째 줄에 자연수 N이 주어진다. (3 ≤ N ≤ 6)
#### 둘째 줄에 N개의 줄에 걸쳐서 복도의 정보가 주어진다. 각 행에서는 N개의 원소가 주어지며, 공백으로 구분함. 해당 위치에 학생이 있다면 S, 선생님이 있다면 T, 아무 것도 존재하지 않는다면 X가 주어짐. 단, 항상 빈 칸의 개수는 3개 이상으로 주어진다.

### 출력 조건
#### 첫째 줄에 정확히 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는 지의 여부를 출력함. 모든 학생들을 감시로부터 피하도록 할 수 있다면 "YES", 그렇지 않다면 "NO"를 출력함.

- 문제 해결 아이디어
   - 장애물을 정확히 3개 설치하는 모든 경우를 확인하며, 매 경우마다 모든 학생을 감시로부터 피하도록 할 수 있는지의 여부를 출력한다.
   - 복도의 크기는 N × N이며, N은 최대 6이다. 따라서 장애물을 정확히 3개 설치하는 모든 조합의 수는 최악의 경우 36C3이다.
   - 경우의 수가 10,000이하이므로, 모든 조합을 고려하여 완전 탐색을 수행해 해결할 수 있다.
      - 모든 조합을 찾을 때에는 DFS/BFS를 이용하거나 조합 꼐산 라이브러리를 사용한다.
      
- 정답
```
from itertools import combinations

n = int(input()) # 복도의 크기
board = [] # 복도 정보 (N x N)
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teachers.append((i, j))
        # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if board[i][j] == 'X':
            spaces.append((i, j))

# 특정 방향으로 감시를 진행 (학생 발견: True, 학생 미발견: False)
def watch(x, y, direction):
    # 왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y -= 1
    # 오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y += 1
    # 위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x -= 1
    # 아래쪽 방향으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x += 1
    return False

# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생의 위치를 하나씩 확인
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    # 장애물들을 설치해보기
    for x, y in data:
        board[x][y] = 'O'
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        # 원하는 경우를 발견한 것임
        find = True
        break
    # 설치된 장애물을 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')
```    
