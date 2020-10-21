from typing import List
# 10/16
#첫날 같이 풀어본 문제

# num1 = int(input()) # 행 개수
# num2 = int(input()) # 열 개수
# input3 = input().split()
# input3 = [int(i) for i in input3]
# answer = []
# for i in range(num1):
#     answer.append(min(input3[i * num2: (i + 1) * num2]))
# print(max(answer))

# 10/22
# 그리디 &구현 과제 1
def solution1(N : int,K : int)->int:
    answer =0
    while N!=1:
        if N%K==0:
            N=N/K
            answer+=1
        else:
            N-=1
            answer+=1
    return answer
print(solution1(25,5))

# 그리디 &구현 과제 2
def solution2(N: int, PLAN: List[str]) -> List[int]:
    where = [1,1]
    for i in PLAN:
        if i == 'R'and where[1]<N:
            where[1]+=1
        elif i == 'L' and where[1]>1:
            where[1]-=1
        elif i =='U' and where[0]>1:
            where[0]-=1
        elif i =='D' and where[0]<N:
            where[0]+=1
    return where
print(solution2(5,['R','R','R','U','D','D']))

# 그리디 &구현 과제 3
def solution3(N : int) -> int :
    case2 = 6*10*6*10 - 5*9*5*9
    case1 = 6*10*6*10
    answer =0
    for i in range(0,N+1):
        i=str(i)
        if "3" in i:
            answer += case1
        else:
            answer += case2
    return answer
print(solution3(5))


