from book import Book   # book.py 파일 안에서 => Book 클래스를 main.py에 가져오기
from user import User

# 만들어 둔 클래스들을 활용해서 실제 동작 관련 코드 작성

# 책의 인스턴스 하나를 생성  + 변수에 담아두자
book1 = Book('타짜', 700, 19)   # Book 클래스의 생성자에서는 파라미터 3개 요구 (하도록 수정됨), 사용시에는 arguments를 안 보내고 있다.

# 방금 만든 책의 데이터 설정 ( 타짜, 700, 19 )

# set_data 메쏘드의 self 파라미터에는 book1이 대입됨
# book1.set_data( '타짜', 700, 19 )  # 전달인자 (arguments)들을 self 파라미터만 제외하고 작성

book1.print_book_info()


# 두 번째 책의 인스턴스를 추가로 생성
book2 = Book()

# 두 번째 책의 데이터 설정 ( 드래곤볼, 1000, 15 )
book2.set_data('드래곤볼', 1000, 15)

# 두 번째 책의 정보 출력
book2.print_book_info()

# 연습 문제. 연령제한이 0 => 그때는 전체 이용가로 나타나도록
# 연령 제한이 그 외의 숫자 => ~세 이용가로 나타나도록
book3 = Book()
book3.set_data('뽀로로', 500, 0)
book3.print_book_info()


test02 = '테스트 변수'

# 함수와의 비교를 위한 예시 코드
def add_and_print(num1,num2):
    print(num1 + num2)
    print(test02)

    
    
add_and_print(5, 11)



book1.is_rent_available( 2000 )


num = 10

if num > 5:
    result = '5보다 크다.'
    
print(result)

# 연습문제. 클래스 추가 - User
# set_data 메쏘드 => 이름, 출생년도, 보유포인트를 받아서 저장
# print_user_info 메쏘드 => 위의 3가지 정보 출력


# 사용자 한명 생성 '본인이름', 출생년도, 10000으로 데이터 세팅
# 정보 출력


user1 = User()
user1.set_data ('김현희', 1995, 10000)

print(f'사용자1의 이름 : {user1.name}')

user1.print_user_info()


user2 = User()

user2.name = '김학생'
user2.birth_year = 2005
user2.point = 5000

user2.is_man = False  # 변수를 만들 수는 있지만 추천하지 않음

user2.print_user_info()

# 사용자 클래스에도 생성자 추가. 이름 / 출생 년도 / 포인트 한꺼번에 입력
# 기존 기본생성자()를 유지해보자

user3 =  User('이아동', 2012, 1000)

user3.print_user_info()

# book1의 정보 출력
book1.print_book_info()