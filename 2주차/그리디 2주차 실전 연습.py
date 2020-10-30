#백준 2839 설탕배달
def solution(a):
    three = 0
    five = 0
    i = 0
    while i * 5 <= a:
        if (a - i * 5) % 3 == 0:
            three = (a - i * 5) // 3
            five = i
        i += 1
        print(three, five)

    if three == 0 and five == 0:
        return -1
    return five + three
print(solution(a))

#백준 11399 atm
a= input().split()
a= list(a)
b= input()
a = input().split()
a = list(a)
def solution(a):
    a= [int(i) for i in a]
    a.sort()

    sum = 0
    for i in range(len(a)):
        sum += a[i] * (len(a) - i)
    return sum
print(solution(a))

#백준 1931회의실 배정
allnum = input()
allnum=int(allnum)
order = []
for i in range(allnum):
    b= input().split()
    b = [int(i) for i in b]
    order.append(b)
def solution (order):
     order.sort(key = lambda x: (x[1], x[0]))
     print(order)
     k = 0
     count =0
     for i in range(len(order)):
         if order[i][0]>=k:
             print(order[i])
             count +=1
             k = order[i][1]
     return count
print(solution(order))

#프로그래머스 체육복
def solution(n, lost, reserve):
    answer = 0
    lost1 = list(set(lost) - set(reserve))
    reserve1 = list(set(reserve) - set(lost))

    for i in lost1:
        if i - 1 in reserve1:
            if i - 1 >= 1:
                answer += 1
                reserve1.remove(i - 1)
        elif i + 1 in reserve1:
            if i + 1 <= n:
                answer += 1
                reserve1.remove(i + 1)

    answer = answer + n - len(lost1)
    return answer