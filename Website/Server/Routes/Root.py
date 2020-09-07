


from __main__ import app, request, session;
from flask import render_template;


@app.route("/", methods=["GET"])
def index():
	if("user" not in session): return render_template("login.html")
	return render_template("index.html", user=session["user"])



@app.route("/login", methods=["GET", "POST"])
def login():
	pass;
	# if(request.method == "GET"): return render_template("login.html");  # here to login

	# # POST
	# if("user" in session): return render_template("index.html", user=session["user"])  # already logged in

	# # validate inputs
	# if("username" not in request.form or not request.form["username"]):
	# 	return render_template("login.html", error="No user name provided");
	# if("password" not in request.form or not request.form["password"]):
	# 	return render_template("login.html", error="No password provided");
	# username = request.form["username"]
	# password = request.form["password"]
	# print(username, "\n", password)  #TESTING

	# verify data intregrity
	# ldap check
	# create object
	# session["user"] = username  #TODO: store object
	return json.dumps({"status" : True})


@app.route("/signup", methods=["POST"])
def signup():
	pass;