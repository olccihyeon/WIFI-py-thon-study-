#1 위에서 아래로
num = int(input( ))
list =[]
for i in range(num):
    list.append(int(input()))
list.sort(reverse=True)
for i in list:
    print(i, end =' ')


#2 성적이 낮은 순서로 학생 출력하기
num = int(input())
dic = {}
for i in range(num):
    a = list(map(str, input().split( )))

    dic[a[0]]= int(a[1])

dic = sorted(dic.items(), key = lambda x : x[1])

for i in dic:
    print(i[0],end =' ')

#3 두 배열의 원소 교체
num = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)
for i in range(num[1]):
    if a[i]<b[i]:
        tem  = a[i]
        a[i] = b[i]
        b[i] = tem
print(sum(a))