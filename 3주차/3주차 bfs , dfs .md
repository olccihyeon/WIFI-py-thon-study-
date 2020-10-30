# 3주차 bfs , dfs 

> python에서 유용한 모듈
1. collections.deque()   
속도가 빠릅니다.

  ```
  import collections
  d = collections.deque()
  d.append(2)
  d.popleft()
  ```

2. defaultdict 객체   
존재하지 않는 키를 조회할 경우 해당 키에 대한 딕셔너리 아이템을 생성해줍니다.

```
a= collections.defaultdict(int)
a['A'] = 5
a['B'] = 4
a['C'] +=1
print(a)
```
**output : defaultdict(<class 'int'>, {'A' : 5, 'B' : 4 ,'C' :1})**

3. Counter 객체
```
a= [1,2,3,4,5,5,5,6,6 ]
b = collections.Counter(a)
print(b)
```
**output : Counter({5:3,6:2,1:1,2:1,3:1,4:1})**<br/><br/><br/>
 
 
> stack, queue   

스택은 상자 쌓기   
큐는 버스 타기 두 가지만 기억하면 됩니다!<br/><br/><br/>


> DFS
* 기본 원리   
1) 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2) 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은
인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3) 인접한 노드 중에서 방문하지 않은 노드가 여러 개 있으면 번호가 낮은 순서부터 처리한다.

* 주의할 점
1) 좌표, 연결 상황에 제약이 있는 경우? 2차원 배열 이동 상하좌우 밖에 못 움직임, 숫자 조합 => 바로 다음 숫자만 이어붙일 수 있음  이런 경우 dfs를 떠올리자!
2) dfs  같은 경우는 재귀함수가 많이 쓰이고 흔히 점화식이라 생각할 수 있음
3) 방문 표시 =>   
모든 경로 탐색 : 모든 경로에 대해서 방문 표시   
결과값에 대해서 탐색 : 해당 요소에 대해서만 방문표시<br/><br/><br/>

> BFS
* 기본 원리
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

           
* 주의할 점
1) 재귀함수가 불가능
2) 우리 예제에서처럼 최단거리를 탐색할 때 사용 가능<br/><br/><br/>


> 오늘의 문제들
1. 영역 구하기 https://www.acmicpc.net/problem/2583 => dfs 난이도 하

2. 나이트의 이동 https://www.acmicpc.net/problem/7562 => bfs 난이도 중하 

3. 프로그래머스 https://programmers.co.kr/learn/courses/30/parts/12421 => dfs 문제 난이도 중    
: 잘못된 풀이 소개  
```
def solution(numbers, target):
    answer = 0
    result = []
    dic = {}
    dic[0] = [numbers[0], -numbers[0]]
    for i in range(len(numbers) - 1):
        dic[numbers[i]] = [numbers[i + 1], -numbers[i + 1]]
        dic[-numbers[i]] = [numbers[i + 1], -numbers[i + 1]]

    def dfs(index, path):
        if len(path) == len(numbers):
            result.append(path[:])
            a= path.pop()
            while a < 0 and path:
               a=path.pop()
            return

        for i in dic[index]:
            path.append(i)
            dfs(i, path)

    dfs(0, [])
    for i in result:
        if sum(i)==target:
            answer+=1
    return answer
```

파이썬에서 스택, 큐 꼭 append와 pop()을 활용할 필요가 없다. 카운트 하는 문제는 최대한 간단하게 풀어야함!   
   
4. 전화번호 문자 조합  https://leetcode.com/problems/letter-combinations-of-a-phone-number/ => dfs 문제  난이도 중

5. 아기 상어 https://www.acmicpc.net/problem/16236=> bfs 난이도 중상 (집가서 풀기?)
