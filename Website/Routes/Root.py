


from flask import Blueprint, render_template, request, session;
from Global import *


Root_Blueprint = Blueprint("Root_Blueprint", __name__, template_folder="MAIN_HTML_DIR", static_folder=STATIC_HTML_DIR);

@Root_Blueprint.route("/", methods=["GET"])
def index():
	return rendered_index();



@Root_Blueprint.route("/favicon.ico", methods=["GET"])
def favicon():
	return "";


def rendered_index():
	params = {"page": request.path}
	if("user" in session): return render_template("Index_User.html", **params);
	return render_template("Index_Userless.html", **params);