num1 = int(input()) # 행 개수
num2 = int(input()) # 열 개수
input3 = input().split()
input3 = [int(i) for i in input3]
answer = []
for i in range(num1):
    answer.append(min(input3[i * num2: (i + 1) * num2]))
print(max(answer))




