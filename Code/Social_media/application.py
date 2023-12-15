from flask import Flask, render_template, request, session, redirect, url_for, flash
import pymysql
import re

application = Flask(__name__)
application.secret_key = 'FR45tg$%'
  
connection = None
@application.route('/')
def first():
    return render_template('first.html')

@application.route('/elogin', methods=['GET', 'POST'])    
def elogin():
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='login',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    msg = ''
    if request.method == 'POST':
        cred = list(request.form.listvalues())
        user_name = cred[0][0]
        password = cred[1][0]
        status = 'EM'
        
        with connection:
            with connection.cursor() as cursor:
                #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT * FROM aut_sys WHERE user_name = %s AND password = %s AND status = %s' , (user_name, password, status,))
    
            account = cursor.fetchone()
            # If account exists in accounts table in out database
            if account:
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['user_id'] = account['user_id']
                session['user_name'] = account['user_name']
                msg = 'Logged in successfully'
                
                return redirect(url_for('ehome'))

            else:
                # Account doesnt exist or username/password incorrect
                msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('elogin.html', msg=msg)  
    return render_template('elogin.html')    

@application.route('/eregister', methods=['GET', 'POST'])
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

@application.route('/tlogin', methods=['GET', 'POST'])    
def tlogin():
    
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
                return redirect(url_for('thome'))

            else:
                # Account doesnt exist or username/password incorrect
                msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('tlogin.html', msg=msg)  
    return render_template('tlogin.html')    

@application.route('/tregister', methods=['GET', 'POST'])
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

@application.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('user_id', None)
   session.pop('user_name', None)
   return redirect(url_for('login'))

@application.route('/elogin/home', methods=['GET', 'POST'])
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the   page
        connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='login',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT t_id,first_name, last_name, dob, application_name,join_date, ranking, m_name, email, phone FROM talent')
                account = cursor.fetchall()
                print(account)
                return render_template('home.html', account=account)
            # User is not loggedin redirect to login page
    return redirect(url_for('elogin'))

@application.route('/dashboard/<t_id>', methods=['GET', 'POST'])
def dashboard(t_id):
    if 'loggedin' in session:
       connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='social_media',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
        
    with connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT d_id, application_id, application_name, m_id, posts, likes, shares, saves, link FROM dashboard where t_id = %s', (t_id,))

                account = cursor.fetchall()
                print(t_id)
                return render_template('dashboard.html', account=account)
      #  return redirect(url_for('home'))

    return redirect(url_for('dashboard',t_id=t_id))

@application.route('/advertisment/<t_id>', methods=['GET', 'POST'])
def advertisment(t_id):
    if 'loggedin' in session:
       connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='social_media',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
        
    with connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT t_id, application_id, application_name, brand_name, partnership, charges FROM advertisement where t_id = %s', (t_id,))

                account = cursor.fetchall()

                return render_template('advertisment.html', account=account)
    return redirect(url_for('dashboard',t_id=t_id))

    #return render_template('dashboard.html')

@application.route('/deliverables/<t_id>', methods=['GET', 'POST'])
def deliverables(t_id):
    print("deliverables")
    print(t_id)
    if 'loggedin' in session:
       connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='social_media',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    with connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT promotion_id, d_id, application_id, rank, status, no_of_uploads, to_be_uploaded, start_date, end_date FROM deliverables where t_id = %s', (t_id,))

                account = cursor.fetchall()

                return render_template('deliverables.html', account=account)
    return redirect(url_for('deliverables',t_id=t_id))

@application.route('/details/<t_id>', methods=['GET', 'POST'])
def details(t_id):
    if 'loggedin' in session:
       connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='social_media',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
        
    with connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT t_id,first_name,last_name,m_name,phone,email,dob, join_date,ranking, refered_by, salary, street, zip FROM talent where t_id = %s', (t_id,))

                account = cursor.fetchall()
                
                return render_template('details.html', account=account)


    return redirect(url_for('dashboard', t_id = t_id))

@application.route('/elogin/ehome', methods=['GET', 'POST'])
def ehome():
    return render_template('ehome.html')


@application.route('/tlogin/thome', methods=['GET', 'POST'])
def thome():
    return render_template('thome.html')


@application.route('/insert', methods = ['POST'])
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
        application_name = request.form['application_name']
        join_date = request.form['join_date']
        ranking = request.form['ranking']
        email = request.form['email']
        phone = request.form['phone']
        application_name = request.form['application_name']
        ref_by = request.form['ref_by']
        salary = request.form['salary']
        street = request.form['street']
        zip_code = request.form['zip']

        with connection.cursor() as cursor: 

            cursor.execute('INSERT INTO talent VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (first_name, last_name, email, application_name,None,phone,street,zip_code,None,"", dob,join_date, ranking,ref_by,salary,))
        connection.commit()
        flash("Employee Inserted Successfully")
 
        return redirect(url_for('home'))

@application.route('/update', methods = ['GET', 'POST'])
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
        application_name = request.form['application_name']
        join_date = request.form['join_date']
        ranking = request.form['ranking']
        email = request.form['email']
        phone = request.form['phone']
        salary = request.form['salary']
        ref_by = request.form['ref_by']
        street = request.form['street']
        zip_code = request.form['zip']
    
        with connection:
            with connection.cursor() as cursor:
                sql = "update talent set first_name=\'"+first_name+"\'  ,last_name=\'"+last_name+"\' ,dob=\'"+dob+"\' ,application_name=\'"+application_name+"\' ,join_date=\'"+join_date+"\' ,ranking=\'"+ranking+"\' ,email=\'"+email+"\' ,phone=\'"+phone+"\' ,ref_by=\'"+ref_by+"\' ,salary=\'"+salary+"\' ,street=\'"+street+"\' ,zip=\'"+zip_code+"\' where t_id="+t_id
                print(sql)
                cursor.execute(sql)
            connection.commit()

        flash("Talent Updated Successfully")
 
        return redirect(url_for('home'))


@application.route('/promotions', methods = ['POST'])
def promotions():
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='social_media',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    if request.method == 'POST':
        
        
        application_id = request.form['application_id']
        application_name = request.form['application_name']
        brand_name = request.form['brand_name']
        partnership = request.form['partnership']
        charges = request.form['charges']

        with connection.cursor() as cursor: 

            cursor.execute('INSERT INTO advertisement VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)', (application_id,None, None, brand_name, partnership,charges,application_name,))
        connection.commit()
        flash("Employee Inserted Successfully")
 
        #return redirect(url_for('advertisment', t_id = t_id))
        return render_template('advertisment.html')

@application.route('/delete/<t_id>', methods = ['GET', 'POST'])
def delete(t_id):
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='login',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    if request.method == 'GET':
        print("deleted",t_id)

        with connection:
            with connection.cursor() as cursor:
                sql = "delete from talent where t_id ="+t_id
                print(sql)
                cursor.execute(sql)
            connection.commit()

        flash("Talent deleted Successfully")
        return redirect(url_for('home'))

@application.route('/addupdate', methods = ['GET', 'POST'])
def addupdate():
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='social_media',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    if request.method == 'POST':

        t_id = request.form.get('t_id')
        
        application_id= request.form['application_id']
        application_name= request.form['application_name']
        brand_name = request.form['brand_name']
        partnership = request.form['partnership']
        charges = request.form['charges']
    
        with connection:
            with connection.cursor() as cursor:
                sql = "update advertisement set application_id=\'"+application_id+"\'  ,application_name=\'"+application_name+"\' ,brand_name=\'"+brand_name+"\' ,partnership=\'"+partnership+"\' ,charges=\'"+charges+"\'  where t_id="+t_id
                print(sql)
                cursor.execute(sql)
            connection.commit()

        flash("Promotions Updated Successfully")
        return redirect(url_for('advertisment',t_id=t_id))

@application.route('/adddelete/<t_id>', methods = ['GET', 'POST'])
def adddelete(t_id):
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='DE34rf#$',
                            database='social_media',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    if request.method == 'GET':
        print("deleted",t_id)

        with connection:
            with connection.cursor() as cursor:
                sql = "delete from advertisement where t_id ="+t_id
                print(sql)
                cursor.execute(sql)
            connection.commit()

        flash("Talent deleted Successfully")
        return redirect(url_for('advertisment',t_id=t_id))
        

if __name__ == "__main__":
    application.run(debug=True)
