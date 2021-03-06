from flask import *
from flask_mysqldb import MySQL

app=Flask(__name__)
#database username,password
mysql=MySQL(app)

@app.route("/")

#def index():
#    cur = mysql.connection.cursor()
#    print("Database opened successfully")
#    cur.execute('''CREATE TABLE GYM(id INTEGER PRIMARY KEY AUTO_INCREMENT,name varchar(255) NOT NULL, age INTEGER NOT NULL,email varchar(255) UNIQUE NOT NULL,phone INTEGER NOT NULL,gender varchar(255) NOT NULL,training varchar(255) NOT NULL,package varchar(255) NOT NULL,address varchar(255) NOT NULL)''')
#    print("Table created successfully")
#    mysql.connection.commit()
#    cur.close()

@app.route("/home")
def home():
    return render_template('home_new.html')

@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route("/package")
def package():
    return render_template('package_new.html')

@app.route("/trainer")
def trainer():
    return render_template('trainer_new.html')

@app.route("/about")
def about():
    return render_template('about_new.html')

@app.route("/register")
def register():
    return render_template('register_new.html')

@app.route("/registration_new",methods = ["POST","GET"])
def registration_new():
    if request.method == "POST":
        try:
            data={}
            data['name']     =   request.form["name"]
            data['age']      =   request.form["age"]
            data['email']    =   request.form["email"]
            data['phone']    =   request.form["phone"]
            data['gender']   =   request.form["gender"]
            data['training'] =   request.form["training"]
            data['package']  =   request.form["package"]
            data['address']  =   request.form["address"]
            cur = mysql.connection.cursor()
            cur.execute("INSERT into GYM(name,age,email,phone,gender,training,package,address)values(%s,%s,%s,%s,%s,%s,%s,%s)",(data['name'],data['age'],data['email'],data['phone'],data['gender'],data['training'],data['package'],data['address']))
            mysql.connection.commit()
            return render_template('registration_new.html',record = data)
        except Exception as error:
            error="Sorry ! Unable to Register......"
            return render_template('error_msg.html',error = error)

@app.route("/view")
def view():
    cur = mysql.connection.cursor()
    cur.execute("select * from GYM")
    rows = cur.fetchall()
    mysql.connection.commit()
    return render_template("view.html",rows = rows)

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/deleterecord",methods = ["POST"])
def deleterecord():
    if request.method == "POST":
        try:
            id1 = request.form["id"]
            cur = mysql.connection.cursor()
            del_sql='''delete from GYM where id = %s'''
            cur.execute(del_sql,id1)
            msg = "User successfully deleted"
            mysql.connection.commit()
            return render_template("deleterecord.html",msg = msg)
        except:
            msg="Sorry unable to delete ! Thankyou for Registering ."
            return render_template("deleterecord.html",msg = msg)
        finally:
            cur.close()

if __name__ == "__main__":
    app.run(debug=True)
'''except:
            error="Sorry ! Unable to Register......"
            return render_template('error_msg.html',error = error) '''
