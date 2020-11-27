def solution(n, times):
    a = max(times)
    min_value = 1
    max_value = a*n
    while min_value<=max_value:
        mid = (min_value+max_value)//2
        sum = 0
        for i in times:
            sum = sum + (mid//i)
            if sum >=n:
                break
        if sum == n:
            answer = mid
            max_value = mid -1
        elif sum >n:
            answer = mid
            max_value = mid -1
        else:
            min_value = mid+1
    return answer