# Ctrl + Shift + P => select interpreter => Base
# Ctrl + j : cmd창에서 테스트 하려면 python fibonacci.py 100 
def fibonacci_print(n):
    '''
    매개변수로 들어온 n값 미만의 피보나치 수열을 출력하는 함수
    ex. n=10 : 0, 1, 1, 2, 3, 5, 8 - 10 미만
    ex. n=100 : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 - 100 미만
        논리 : 0+1=1이라 0,1,1로 정렬 그 다음 1+1=2라서 0,1,1,2가 됨
    '''
    a, b = 0, 1 # 함수 내에 선언한 변수 : 지역변수 (반대말은 '전역변수')
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print() # 개행
def fibonacci(n):  #1.2절에서 만든 피보나치 함수에 덮어씌워져서 기존 함수는 이것으로 대체되어 사라짐..
    "n미만의 피보나치 수열을 리스트로 return"
    result = [] # 피보나치 수열을 append할 리스트
    a, b = 0, 1
    while a<n:
        result.append(a) # 출력대신 비어진 리스트에 계속 append 해서 채워지는 개념
        a, b = b, a+b
    return result

# 피보나치 수열 관련 함수들 테스트(cmd창에서 python fibonacci.py 100)
if __name__=="__main__":
    import sys
    if len(sys.argv) > 1:  # sys.argv는 원래 명령줄 인자를 받을 때 쓰는 것
        n = int(sys.argv[1])
    else:
        n = int(input("n? "))
    print("1. print test :", end=' ')
    fibonacci_print(n)
    print("2. return test :", fibonacci(n))