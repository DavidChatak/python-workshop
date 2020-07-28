from flask import Flask, request, render_template, redirect,url_for
from flaskext.mysql import MySQL
app=Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'database-2.cdqj5q1oiaw9.eu-west-3.rds.amazonaws.com'
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Clarusway_1'
app.config['MYSQL_DATABASE_DB'] = 'phone_book'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql = MySQL()
mysql.init_app(app)
connection = mysql.connect()
cursor = connection.cursor()
drop_table = 'DROP TABLE IF EXISTS persons;'
phone_table= """
create table persons(
id decimal(5) not null,
person varchar(30) not null,
number decimal(15) not null )
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
"""
data = """
insert into phone_book.persons(id,person,number) values(1,"David Chataque", 505050050),(2,"john smith",0090505343434)
"""
# cursor.execute(drop_table)
# cursor.execute(phone_table)
cursor.execute(data)
developer_name = "David CHATAQUE"

def find(word):
    query = f"select person, number from phone_book.persons where person like '%{word}%'"
    cursor.execute(query)
    result = cursor.fetchall()
    person = [(row[0],row[1]) for row in result]
    if not any(person):
        person = [('Not found.', 'Not Found.')]
    return person
@app.route("/")
@app.route("/index", methods=['GET'])
def index():
    query="select * from phone_book.persons"
    note = cursor.execute(query)
    return render_template("index.html", developer_name = developer_name,note=note)
@app.route("/index", methods=['POST'])
def show():
    query="select * from phone_book.persons"
    note = cursor.execute(query)
    
    word = request.form["username"]
    persons = find(word)
    return render_template("index.html", developer_name = developer_name,show_result=True,persons = persons,note=note)

def add(word,num):
    id=cursor.execute("select max(id) from phone_book.persons")+1
    query = f"insert into phone_book.persons values({id},'{word}',{num})"
    cursor.execute(query)
    return f"{word} is added successfully"

@app.route("/add-update", methods=["GET", "POST"])
def add_update():
    action_name="add"
    return render_template("add-update.html", action_name=action_name,developer_name=developer_name)

@app.route("/add",methods=["POST"])
def add():
    word = request.form["username"]
    num = request.form["phonenumber"]
    result = add(word,num)
    return render_template("add-update.html",show_result=True, result=result,developer_name=developer_name)






if __name__ == "__main__":
    app.run(debug=True)