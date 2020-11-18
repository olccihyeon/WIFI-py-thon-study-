#1 국영수
n = int(input())
students = []
for _ in range(n):
    students.append(input().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for student in students:
    print(student[0])

#2 안테나
n = int(input())
a = list(map(int, input().split()))
a.sort()
print(a[(n - 1) // 2])

#3 실패율
def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)
        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        length -= count

    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer