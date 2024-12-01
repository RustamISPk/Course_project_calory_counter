import time
from bs4 import BeautifulSoup
import requests
from pymysql.cursors import Cursor
from pymysql import connect
import pymysql
from config import host, port, user, passwd, database, product_table
import re


class ProductParser:
    def __init__(self):
        self.connection = None
        self.filepath = 'products.txt'
        self.products_links_arr = []
        self.test_connection_to_db()
        self.execute_links()
        self.parser()

    def execute_links(self):
        with open(self.filepath, 'r') as product_file:
            self.products_links_arr = product_file.readlines()
            product_file.close()
        self.products_links_arr = [product_link.rstrip() for product_link in self.products_links_arr]
        print(self.products_links_arr)

    def get_html_body(self, link):
        try:
            response = requests.get(link)
            return response.text
        except Exception as e:
            with open('error.txt', 'a') as error_file:
                error_file.writelines(str(e))
                error_file.close()

    def parse_data_from_html(self, html):
        product = {
            'name': '',
            'calory': '',
            'protein': '',
            'fats': '',
            'carbohydrate': ''
        }
        html_parser = BeautifulSoup(html, "html.parser")
        name_block = html_parser.find('h1', {'id': 'page-title'}).text
        product['name'] = name_block
        calory_block = html_parser.find('div', {'class': 'field field-type-number-decimal field-field-kcal'}).text
        calory_block = self.remove_words(calory_block)
        product['calory'] = calory_block
        protein_block = html_parser.find('div', {'class': 'field field-type-number-decimal field-field-protein'}).text
        protein_block = self.remove_words(protein_block)
        product['protein'] = protein_block
        fats_block = html_parser.find('div', {'class': 'field field-type-number-decimal field-field-fat'}).text
        fats_block = self.remove_words(fats_block)
        product['fats'] = fats_block
        carbohydrate_block = html_parser.find('div', {'class': 'field field-type-number-decimal '
                                                               'field-field-carbohydrate'}).text
        carbohydrate_block = self.remove_words(carbohydrate_block)
        product['carbohydrate'] = carbohydrate_block
        return product

    def parser(self):
        count = 0
        for product_link in self.products_links_arr:
            time.sleep(3)
            try:
                html = self.get_html_body(product_link)
                product = self.parse_data_from_html(html)
                self.save_product_in_database(product)
                count += 1
                print(f'Продукт {count} из {len(self.products_links_arr)} сохранен')
            except Exception as e:
                with open('error.txt', 'a') as error_file:
                    error_file.writelines(f'{e} ссылка {product_link}\n')
                    error_file.close()

    def remove_words(self, input_string):
        cleaned_string = re.sub(r'[^0-9.]', '', input_string)
        return cleaned_string

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
            print("successfully connected")
            print("#" * 20)
        except Exception as ex:
            print("Connection refused...")
            print(ex)

    def save_product_in_database(self, product):
        with self.connection.cursor() as cursor:
            insert_query = f"INSERT INTO {product_table}(product_name, calory, protein, fats, carbohydrates) VALUES(" \
                           f"%s, %s, %s, %s, %s); "
            cursor.execute(insert_query, (
                product['name'], product['calory'], product['protein'], product['fats'], product['carbohydrate']))
            self.connection.commit()
            cursor.close()


a = ProductParser()
