# ch05.py (ch05모듈) 자동완성핫키 : Ctrl+space
# 아나콘다에서 Path 추가 안했으면 실행 안됨 > ctrl+shift+p => select interpreter => Python => Python(base) 'base'는 인터프리터다.
# 실행 : cmd 터미널 > 입력 : python ch05.py 
        #방법1 : 우하단 화살표에서 Command Prompt 방법2 : ctrl+j
def my_hello(cnt): #cnt번 반복
    print(__name__)
    for i in range(cnt):
        print('Hello, Python', end='\t')
        print('Hello, World')
if __name__ == '__main__':
    my_hello(2)