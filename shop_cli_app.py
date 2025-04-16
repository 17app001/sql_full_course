
import MySQLdb

# 建立資料庫連線
conn = MySQLdb.connect(
    host="localhost",
    user="your_user",
    passwd="your_password",
    db="your_db",
    charset="utf8"
)
cursor = conn.cursor()

def add_product():
    name = input("商品名稱：")
    price = float(input("價格："))
    cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (name, price))
    conn.commit()
    print("商品已新增！")

def list_products():
    cursor.execute("SELECT id, name, price FROM products ORDER BY id;")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, 名稱: {row[1]}, 價格: {row[2]:.2f}")

def add_customer():
    name = input("顧客姓名：")
    email = input("顧客 Email：")
    cursor.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    print("顧客已新增！")

def place_order():
    list_products()
    product_id = int(input("輸入商品 ID："))
    quantity = int(input("數量："))
    customer_email = input("輸入顧客 Email：")

    cursor.execute("SELECT id FROM customers WHERE email = %s", (customer_email,))
    result = cursor.fetchone()
    if not result:
        print("查無顧客，請先新增")
        return

    customer_id = result[0]
    cursor.execute("INSERT INTO orders (customer_id, product_id, quantity) VALUES (%s, %s, %s)",
                   (customer_id, product_id, quantity))
    conn.commit()
    print("訂單已新增！")

def list_orders():
    cursor.execute("""
        SELECT o.id, c.name, p.name, o.quantity, p.price, o.quantity * p.price AS total
        FROM orders o
        JOIN customers c ON o.customer_id = c.id
        JOIN products p ON o.product_id = p.id
        ORDER BY o.id;
    """)
    for row in cursor.fetchall():
        print(f"訂單ID: {row[0]}, 顧客: {row[1]}, 商品: {row[2]}, 數量: {row[3]}, 單價: {row[4]}, 總價: {row[5]:.2f}")

def main():
    while True:
        print("\n== 小型商店系統 ==")
        print("1. 新增商品")
        print("2. 查詢商品")
        print("3. 新增顧客")
        print("4. 建立訂單")
        print("5. 查詢訂單")
        print("0. 離開")
        choice = input("請輸入選項：")

        if choice == "1":
            add_product()
        elif choice == "2":
            list_products()
        elif choice == "3":
            add_customer()
        elif choice == "4":
            place_order()
        elif choice == "5":
            list_orders()
        elif choice == "0":
            break
        else:
            print("無效選項")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
