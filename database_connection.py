from datetime import datetime
from pymysql import connect
import pymysql
from config import host, port, user, passwd, database, user_account_table, user_weight_story_table


class DatabaseConnection():
    def __init__(self):
        self.connection = None
        self.test_connection_to_db()

    def test_connection_to_db(self):
        try:
            self.connection = connect(
                host=host,
                port=port,
                user=user,
                password=passwd,
                database=database,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Successfully connected")
            print("#" * 20)
        except Exception as ex:
            print("Connection refused...")
            print(ex)

    def save_user_account(self, name, surname, login, password, height, weight, age, gender):
        with self.connection.cursor() as cursor:
            insert_query = f"INSERT INTO {user_account_table}(user_name, user_lastname, user_login, user_password, " \
                           f"user_height, user_birthdate, user_gender) VALUES(%s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(insert_query, (
                name, surname, login, password, height, age, gender))

            user_id = self.connection.insert_id()
            print(user_id)

            now = datetime.now()
            formatted_date = now.strftime("%Y-%m-%d")
            print(formatted_date)
            insert_query = f"INSERT INTO {user_weight_story_table}(user_id, user_weight, weight_date) VALUES(%s, %s, %s);"
            cursor.execute(insert_query, (user_id, weight, formatted_date))

        self.connection.commit()
        print('Данные успешно сохранены')

