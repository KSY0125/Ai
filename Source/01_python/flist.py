def safe_index(lst, item): 
    """첫번째 매개변수 lst에서 item 요소가 있는 index를 반환. 
    item 요소가 없으면 -1 반환"""
    if item in lst:
        return lst.index(item) 
    return -1
def safe_index(lst, item, start=0):
    """
    첫번째 매개변수 lst : 리스트, 튜플
    두번째 매개변수 item : 리스트나 튜플에서 찾을 데이터
    세번째 매개변수 start : 몇번째 index부터 찾을지 index 수(기본값:0) #3번째 변수가 추가업데이트 됨. 25.09.19
    """
    return lst.index(item, start) if item in lst[start:] else -1
#     if item in lst[start:]: 
#         return lst.index(item, start) # start번째부터 item이 있는 index를 반환
#     return -1 #없으면 -1을 반환. 