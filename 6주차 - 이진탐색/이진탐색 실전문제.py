#반복문으로 구현한 이진 탐색 소스 코드
def binary_search(array, target, start, end):
    while start <=end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid +1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)


# 실전 문제1 정렬된 배열에서 특정 수의 개수 구하기
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))
result = binary_search(array, target, 0, n - 1)

if result == None:
    print(-1)
else:
    n1 = 0
    n2 = 0
    for i in range(1, len(array)):
        if array[result + i] == target:
            n1 += 1
        else:
            break

    for i in range(1, len(array)):
        if array[result - i] == target:
            n2 += 1
        else:
            break
    print(n1+n2 + 1)


# 실전 문제 2 고정점 찾기
N = int(input())
array = list(map(int, input().split()))

def fixbinary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return -1

result = fixbinary_search(array, 0, N - 1)
print(result)


# 실전 문제 3 공유기 설치, 기준을 사이 gap으로 정한다.
N, C = map(int, input().split())
array =[]
for i in range(N):
    array.append(int(input()))
array.sort()
def best_wifi(array):
    min = array[-1] - array[0]
    for i in range(len(array) - 1):
        if array[i + 1] - array[i] < min:
            min = array[i + 1] - array[i]
    min_gap = min
    max_gap = array[-1]-array[0]
    while min_gap <= max_gap:
        mid = (min_gap + max_gap)//2
        count = 1
        m = 0
        for i in range(len(array)-1):
            if array[i+1]-array[m] >= mid:
                m = i+1
                count+=1
        if count >= C:
            min_gap = mid+1
        else:
            max_gap = mid-1
    return (min_gap + max_gap) // 2
print(best_wifi(array))




