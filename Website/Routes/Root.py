


from flask import Blueprint, redirect, render_template, request, session;
from Global import *;
from Global import __GLOBAL__set_location_and_render_template;

from Python.Class import User;


Root_Blueprint = Blueprint("Root_Blueprint", __name__, template_folder="MAIN_HTML_DIR", static_folder=STATIC_HTML_DIR);

@Root_Blueprint.route("/", methods=["GET"])
def index():
	session["current"] = "/";
	return rendered_index();


@Root_Blueprint.route("/login", methods=["GET", "POST"])
def login():
	session["current"] = "/login";
	return rendered_login();



@Root_Blueprint.route("/favicon.ico", methods=["GET"])
def favicon():
	return "";


# ————————————————————— RENDERING —————————————————————

def rendered_index():
	params = {"page": request.path}
	if("user" in session): return __GLOBAL__set_location_and_render_template("Home.html", params);
	return __GLOBAL__set_location_and_render_template("Index_Userless.html", params);


def rendered_login():
	# naughty user already logged in and shouldn't be here
	if("user" in session):
		if("previous" in session): return redirect(session["previous"]);
		return redirect("/");

	if(request.method == "GET"): return render_template("Login.html");
	try:
		# new user
		session["user"]	 = request.form["__SIGNIN__name_input"];
		print("LOGIN: pulled data");  #TESTING
		return redirect("/");
	except Exception as error:
		print(error);
		print("LOGIN: trying again");  #TESTING
		return __GLOBAL__set_location_and_render_template("Login.html");
	
