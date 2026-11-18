import sqlite3

# Подключаемся к базе данных
connect = sqlite3.connect("store.db")

# Создаём курсор для работы с базой данных
cursor = connect.cursor()

# Создаём таблицу products
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
""")

connect.commit()


# CREATE — добавление товара
def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    connect.commit()


# READ — получение всех товаров
def read_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    for product in products:
        print(product)


# UPDATE — изменение цены товара
def update_product(id, price):
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (price, id)
    )
    connect.commit()


# DELETE — удаление товара
def delete_product(id):
    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (id,)
    )
    connect.commit()


# Добавляем товары
create_product("Laptop", 50000, 5)
create_product("Mouse", 1500, 10)
create_product("Keyboard", 3000, 7)

# Выводим все товары
print("Все товары:")
read_products()

# Изменяем цену товара с id 1
update_product(1, 55000)

print("После изменения цены:")
read_products()

# Удаляем товар с id 2
delete_product(2)

print("После удаления:")
read_products()

# Закрываем соединение с базой данных
connect.close()