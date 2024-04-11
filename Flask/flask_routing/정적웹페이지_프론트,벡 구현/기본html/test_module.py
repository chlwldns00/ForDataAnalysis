def add_one(data):
    return data + 1
 
def add_two(data):
    return data + 2
 
if __name__ == '__main__': # 모듈이 아니라, 해당 코드 직접 실행시만 실행
    print(add_one(10))
    print(add_two(10))