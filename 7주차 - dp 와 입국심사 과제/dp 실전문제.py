#1 금광 flipkart 문제
arr =[]
testcase = int(input())
for _ in range(testcase):
    n, m = map(int, input().split())
    array = [[0] * n for i in range(m)]
    example = list(map(int, input().split()))
    for j in range(n):
        for i in range(m):
            array[i][j]=example[j*m +i]

    dp = [[0] * n for i in range(m)]
    for i in range(n-1):
        dp[0][i] = array[0][i]
    for j in range(m-1):
        for i in range(n):
            if i == 0:
                dp[j+1][i] = max(dp[j][i], dp[j][i+1]) + array[j+1][i]
            elif i == n-1:
                dp[j + 1][i] = max(dp[j][i], dp[j][i - 1]) + array[j + 1][i]
            else:
                dp[j + 1][i] = max(dp[j][i], dp[j][i + 1],dp[j][i-1]) + array[j + 1][i]

    arr.append(max(map(max,dp)))
for i in arr:
    print(i)


#2 정수 삼각형
num = int(input())
dp = [0]*num
dp[0] = 0
for i in range(num):
    before = dp[:]
    arr = list(map(int, input().split()))
    for j in range(i+1):
        if j == 0:
            dp[j] = arr[j] + before[j]
        elif j == i:
            dp[j] = arr[j] + before[j-1]
        else:
            dp[j]= arr[j] + max(before[j],before[j-1])

print(max(dp))


#3 병사 배치하기
num = int(input())
arr = list(map(int, input().split()))
dp = [0]*num
ans =0
for i in range(0,num):
    here = 0
    for j in range(0,i):
        print(i,j)
        if arr[i] <arr[j]:
            here = max(here, dp[j])
    dp[i] = here +1
    ans = max(ans, dp[i])
print(num - ans)
