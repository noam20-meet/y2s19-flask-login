from databases import *
from flask import Flask, request, redirect, render_template
from flask import session as login_session, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def home():
    return render_template('home.html')
    

@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'])
    if user != None and user.verify_password(request.form["password"]):
        login_session['name'] = user.username
        login_session['logged_in'] = True
        return logged_in()
    else:
        return home()


@app.route('/signup', methods=['POST'])
def signup():
    #check that username isn't already taken
    user = get_user(request.form['username'])
    if user == None:
        add_user(request.form['username'],request.form['password'])
    return home()


@app.route('/logged-in' , methods=['GET', 'POST'])
def logged_in():
    
    # if request.method == 'POST':
    #     def update_fav_food(username, fav_food):
    #         User_object = session.query(
    #             User).filter_by(
    #             username=username).first()
    #         User_object.fav_food = fav_food
    #         session.commit()
    #     update_fav_food("fav_food", True)
       
    # else: 
    #     current_user= get_user(login_session['name'])
    #     return render_template('home.html', food = current_user.fav_food)
    return render_template('logged.html')

@app.route('/food' , methods=['POST'])
def get_food():
    update_fav_food(login_session['name'], request.form['fav_food'])
    return render_template('logged.html')


        



@app.route('/logout') 
def logout():
    login_session['logged_in'] = False
    return redirect(url_for('home')) 



if __name__ == '__main__':
    app.run(debug=True)
