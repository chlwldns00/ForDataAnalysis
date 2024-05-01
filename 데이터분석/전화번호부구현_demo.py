contacts = {}

def add_contact():
    name = input("이름을 입력하세요: ")
    number = input("전화번호를 입력하세요: ")
    contacts[name] = number
    #print("연락처가 추가되었습니다.")

def delete_contact():
    name = input("삭제할 연락처의 이름을 입력하세요: ")
    if name in contacts:
        del contacts[name]
        print("연락처가 삭제되었습니다.")
    else:
        print("해당하는 이름의 연락처가 없습니다.")

def search_contact():
    name = input("이름: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("연락처가 없습니다.")

def display_contacts():

    if contacts:
        #print("연락처 목록:")

        for name, number in contacts.items():
            print(f"{name} 의 전화번호: {number}")
    else:
        print("연락처가 비어 있습니다.")

while True:
    print("\n1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")
    choice = input("번호를 선택하세요: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        delete_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        display_contacts()
    elif choice == '5':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 시도하세요.")