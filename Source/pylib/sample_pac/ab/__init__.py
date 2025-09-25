'''
sample_pac/ab/__init__.py
ab 패키지를 import할 때 자동 실행되는 파일
from sample_pac.ab import * 을 수행 시, a(* 자리에)모듈만 자동 import되도록
__all__를 셋팅
'''
__all__ = ['a','b','c']
print('sample_pac.ab 패키지 로드')
