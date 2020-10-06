## 정렬 알고리즘
- **정렬** : 데이터를 특정한 기준에 따라 순서대로 나열하는 것
- 일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용됨.

### 선택 정렬
- 처리되지 않은 데이터 중에서 **가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복**
- 선택 정렬 소스코드
```
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)

실행 결과
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### 선택 정렬의 시간 복잡도
- 선택 정렬을 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 함.
- 구현 방식에 따라서 사소한 오차는 있을 수 있지만, 전체 연산 횟수는 다음과 같음.
```
N + (N - 1) + (N - 2) + ··· + 2
```
- 이는 (N² + N - 2) / 2로 표현할 수 있는데, 빅오 표기법에 따라서 **O(N²)** 이라고 작성함.

### 삽입 정렬
- 처리되지 않은 데이터를 하나씩 골라 **적절한 위치**에 삽입
- 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작함.

#### 삽입 정렬 소스코드
```
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j - 1]: #한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)

실행 결과
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### 삽입 정렬의 시간 복잡도
- 삽입 정렬의 시간 복잡도 : **O(N²)**
- 선택 정렬과 마찬가지로 반복문이 두 번 중첩되어 사용됨.
- 삽입 정렬은 <현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작
  - 최선의 경우 O(N)의 시간 복잡도를 가짐.

### 퀵 정렬
- 기준 데이터를 설정하고 **그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법**
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
- 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
- 가장 기본적인 퀵 정렬 : **첫 번째 데이터를 기준 데이터(Pivot)로 설정**

#### 퀵 정렬의 시간 복잡도
- 평균의 경우 **O(NlogN)** 의 시간 복잡도를 가짐.
- 하지만 최악의 경우 **O(N²)** 의 시간 복잡도를 가짐.

#### 퀵 정렬이 빠른 이유 : 직관적인 이해
- 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수는 O(NlogN)와 비례할 것을 예상할 수 있음.
    - **너비 × 높이** = N × logN = NlogN
    
#### 퀵 정렬 소스코드
```
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right) # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

실행 결과
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### 퀵 정렬 소스코드 : 파이썬의 장점을 살린 방식
```
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))    

실행 결과
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### 정렬 알고리즘 비교
- 표준 정렬 라이브러리는 최악의 경우에서 **O(NlogN)** 을 보장함.


|정렬 알고리즘|평균 시간 복잡도|공간 복잡도|특징
|:----------:|:----------:|:----------:|:-------:
|선택 정렬|O(N²)|O(N)|아이디어가 매우 간단함
|삽입 정렬|O(N²)|O(N)|데이터가 거의 정렬되어 있을 때는 가장 빠름
|퀵 정렬|O(NlogN)|O(N)|대부분의 경우에 가장 적합하며, 충분히 빠름

#### 선택 정렬과 기본 정렬 라이브러리 수행 시간 비교
```
from random import randint
import time

# 배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
    # 1부터 100 사이의 랜덤한 정수
    array.append(randint(1, 100))

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

# 측정 종료
end_time = time.time()

# 수행 시간 출력
print("선택 정렬 성능 측정 : ", end_time - start_time)

# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    # 1부터 100 사이의 랜덤한 정수
    array.append(randint(1, 100))

# 기본 정렬 라이브러리 성능 측정
start_time - time.time()

# 기본 정렬 라이브러리 사용
array.sort()

# 측정 종료
end_time = time.time()

# 수행 시간 출력
print("기본 정렬 라이브러리 성능 측정 : ", end_time - start_time)

실행 결과
선택 정렬 성능 측정 : 35.8414609432222046
기본 정렬 라이브러리 성능 측정 : 0.0013387203216552734
```

### 문제 1) 영산이는 두 개의 배열 A와 B를 가지고 있다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수이다.
### 영산이는 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다.
### 영산이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이다.
### N, K 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하라.

#### ex) N = 5, K = 3이고, 배열 A와 B가 다음과 같다고 해보자.
-  배열 A = [1, 2, 5, 4, 3]
-  배열 B = [5, 5, 6, 6, 5]
#### 이 경우, 다음과 같이 세 번의 연산을 수행할 수 있다.
- 연산 1) 배열 A의 원소 '1'과 배열 B의 원소 '6'을 바꾸기
- 연산 2) 배열 A의 원소 '2'와 배열 B의 원소 '6'을 바꾸기
- 연산 3) 배열 A의 원소 '3'와 배열 B의 원소 '5'을 바꾸기
#### 세 번의 연산 이후 배열 A와 배열 B의 상태는 다음과 같이 구성될 것이다.
- 배열 A = [6, 6, 5, 4, 5]
- 베열 B = [3, 5, 1, 2, 5]
#### 이 때, 배열 A의 모든 원소의 합은 26이 되며, 이보다 더 합을 크게 만들 수는 없다. 

### 입력 조건
-  첫 번째 줄에 N, K가 공백을 기준으로 구분되어 입력된다. (1 ≤ N ≤ 100,000, 0 ≤ K ≤ N)
-  두 번째 줄에 배열 A의 원소들이 공백을 기준으로 구분되어 입력된다. 모든 우너소는 10,000,000보다 작은 자연수이다.
-  세 번째 줄에 배열 B의 원소들이 공백을 기준으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.

### 출력 조건
- 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력한다.

#### 문제 해결 아이디어
- **핵심 아이디어** : 매번 배열 A에서 가장 작은 원소를 골라서, 배열 B에서 가장 큰 원소와 교체한다.
- 가장 먼저 배열 A와 B가 주어지면 A에 대하여 오름차순 정렬하고 B에 대하여 내림차순 정렬한다.
- 이후에 두 배열의 원소를 첫 번째 인덱스부터 차례로 확인하면서 A의 원소가 B의 원소보다 작을 때에만 교체를 수행한다.
- 이 문제에서는 두 배열의 원소가 최대 100,000개까지 입력될 수 있으므로, 최악의 경우 **O(NlogN)** 을 보장하는 정렬 알고리즘을 이용해야 한다.

#### 정답
```
n, k = map(int, input().split()) # N과 K를 입력 받기
a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력 받기
b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력 받기

a.sort() # 배열 A는 오름차순 정렬 수행
b.sort(reverse = True) # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a)) 
```

## 이진 탐색 알고리즘
- 순차 탐색 : 리스트 안에 있는 특정한 **데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인**하는 방법
- 이진 탐색 : 정렬되어 있는 리스트에서 **탐색 범위를 절반씩 좁혀가며 데이터를 탐색**하는 방법
    - 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정
    
#### 이진 탐색의 시간 복잡도
- 단계마다 탐색 범위를 2로 나누느 것과 동일하므로 **연산 횟수는 log₂에 비례한다.**
- 예를 들어 초기 데이터 개수가 32개일 때, 이상적으로 1단계를 거치면 16개 가량의 데이터만 남는다.
    - 2단계를 거치면 8개 가량의 데이터만 남는다.
    - 3단계를 거치면 4개 가량의 데이터만 남는다.
- 다시 말해 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 **O(LogN)** 을 보장한다.    

#### 이진 탐색 소스코드 : 재귀적 구현
```
# 이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간 점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간 값의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))        
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)    

실행 결과 1)
10 7
1 3 5 7 9 11 13 15 17 19
4

실행 결과 2)
1 3 5 6 9 11 13 15 17 19
원소가 존재하지 않습니다.
```

#### 이진 탐색 소스코드 : 반복문 구현
```
# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간 점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간 값의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))        
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)    
```

#### 파이썬 이진 탐색 라이브러리
- bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 위치 반환
- bisect_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 위치를 반환
```
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left)
print(bisect_right)

실행 결과
2
4
```

#### 값이 특정 범위에 속하는 데이터 개수 구하기
```
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)
  return right_index - left_index

# 배열 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))

실행 결과
2
6
```

### 파라메트릭 서치 (Parametric Search)
- 최적화 문제를 결정 문제('예' 또는 '아니오')로 바꾸어 해결하는 기법
    - ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
- 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 **이진탐색을 이용하여 해결 가능**

### 문제 2) 오늘 영산이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했다. 영산이네 떡볶이 떡은 떡볶이 떡의 길이가 일정하지 않다. 대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
### 절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
### 예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것이다. 잘린 떡의 길이는 차례대로 4, 0, 0, 2cm이다. 손님은 6cm만큼의 길이를 가져간다.
### 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하라.

### 입력 조건
- 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)
- 둘째 줄에 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다. 높이는 10억보다 작거나 같은 양의정수 또는 0이다.

### 출력 조건
- 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

#### 문제 해결 아이디어
- 적절한 높이를 찾을 때까지 이진 탐색을 수행하여 높이 H를 반복해서 조정하면 된다.
- '현재 이 높이로 자르면 조건을 만족할 수 있는가?'를 확인한 뒤에 조건의 만족 여부에 따라서 탐색 범위를 좁혀서 해결할 수 있다.
- 절단기의 높이는 0부터 10억까지의 정수 중 하나이다.
    - 이렇게 큰 탐색 범위를 보면 가장 먼저 **이진 탐색** 을 떠올려야 한다.    
- 중간점의 값은 시간이 지날수록 **'최적화된 값'** 이 되기 때문에, 과정을 반복하면서 얻을 수 있는 떡의 길이 합이 필요한 떡의 길이보다 크거나 같을 때마다 **중간점의 값을 기록**하면 된다.

#### 정답
```
# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력
n, m = list(map(int, input().split()))

# 각 떡의 개별 높이 정보를 입력
array = list(map, int, input().split())

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
        # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
        if total < m:
            end = mid - 1
        # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
        else:
            result = mid # 최대한 덜 잘랐을 때가 정답이므로 여기에서 result에 기록
            start = mid + 1

print(result)            
```

### 문제 3) N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다. 이 때 이 수열에서 x가 등장하는 횟수를 계산하라.
### 예를 들어 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력한다.
### 단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 **시간초과** 판정을 받는다.

### 입력 조건
- 첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력된다. (1 ≤ N ≤ 1,000,000), (-10^9 ≤ x 10^9)
- 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력된다. (-10^9 ≤ 각 원소의 값 10^9)

### 출력 조건
- 수열의 원소 중에서 값이 x인 원소의 개수를 출력한다. 단, 값이 x인 원소가 하나도 없다면 -1을 출력한다.

#### 문제 해결 아이디어
- 시간 복잡도 O(logN)으로 동작하는 알고리즘을 요구하고 있다.
    - 일반적인 선형 탐색으로는 시간초과 판정을 받는다. 
    - 하지만 데이터가 정렬되어 있기 때문에 **이진 탐색을 수행**할 수 있다.
- 특정 값이 등장하는 첫 번째 위치와 마지막 위치를 찾아 인덱스 차이를 계산해 문제를 해결할 수 있다.    

#### 정답
```
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

# 데이터의 개수 N, 찾고자 하는 값 x
n, x = map(int, input().split())    

array = list(map(int, input().split()))

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)
```


