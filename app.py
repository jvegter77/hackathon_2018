import os
from flask import Flask, render_template, redirect, request, url_for, session, flash

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def sign_up():	
	#Log_in user and add him to Flask session
    if request.method == "POST":        
        session['user'] = request.form['username']
        flash("Logged in")
        return redirect(url_for('index'))
    if 'user' in session:
        flash("Already logged in")
        return redirect(url_for('index'))
    return render_template("index.html")


@app.route('/logout')
def logout():
	#Logoout user from flask session
    session.pop('user')
    flash("Logged out")
    return_url = request.referrer
    return redirect(return_url)




if __name__ == '__main__':
	if os.environ.get("DEVELOPMENT"):
		app.run(host=os.environ.get('IP'),
				port=os.environ.get('PORT'),
				debug=True)
	else:
		app.run(host=os.environ.get('IP'),
				port=os.environ.get('PORT'),
				debug=False)
