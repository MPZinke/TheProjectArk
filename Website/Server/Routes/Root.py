


from __main__ import app, request, session;
from flask import render_template;


@app.route("/", methods=["GET"])
def index():
	return render_template("index_info.html");



@app.route("/favicon.ico", methods=["GET"])
def favicon():
	return "";