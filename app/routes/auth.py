from flask import Blueprint,render_template,request,url_for,session,redirect,flash

auth_bp = Blueprint('auth',__name__)

USER_CREDENTIALS = {
    'username':'admin',
    'password':'1234'
}

@auth_bp.route('/login',methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['user'] = username
            flash('login successful')
        else:
            flash('invalid username and password')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user',None)
    flash('Logged Out')
    return redirect(url_for('auth.login'))



