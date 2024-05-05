from flask_login import UserMixin  # Flask-Login의 UserMixin을 import합니다.
from db_model.mysql import conn_mysqldb  # MySQL 데이터베이스 연결을 위한 함수를 import합니다.

class User(UserMixin):  # User 클래스를 정의하고 UserMixin을 상속합니다.

    def __init__(self, user_id, user_email, blog_id):
        # User 클래스의 생성자입니다. 사용자의 아이디, 이메일, 블로그 아이디를 초기화합니다.
        self.id = user_id
        self.user_email = user_email
        self.blog_id = blog_id

    def get_id(self):
        # 현재 사용자의 고유 식별자를 반환합니다. 이 메소드는 Flask-Login에서 필요합니다.
        return str(self.id)

    @staticmethod
    def get(user_id):
        # 사용자의 아이디를 인자로 받아 해당 사용자를 데이터베이스에서 검색합니다.
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE USER_ID = '" + \
            str(user_id) + "'"  # SQL 쿼리를 생성합니다.
        db_cursor.execute(sql)  # 쿼리를 실행합니다.
        user = db_cursor.fetchone()  # 쿼리 결과를 가져옵니다.
        if not user:
            db_cursor.close()
            return None

        user = User(user_id=user[0], user_email=user[1], blog_id=user[2])  # User 객체를 생성합니다.
        db_cursor.close()
        return user

    @staticmethod
    def find(user_email):
        # 사용자의 이메일을 인자로 받아 해당 사용자를 데이터베이스에서 검색합니다.
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE USER_EMAIL = '" + \
            str(user_email) + "'"  # SQL 쿼리를 생성합니다.
        db_cursor.execute(sql)  # 쿼리를 실행합니다.
        user = db_cursor.fetchone()  # 쿼리 결과를 가져옵니다.
        if not user:
            db_cursor.close()
            return None

        user = User(user_id=user[0], user_email=user[1], blog_id=user[2])  # User 객체를 생성합니다.
        db_cursor.close()
        return user

    @staticmethod
    def create(user_email, blog_id):
        # 사용자의 이메일과 블로그 아이디를 인자로 받아 새로운 사용자를 생성합니다.
        user = User.find(user_email)  # 해당 이메일의 사용자가 이미 있는지 확인합니다.
        if user == None:
            # 해당 이메일의 사용자가 없을 경우 데이터베이스에 새로운 사용자를 추가합니다.
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            sql = "INSERT INTO user_info (USER_EMAIL, BLOG_ID) VALUES ('%s', '%s')" % (
                str(user_email), str(blog_id))  # SQL 쿼리를 생성합니다.
            db_cursor.execute(sql)  # 쿼리를 실행합니다.
            mysql_db.commit()  # 변경사항을 데이터베이스에 반영합니다.
            return User.find(user_email)  # 새로 생성된 사용자를 반환합니다.
        else:
            return user  # 이미 존재하는 사용자의 경우 해당 사용자를 반환합니다.

    @staticmethod
    def delete(user_id):
        # 사용자의 아이디를 인자로 받아 해당 사용자를 데이터베이스에서 삭제합니다.
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "DELETE FROM user_info WHERE USER_ID = %d" % (user_id)  # SQL 쿼리를 생성합니다.
        deleted = db_cursor.execute(sql)  # 쿼리를 실행하고 삭제된 행의 수를 반환합니다.
        mysql_db.commit()  # 변경사항을 데이터베이스에 반영합니다.
        return deleted  # 삭제된 행의 수를 반환합니다.

