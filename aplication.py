# importing redirect 
from flask import Flask, redirect, url_for, render_template, request 

# Initialize the flask application 
app = Flask(__name__) 

# It will load the form template which 
# is in login.html 
# @app.route('/') 
# def index(): 
# 	return render_template("login.html") 


# @app.route('/success') 
# def success(): 
# 	return "logged in successfully"

# # loggnig to the form with method POST or GET 
# @app.route("/login", methods=["POST", "GET"]) 
# def login(): 
	
# 	# if the method is POST and Username is admin then 
# 	# it will redirects to success url. 
# 	if request.method == "POST" and request.form["username"] == "admin": 
# 		return redirect(url_for("success")) 

# 	# if the method is GET or username is not admin, 
# 	# then it redirects to index method. 
# 	return redirect(url_for('index')) 


@app.route('/name/<nameofuser>')
def hi_user(nameofuser):
    return f'Hi {nameofuser} ! are you intresting in squareroots'
@app.route('/user/<username>')
def show_user(username):
    return f'Hello {username} !. Welcome to LTIMindtree'

@app.route('/', methods=['GET', 'POST'])
def squarenumber():
 # If method is POST, get the number entered by user
 # Calculate the square of number and pass it to answermaths 
    if request.method == 'POST':
        if(request.form['num'] == ''):
            return "Invalid number."
        else:
            number = request.form['num']
            sq = int(number) * int(number)
            return render_template('answer.html',squareofnum=sq, num=number)
    
    # If the method is GET,render the HTML page to the user
    if request.method == 'GET':
        return render_template("squarenum.html")


if __name__ == "__main__":
    app.run(debug=True) 