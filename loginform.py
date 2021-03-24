import mysql.connector
from flask import Flask,render_template,request

def password_checker(name):
    mydb = mysql.connector.connect(host="localhost", username='root1', passwd="********", database="mydb")
    mycursor = mydb.cursor()
    sql = "SELECT password FROM records WHERE name = '{value}'"
    name = name
    sql = sql.format(value=name)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result
def name_checker(name):
    mydb = mysql.connector.connect(host="localhost", username='root1', passwd="*********", database="mydb")
    mycursor = mydb.cursor()
    sql = "SELECT name FROM records WHERE name = '{value}'"
    name = name
    sql = sql.format(value=name)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("login_form.html")

@app.route('/validation',methods = ['POST'])
def validation():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['pwd']
    valid_pwd = password_checker(user)
    name_validation = name_checker(user)
    if name_validation == []:
        return "User Name not available"
    elif name_validation[0][0] == user:
        if valid_pwd == password:
            return f"welcome {user}"
        else:
            return "password invalid"



if __name__ == '__main__':
    app.run(debug=True)


