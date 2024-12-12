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
            insert_query = f"INSERT INTO {user_weight_story_table}(user_id, user_weight, weight_date) VALUES(%s, %s, " \
                           f"%s); "
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

    def get_product_by_id(self, product_id, eating_id):
        with self.connection.cursor() as cursor:
            now = datetime.now()
            formatted_date = now.strftime("%Y-%m-%d")
            insert_query = f"SELECT p.product_name, p.calory, p.protein, p.fats, p.carbohydrates,e.eating_date, " \
                           f"e.product_count, e.eating_type FROM product_and_recipe_list p INNER JOIN eating e ON " \
                           f"p.product_id = e.product_id WHERE p.product_id = {product_id} AND e.eating_date = " \
                           f"'{formatted_date}' AND e.eating_id = '{eating_id}'; "
            cursor.execute(insert_query)
            ate_food = cursor.fetchall()
        return ate_food

    def remove_eating(self, eating_id):
        with self.connection.cursor() as cursor:
            insert_query = f"DELETE FROM eating WHERE eating_id = '{eating_id}'"
            cursor.execute(insert_query)
        self.connection.commit()

    def get_user_birth_date(self, user_id):
        with self.connection.cursor() as cursor:
            insert_query = f"SELECT * FROM user_account WHERE user_id = '{user_id}'"
            cursor.execute(insert_query)
            ate_food = cursor.fetchall()
        return ate_food[0]['user_birthdate']

    def change_user_params(self, user_id, user_height, user_weight, user_age, user_gender):
        with self.connection.cursor() as cursor:
            if user_weight == '' and user_height != '':
                insert_query = f"UPDATE user_account SET user_height = '{user_height}', user_birthdate = '{user_age}'," \
                               f" user_gender = '{user_gender}' WHERE user_id = {user_id}"
                cursor.execute(insert_query)
                self.connection.commit()
            elif user_weight != '' and user_height == '':
                insert_query = f"INSERT INTO user_weight_story (user_id, user_weight, weight_date) VALUES(%s, %s, %s);"
                now = datetime.now()
                formatted_date = now.strftime("%Y-%m-%d")
                cursor.execute(insert_query, (
                    user_id, user_weight, formatted_date))
                self.connection.commit()
            elif user_weight != '' and user_height != '':
                insert_query = f"UPDATE user_account SET user_height = '{user_height}', user_birthdate = '{user_age}'," \
                               f" user_gender = '{user_gender}' WHERE user_id = {user_id}"
                cursor.execute(insert_query)
                insert_query = f"INSERT INTO user_weight_story (user_id, user_weight, weight_date) VALUES(%s, %s, %s);"
                now = datetime.now()
                formatted_date = now.strftime("%Y-%m-%d")
                cursor.execute(insert_query, (
                    user_id, user_weight, formatted_date))
                self.connection.commit()
            elif user_weight == '' and user_height == '':
                print('WTF???')

    def save_product_in_database(self, product):
        with self.connection.cursor() as cursor:
            insert_query = f"INSERT INTO product_and_recipe_list (product_name, calory, protein, fats, carbohydrates) " \
                           f"VALUES(%s, %s, %s, %s, %s); "
            cursor.execute(insert_query, (
                product['name'], product['calory'], product['protein'], product['fats'], product['carbohydrate']))
            self.connection.commit()
            cursor.close()

