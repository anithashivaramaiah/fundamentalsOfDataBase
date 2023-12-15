from flask import Flask, render_template, request, session, redirect, url_for, flash
import pymysql
import re

app = Flask(__name__)
app.secret_key = 'FR45tg$%'

# connection = pymysql.connect(host='localhost',
#                             user='root',
#                             password='DE34rf#$',
#                             database='login',
#                             charset='utf8mb4',
#                             cursorclass=pymysql.cursors.DictCursor)
  

connection = None
@app.route('/')
def first():
    return render_template('first.html')

@app.route('/elogin', methods=['GET', 'POST'])    
def elogin():
    #return render_template('employee.html')
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='login',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    # Output message if something goes wrong...
    msg = ''
    if request.method == 'POST':
        cred = list(request.form.listvalues())
        user_name = cred[0][0]
        password = cred[1][0]
        status = 'EM'
        # Check if account exists using MySQL
        with connection:
            with connection.cursor() as cursor:
                #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT * FROM aut_sys WHERE user_name = %s AND password = %s AND status = %s' , (user_name, password, status,))
        # Fetch one record and return result

            account = cursor.fetchone()
            # If account exists in accounts table in out database
            if account:
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['user_id'] = account['user_id']
                session['user_name'] = account['user_name']
                msg = 'Logged in successfully'
                # Redirect to home page
                return redirect(url_for('home'))

            else:
                # Account doesnt exist or username/password incorrect
                msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('elogin.html', msg=msg)  
    return render_template('elogin.html')    

@app.route('/eregister', methods=['GET', 'POST'])
def eregister():
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='login',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    #if request.method == 'POST' and 'user_name' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
    if request.method == 'POST':
        cred = list(request.form.listvalues())
        #print(cred)
        user_name = cred[0][0]
        password = cred[1][0]
        email = cred[2][0]
        status = 'EM'


        with connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM aut_sys WHERE user_name = %s', (user_name,))
                account = cursor.fetchone()
        # If account exists show error and validation checks
                if account:
                    msg = 'Account already exists!'
                elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                    msg = 'Invalid email address!'
                elif not re.match(r'[A-Za-z0-9]+', user_name):
                    msg = 'Username must contain only characters and numbers!'
                elif not user_name or not password or not email:
                    msg = 'Please fill out the form!'
                else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
                    # with connection:
                    with connection.cursor() as cursor:
                        cursor.execute('INSERT INTO aut_sys VALUES (NULL, %s, %s, %s, %s)', (user_name, password, email, status,))
                    connection.commit()
                    msg = 'You have successfully registered!'
                    return render_template('elogin.html', msg=msg)
    elif request.method == 'POST': 
                    # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('eregister.html', msg=msg)

@app.route('/tlogin', methods=['GET', 'POST'])    
def tlogin():
    #return render_template('employee.html')
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='login',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    # Output message if something goes wrong...
    msg = ''
    if request.method == 'POST':
        cred = list(request.form.listvalues())
        user_name = cred[0][0]
        password = cred[1][0]
        status = 'TA'
        # Check if account exists using MySQL
        with connection:
            with connection.cursor() as cursor:
                #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT * FROM aut_sys WHERE user_name = %s AND password = %s AND status = %s' , (user_name, password, status,))
        # Fetch one record and return result

            account = cursor.fetchone()
            # If account exists in accounts table in out database
            if account:
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['user_id'] = account['user_id']
                session['user_name'] = account['user_name']
                msg = 'Logged in successfully'
                # Redirect to home page
                return redirect(url_for('home'))

            else:
                # Account doesnt exist or username/password incorrect
                msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('tlogin.html', msg=msg)  
    return render_template('tlogin.html')    

@app.route('/tregister', methods=['GET', 'POST'])
def tregister():
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='login',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    #if request.method == 'POST' and 'user_name' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
    if request.method == 'POST':
        cred = list(request.form.listvalues())
        #print(cred)
        user_name = cred[0][0]
        password = cred[1][0]
        email = cred[2][0]
        status = 'TA'


        with connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM aut_sys WHERE user_name = %s', (user_name,))
                account = cursor.fetchone()
        # If account exists show error and validation checks
                if account:
                    msg = 'Account already exists!'
                elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                    msg = 'Invalid email address!'
                elif not re.match(r'[A-Za-z0-9]+', user_name):
                    msg = 'Username must contain only characters and numbers!'
                elif not user_name or not password or not email:
                    msg = 'Please fill out the form!'
                else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
                    # with connection:
                    with connection.cursor() as cursor:
                        cursor.execute('INSERT INTO aut_sys VALUES (NULL, %s, %s, %s, %s)', (user_name, password, email, status,))
                    connection.commit()
                    msg = 'You have successfully registered!'
                    return render_template('tlogin.html', msg=msg)
    elif request.method == 'POST': 
                    # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('tregister.html', msg=msg)


@app.route('/login', methods=['GET', 'POST'])
def login():
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='login',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    # Output message if something goes wrong...
    msg = ''
    # print("test1")
    # print(request.method)
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST':
        # and 'user_name' in request.form and 'password' in request.form
        # Create variables for easy access
        cred = list(request.form.listvalues())
        # print("user_name ",cred[0][0])
        # user_name = request.form['user_name']
        # password = request.form['password']
        user_name = cred[0][0]
        password = cred[1][0]

        # Check if account exists using MySQL
        with connection:
            with connection.cursor() as cursor:
                #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT * FROM aut_sys WHERE user_name = %s AND password = %s', (user_name, password,))
        # Fetch one record and return result

            account = cursor.fetchone()
            # If account exists in accounts table in out database
            if account:
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['user_id'] = account['user_id']
                session['user_name'] = account['user_name']
                msg = 'Logged in successfully'
                # Redirect to home page
                return redirect(url_for('home'))

            else:
                # Account doesnt exist or username/password incorrect
                msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)  
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('user_id', None)
   session.pop('user_name', None)
   # cursor.close()
   # session.clear()
   # connection.close()

   # Redirect to login page
   return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='login',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    #if request.method == 'POST' and 'user_name' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
    if request.method == 'POST':
        cred = list(request.form.listvalues())
        #print(cred)
        user_name = cred[0][0]
        password = cred[1][0]
        email = cred[2][0]


        with connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM aut_sys WHERE user_name = %s', (user_name,))
                account = cursor.fetchone()
        # If account exists show error and validation checks
                if account:
                    msg = 'Account already exists!'
                elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                    msg = 'Invalid email address!'
                elif not re.match(r'[A-Za-z0-9]+', user_name):
                    msg = 'Username must contain only characters and numbers!'
                elif not user_name or not password or not email:
                    msg = 'Please fill out the form!'
                else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
                    # with connection:
                    with connection.cursor() as cursor:
                        cursor.execute('INSERT INTO aut_sys VALUES (NULL, %s, %s, %s)', (user_name, password, email,))
                    connection.commit()
                    msg = 'You have successfully registered!'
                    return render_template('login.html', msg=msg)
    elif request.method == 'POST': 
                    # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)

@app.route('/login/home', methods=['GET', 'POST'])
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='login',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT t_id,first_name, last_name, dob, app_name,join_date, ranking, m_name, email, phone FROM talent')
                account = cursor.fetchall()
                print(account)
                return render_template('home.html', account=account)
            # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/insert', methods = ['POST'])
def insert():
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='login',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    if request.method == 'POST':
 
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        app_name = request.form['app_name']
        join_date = request.form['join_date']
        ranking = request.form['ranking']
        email = request.form['email']
        phone = request.form['phone']
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO talent VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (first_name, last_name, email, app_name,None,phone,"","",None,"", dob,join_date, ranking,))
        connection.commit()
        flash("Employee Inserted Successfully")
 
        return redirect(url_for('home'))
    
@app.route('/update', methods = ['GET', 'POST'])
def update():
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='login',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    if request.method == 'POST':

        #my_data = Data.query.get(request.form.get('id'))
        print(request.form)
        t_id = request.form.get('t_id')
        # print(id)
        first_name= request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['DOB']
        app_name = request.form['app_name']
        join_date = request.form['join_date']
        ranking = request.form['ranking']
        # m_name= request.form['m_name']
        email = request.form['email']
        phone = request.form['phone']
        with connection:
            with connection.cursor() as cursor:
                sql = "update talent set first_name=\'"+first_name+"\'   where t_id="+t_id
                print(sql)
                cursor.execute(sql)

                # cursor.execute("update talent set first_name = (?), last_name = (?), dob = (?), app_name= (?), join_date=(?), ranking=(?), email=(?), phone= (?) from talent where t_id = (?)", (first_name, last_name, dob, app_name, join_date, ranking, email, phone, t_id))
                # account = cursor.fetchall()
 
            connection.commit()

        flash("Talent Updated Successfully")
 
        return redirect(url_for('home'))

@app.route('/delete/<t_id>', methods = ['GET', 'POST'])
def delete(t_id):
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='login',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    if request.method == 'GET':
        print("deleted",t_id)

        #my_data = Data.query.get(request.form.get('id'))
        # print(request.form)
        # t_id = request.form.get('t_id')
        with connection:
            with connection.cursor() as cursor:
                sql = "delete from talent where t_id ="+t_id
                print(sql)
                cursor.execute(sql)
            connection.commit()

        flash("Talent deleted Successfully")
        return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)
