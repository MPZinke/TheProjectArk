

from flask import render_template, request, session;
from os import getcwd as __OS_getcwd;
from pathlib import Path;
import sys;


PROJECT_DIR = str(Path(__OS_getcwd()));
MAIN_HTML_DIR = PROJECT_DIR+"/HTML/Root";
STATIC_HTML_DIR = PROJECT_DIR+"/HTML/Static";


# use results from query and create an array of dictionaries for each row in the DB.
# takes the DB cursor.
# returns list of dictionaries for each row.
def __GLOBAL__associate_query(cursor):
	headers = [header[0] for header in cursor._description];
	return [{header : (row[x].decode() if row[x] else None) for x, header in enumerate(headers)} \
			for row in cursor._rows];


def __GLOBAL__set_location_and_render_template(template, params={}):
	session["previous"] = request.path;
	return render_template(template, **params);
