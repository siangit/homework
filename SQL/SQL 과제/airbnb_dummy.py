import pymysql
from faker import Faker
import random

# Faker 객체 초기화
fake = Faker()

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='localhost',  # 데이터베이스 서버 주소
    user='root',       # 데이터베이스 사용자 이름
    password='tldkswndlssla',  # 데이터베이스 비밀번호
    db='과제4',       # 데이터베이스 이름
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)





# Products 테이블을 위한 더미 데이터 생성
def generate_product_data(n):
    for _ in range(n):
        product_name = fake.word().capitalize() + ' ' + fake.word().capitalize()
        price = round(random.uniform(10, 100), 2)
        stock_quantity = random.randint(10, 100)
        create_date = fake.date_time_this_year()
        yield (product_name, price, stock_quantity, create_date)
        

# Customers 테이블을 위한 더미 데이터 생성
def generate_customer_data(n):
    for _ in range(n):
        customer_name = fake.name()
        email = fake.email()
        address = fake.address()
        create_date = fake.date_time_this_year()
        yield (customer_name, email, address, create_date)

# Orders 테이블을 위한 더미 데이터 생성
def generate_order_data(n, customer_ids):
    for _ in range(n):
        customer_id = random.choice(customer_ids)
        order_date = fake.date_time_this_year()
        total_amount = round(random.uniform(20, 500), 2)
        yield (customer_id, order_date, total_amount)

# 데이터베이스에 데이터 삽입
with conn.cursor() as cursor:
    # Products 데이터 삽입
    products_sql = "INSERT INTO Products (productName, price, stockQuantity, createDate) VALUES (%s, %s, %s, %s)"
    #UPDATE the quantity by bring the index of data which is stock position
    productupdate_sql = "UPDATE Products SET stockQuantity = stockQuantity-%s WHERE productID = %s"
    searchproduct_sql = "SELECT * FROM Products WHERE productID=%s"

    for data in generate_product_data(1):
        cursor.execute(products_sql, data)
        #product insert with data index3 which is datetime
        cursor.execute(products_sql, ("Algorithm",49.89,10,data[3]))
        #UPDATE the quantity by bring the index of data which is stock position
        cursor.execute(productupdate_sql,(data[2]-1,data[2]))
        cursor.execute(searchproduct_sql,'1')
        result = cursor.fetchall()
        for data in result:
            print(data)
    conn.commit()

    # Customers 데이터 삽입
    customers_sql = "INSERT INTO Customers (customerName, email, address, createDate) VALUES (%s, %s, %s, %s)"
    csql = "SELECT * FROM Customers ORDER BY customerID"
    searchcustomer_squl = "SELECT * FROM Customers WHERE customerID=%s"
    customereamil_sql = "UPDATE Customers SET email=%s WHERE email=%s"
    vipcustomer_sql = "SELECT * FROM Orders Order By totalAmount DESC LIMIT 1"
    for data in generate_customer_data(1):
        cursor.execute(customers_sql, data)
        cursor.execute(customereamil_sql, ('NEW_'+data[1],data[1]))
        # brought all the customers' informations ordered by ID
        # put the each customer's information in tuple
        cursor.execute(csql)
        result = cursor.fetchall()
        for data in result:
            print(data)
        
       
        cursor.execute(searchcustomer_squl,'1')
        searchresult = cursor.fetchall()
        for searchresult in result:
            print(searchresult)

      
        cursor.execute(vipcustomer_sql)
        vipresult = cursor.fetchone()
        print(vipresult)

    conn.commit()

    # Orders 데이터 삽입
    # Customers 테이블에서 ID 목록을 얻어옵니다.
    cursor.execute("SELECT customerID FROM Customers")
    customer_ids = [row['customerID'] for row in cursor.fetchall()]
    
    #sum the totalamount of orders for each customers by grouping the same customerIDs
    orders_sql = "INSERT INTO Orders (customerID, orderDate, totalAmount) VALUES (%s, %s, %s)"
    sumorders_sql = "SELECT customerID, SUM(totalAmount) FROM Orders GROUP BY customerID" 
    cancel_sql = "DELETE FROM Orders WHERE OrderID=%s"
    vipcustomer_sql = "SELECT CustomerID From Orders WHERE MAX(totalAmount)"
    for data in generate_order_data(15, customer_ids):
        cursor.execute(orders_sql, data)
        cursor.execute(cancel_sql, (data[0]))
        

    
    
    

   
    conn.commit()


# 데이터베이스 연결 종료
conn.close()