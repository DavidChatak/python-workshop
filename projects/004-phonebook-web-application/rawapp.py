import mysql.connector

mydb = mysql.connector.connect(
  host='database-2.cdqj5q1oiaw9.eu-west-3.rds.amazonaws.com',
  user="admin",
  password="Clarusway_1",
  database = "mydatabase"
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("create table rehber(id numeric(4), ad char(20),soyad char(20), numara char(15))")
# mycursor.execute("insert into rehber values(2,'john','Smith','+90-50505555')")
mycursor.execute("select * from rehber")
res = mycursor.fetchall()
print(res)
def add():
    ad=input("Enter the name:").title()
    soyad=input("Enter the sur_name:").title()
    numara=input("Enter the phone number:")
    if any(list(filter(lambda i:i.isalpha,numara))):
        return "hatalı numara girişi"
    mycursor.execute("select ad,soyad from rehber where ad='{ad}' and soyad='{soyad}'")
    adx = mycursor.fetchall()
    if adx==(ad,soyad):
        return f"{ad} {soyad} zaten var.."
    mycursor.execute("select max(id) from rehber")
    id = mycursor.fetchall() + 1
    query = f"insert into rehber values({id},'{ad}','{soyad}','{numara}')"
    mycursor.execute(query)

add()
