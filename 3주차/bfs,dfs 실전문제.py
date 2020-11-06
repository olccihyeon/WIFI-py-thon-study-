#백준 2583 영역 구하기

# a = list(map(int, input().split()))
# graph = []
# for i in range(a[1]):
#     graph.append( [0] * (a[0]))
# result = []
# for i in range(a[2]):
#     result.append(list(map(int, input().split())))
# for i in result:
#     for j in range(i[0],i[2]):
#         for k in range(i[1],i[3]):
#             graph[j][k] = 1
#
# n = a[1]
# m = a[0]
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
#
# def bfs(first):
#     queue = [first]
#     count = 1
#     graph[first[0]][first[1]] = 2
#     while queue:
#         point = queue.pop()
#         for i in range(4):
#             x = point[0] + dx[i]
#             y = point[1] + dy[i]
#             if 0 <= x and x < n and 0 <= y and y < m and graph[x][y] == 0:
#                 graph[x][y] = 2
#                 count += 1
#                 queue.append((x, y))
#     return count
# area =[]
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 0:
#             area.append(bfs((i,j)))
#
# area.sort()
# print(len(area))
# for i in area:
#     print(i, end=' ')


#백준 7562 나이트의 이동
from collections import deque
case = int(input())
path = []
for i in range(case):
    size = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    graph = []
    for i in range(size):
        graph.append( [0] * size)
    dx = [1, 2, 2, 1, -1,-2,-2,-1]
    dy = [2, 1, -1, -2,2,1,-1,-2]
    def bfs(first):
        queue = deque([first])
        graph[first[0]][first[1]] = 1
        while queue:
            point = queue.popleft()
            if point[0] ==end[0] and point[1]==end[1]:
                return graph[point[0]][point[1]]-1
            for i in range(8):
                x = point[0] + dx[i]
                y = point[1] + dy[i]
                if 0 <= x and x < size and 0 <= y and y < size and graph[x][y] == 0:
                    graph[x][y] = graph[point[0]][point[1]]+1
                    queue.append((x, y))

    path.append(bfs(start))
for i in path:
    print(i)




# 프로그래머스 타겟넘버
# answer = 0
#
# def solution(numbers, target):
#     global answer
#
#     def dfs(index, target):
#         global answer
#         if index == len(numbers):
#             if target == 0:
#                 answer += 1
#                 return
#         else:
#             dfs(index + 1, target - numbers[index])
#             dfs(index + 1, target + numbers[index])
#
#     dfs(0, target)
#     return answer