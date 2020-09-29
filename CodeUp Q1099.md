##### Q1099
- 미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고, 먹이가 2로 주어질 때, 성실한 개미의 이동경로를 예상
- 단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는 더 이상 이동하지 않고 그 곳에 머무른다고 가정
- (2, 2)에서 출발 (10 * 10 크기, 이동한 경로를 9로 표시해 출력)
```
board = [0 for x in range(10) for y in range(10)]

# 배경 input
for i in range(10):
  num = input().split()
  board[i] = list(map(int, num))

start = (1, 1)

point = [0, 0]
point[0] = start[0]
point[1] = start[1]

status = 0

while status != 2:
 if board[point[0]][point[1]] == 2:
      status = 2
      board[point[0]][point[1]] = 9
 else:
        # 경로 표시
      board[point[0]][point[1]] = 9

        # 경로 이동
      if board[point[0]][point[1]+1] != 1:
          point[1] = point[1]+1
            # print(point[1])
      else:
          point[0] = point[0] + 1
            # print(point[0])

        # 유효성
      if point[0] > 8:
          point[0] = 8
          break;
      if point[1] > 8:
          point = 8
          break;

for i in range(10):
    for j in range(10):
        print(board[i][j], end=' ')
    print()
```
