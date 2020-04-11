
# 2015100902 김현균
# Algorithm to solve Factorial

# 재귀함수
def factorial_recursive(n):
    if n <= 1:
        return n
    else:
        return factorial_recursive(n-1) * n


# 반복적 문제 해결 
def factorial_loop(n):
    result = 1
    if n == 0:
        return n 
    else:
        for _ in range(1, n+1):
            result = result * _
        return result

# 실행시간을 알기위한 패키지
import time
n = [10, 50, 100, 150, 200]

print('Call Recursive')
for i in n:
    print('n = ',i)
    start = time.time() # 코드 시작시간 
    print('value = ', factorial_recursive(i))
    print('Task time : {} sec\n'.format(time.time()-start))   # 소요시간 출력


print('Call loop')
for i in n:
    print('n = ',i)
    start = time.time() # 코드 시작시간 
    print('value = ', factorial_loop(i))
    print('Task time : {} sec\n'.format(time.time()-start))   # 소요시간 출력


