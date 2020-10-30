#1 음료수 통 개수

n, m = map(int, input().split())
graph =[]
for i in range(n):
    graph.append(list(map(int, input().split())))
def dfs(x, y):
    if x<=-1 or x>=n or y>=m or y<=-1:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
print(result)

#2 미로 탈출 게임

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = []
for i in range(n):
    visited.append([False]*m)

def bfs(graph, startx,starty, visited):
    queue = deque([(startx,starty)])
    visited[startx][starty]=1
    #print(queue)
    while queue:

        v = queue.popleft()
        if v[0]+1<n:
            if graph[v[0]+1][v[1]] ==1 and visited[v[0]+1][v[1]]==False:
                visited[v[0]+1][v[1]] = visited[v[0]][v[1]]+1
                queue.append((v[0]+1, v[1]))

        if v[1]+1<m:
            if graph[v[0]][v[1]+1] ==1 and visited[v[0]][v[1]+1]==False:
                visited[v[0]][v[1]+1] = visited[v[0]][v[1]]+1
                queue.append((v[0] , v[1]+1))

        if v[0]-1>=0:
            if graph[v[0]-1][v[1]] ==1 and visited[v[0]-1][v[1]]==False:
                visited[v[0]-1][v[1]] = visited[v[0]][v[1]]+1
                queue.append((v[0] - 1, v[1]))

        if v[1]-1>=0:
            if graph[v[0]][v[1]-1] ==1 and visited[v[0]][v[1]-1]==False:
                visited[v[0]][v[1]-1] = visited[v[0]][v[1]]+1
                queue.append((v[0] , v[1]-1))

    print(visited[n-1][m-1])

bfs(graph, 0,0,visited)
