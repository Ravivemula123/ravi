from flask import * 
import mysql.connector as msql
from mysql.connector import Error
from flask_session import Session

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
sess = Session()
@app.route('/',methods=["GET","POST"])
def home():
    return render_template('home.html')

@app.route('/register',methods=["GET","POST"])
def register():
    conn = msql.connect(host='127.0.0.1', database='test', user='root', password='Ravi@775829')
    cursor = conn.cursor()
    if request.method=="POST":
        First_name= request.form.get("First_name")
        Last_name=request.form.get("Last_name")
        Username= request.form.get("Username")
        Password=request.form.get("Password")
        Confirm_password= request.form.get("Confirm_Password")
        Email=request.form.get("Email")
        x="INSERT into test.register (First_name,Last_name,Username,Password,Confirm_password,Email) values (%s,%s,%s,%s,%s,%s)"
        y=(First_name,Last_name,Username,Password,Confirm_password,Email)
        cursor.execute(x,y)
        result=cursor.fetchall()
        for i in result:
            print(i)
        conn.commit()
        return "register sucessfully"
   
    return render_template('register.html')   


@app.route('/login',methods=["POST","GET"])
def login():
    conn = msql.connect(host='127.0.0.1', database='test', user='root', password='Ravi@775829')
    cursor = conn.cursor()
    msg = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL

        cursor.execute('SELECT * FROM test.register WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        print(account)
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['username'] = account[3]
            session['password'] = account[4]
            msg='login sucessfully'
            # Redirect to home page
            return render_template('main.html',msg=msg)
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)
    
@app.route ('/main')
def main():
    return render_template('main.html')
  
if __name__=="__main__":
    app.run(debug=True)    
