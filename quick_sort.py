# 입력값을 리스트화
list_n = [x for x in input().split(' ')]


def quick_sort(arr):
    # 값이 1개이기 때문에 return arr
    if len(arr) <= 1:
        return arr
    # 기준점(pivot)을 가운데로 지정
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


print(quick_sort(list_n))
