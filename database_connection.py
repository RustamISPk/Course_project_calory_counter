from datetime import datetime
from pymysql import connect
import pymysql
from config import host, port, user, passwd, database, user_account_table, user_weight_story_table


class DatabaseConnection:
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
            now = datetime.now()
            formatted_date = now.strftime("%Y-%m-%d")
            insert_query = f"INSERT INTO {user_weight_story_table}(user_id, user_weight, weight_date) VALUES(%s, %s, %s);"
            cursor.execute(insert_query, (user_id, weight, formatted_date))

        self.connection.commit()

    def find_user_in_database(self, login, password):
        with self.connection.cursor() as cursor:
            insert_query = f"SELECT * FROM user_account WHERE user_login = '{login}' AND user_password = '{password}'"
            cursor.execute(insert_query)
            user = cursor.fetchall()
        if len(user) > 0:
            user_id = user[0]['user_id']
            return True, int(user_id)
        else:
            return False, None

    def find_all_food(self):
        with self.connection.cursor() as cursor:
            insert_query = f"SELECT * FROM product_and_recipe_list"
            cursor.execute(insert_query)
            food = cursor.fetchall()
            return food

    def write_eating_db(self, user_id, product_id, product_count, eating_type):
        with self.connection.cursor() as cursor:
            now = datetime.now()
            formatted_date = now.strftime("%Y-%m-%d")
            insert_query = f"INSERT INTO eating (user_id, eating_date, product_id, product_count, " \
                           f"eating_type) VALUES(%s, %s, %s, %s, %s);"
            cursor.execute(insert_query, (
                user_id, formatted_date, product_id, product_count, eating_type))
        self.connection.commit()

    def get_ate_food_by_type(self, user_id, eating_type):
        with self.connection.cursor() as cursor:
            now = datetime.now()
            formatted_date = now.strftime("%Y-%m-%d")
            insert_query = f"SELECT * FROM eating WHERE user_id = '{user_id}' AND eating_date = '{formatted_date}' " \
                           f"AND eating_type = '{eating_type}' "
            cursor.execute(insert_query)
            ate_food = cursor.fetchall()
        return ate_food

    def get_product_by_id(self, id):
        with self.connection.cursor() as cursor:
            now = datetime.now()
            formatted_date = now.strftime("%Y-%m-%d")
            insert_query = f"SELECT product_and_recipe_list.product_name, product_and_recipe_list.calory, " \
                           f"product_and_recipe_list.protein, product_and_recipe_list.fats, " \
                           f"product_and_recipe_list.carbohydrates, users.password, data.data_1, data.data_2 FROM " \
                           f"users,data WHERE " \ 
                           f"users.user_id=data.user_id AND users.email='$user_email' "
            cursor.execute(insert_query)
            ate_food = cursor.fetchall()
        return ate_food
