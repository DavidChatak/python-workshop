from flask import Flask, request, render_template, redirect,url_for
from flaskext.mysql import MySQL
from   configDB import ConfigDB
config = ConfigDB()
app=Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] =config.host 
app.config['MYSQL_DATABASE_USER'] = config.user
app.config['MYSQL_DATABASE_PASSWORD'] = config.password
app.config['MYSQL_DATABASE_DB'] = config.db
app.config['MYSQL_DATABASE_PORT'] = config.port

mysql = MySQL()
mysql.init_app(app)
connection = mysql.connect()
cursor = connection.cursor()
drop_table = 'DROP TABLE IF EXISTS persons;'
phone_table= """
create table persons(id INT AUTO_INCREMENT PRIMARY KEY,
    person varchar(30) not null,
    number decimal(15) not null )
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
"""
data = """
insert into phone_book.persons(person,number) values("David Chataque", 505050050),("john smith",0090505343434)
"""
cursor.execute(drop_table)
cursor.execute(phone_table)
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
    return render_template("index.html", name=word,developer_name = developer_name,show_result=True,persons = persons,note=note)
def check(word,num):
    cursor.execute("select * from persons")
    res = cursor.fetchall()
    res= [row[1] for row in res]
    message=False
    if word in res:
        message="it exists already..."
        return message
    if not any([j.isdecimal() for j in str(num)]):
        message = "invalid number, check again please.."
        return message
    return message
def add(word,num):
    res = check(word,num)
    if res == False:
        query = f"insert into phone_book.persons(person,number) values('{word}',{num})"
        cursor.execute(query)
        connection.commit()
        return f"{word} is added successfully"
    else:
        return res
def update(word,newword,newnum):
    cursor.execute("select * from persons")
    res = cursor.fetchall()
    res= [row[1] for row in res]
    if word in res:
        query= f"update persons set person='{newword}', number='{newnum}' where person='{word}'"
        cursor.execute(query)
        connection.commit()
        return ("update done")
    else:
        return (f"{word} ---> no such a person")
def delete_person(word):
    cursor.execute("select * from persons")
    res = cursor.fetchall()
    res= [row[1] for row in res]
    if word in res:
        query= f"delete from persons where person='{word}'"
        cursor.execute(query)
        connection.commit()
        return (f"{word} deleted...")
    else:
        return (f"{word} ---> no such a person")
    
# add("MARY",234234234)

@app.route("/<action>",methods=["GET"])
def add_up(action):
    action == action.lower()
    return render_template("add-update.html",action_name=action,developer_name=developer_name)
@app.route("/<action>",methods=["POST"])
def add_update(action):    
    action == action.lower()
    if action == 'add':
        word = request.form["username"].title()
        num = request.form["phonenumber"]
        if not num.isdecimal():
            message="number is not valid, try again plz...."
            return render_template("add-update.html",message=message,action_name=action,developer_name=developer_name,not_valid=True)
        result = add(word,num)
        return render_template("add-update.html",show_result=True,result=result,action_name=action,developer_name=developer_name)
    elif action == 'update':
        word = request.form["username"].title()
        newword = request.form["newusername"].title()
        newnum = request.form["newphonenumber"]
        if not newnum.isdecimal():
            message="number is not valid, try again plz...."
            return render_template("add-update.html",message2=message,action_name=action,developer_name=developer_name,not_valid2=True)
        result = update(word,newword,newnum)
        return render_template("add-update.html",show_result2=True,result2=result,action_name=action,developer_name=developer_name)
@app.route('/delete',methods=["GET"])
def delete():
    return render_template("delete.html",show_result=False,developer_name=developer_name)
@app.route('/delete',methods=["POST"])
def delete_per():
    word = request.form["username"].title()
    result=delete_person(word)
    return render_template("delete.html",show_result=True,result=result,developer_name=developer_name)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
