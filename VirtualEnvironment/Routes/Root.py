


from flask import render_template, Blueprint;
from Global import *


Root_Blueprint = Blueprint("Root_Blueprint", __name__, template_folder="MAIN_HTML_DIR", static_folder=STATIC_HTML_DIR);

@Root_Blueprint.route("/", methods=["GET"])
def index():
	return render_template("index_info.html");



@Root_Blueprint.route("/favicon.ico", methods=["GET"])
def favicon():
	return "";