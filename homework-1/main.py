"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os
import csv

# Параметры подключения к базе данных
connection_params = {
    "dbname": "north",
    "user": "postgres",
    "password": "1212",
    "host": "localhost"
}

# Подключение к базе данных
conn = psycopg2.connect(**connection_params)
cursor = conn.cursor()

# Путь к папке с данными
data_folder = r"C:\Users\oc83\PycharmProjects\postgres-homeworks\homework-1\north_data"

# Загрузка данных в таблицу employees из employees_data.csv
with open(os.path.join(data_folder, "employees_data.csv"), "r") as file:
    reader = csv.reader(file)
    next(reader)  # пропустить заголовок
    for row in reader:
        cursor.execute(
            "INSERT INTO employees (first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s)",
            (row[1], row[2], row[3], row[4], row[5])
        )

# Загрузка данных в таблицу customers из customers_data.csv
with open(os.path.join(data_folder, "customers_data.csv"), "r") as file:
    reader = csv.reader(file)
    next(reader)  # пропустить заголовок
    for row in reader:
        cursor.execute(
            "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
            (row[0], row[1], row[2])
        )

# Загрузка данных в таблицу orders из orders_data.csv
with open(os.path.join(data_folder, "orders_data.csv"), "r") as file:
    reader = csv.reader(file)
    next(reader)  # пропустить заголовок
    for row in reader:
        cursor.execute(
            "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4])
        )

# Закрыть соединение с базой данных
conn.commit()
cursor.close()
conn.close()