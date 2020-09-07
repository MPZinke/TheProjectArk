

from os import getcwd as __OS_getcwd;
from pathlib import Path;
import sys;

PROJECT_DIR = str(Path(__OS_getcwd()).parent);
MAIN_HTML_DIR = PROJECT_DIR+"/HTML/Main";
STATIC_HTML_DIR = PROJECT_DIR+"/HTML/Static";

print(PROJECT_DIR);

# sys.path.append("./Connections")

# from DBConnect import connect_to_DB


# CNX, CURSOR = connect_to_DB();


# use results from query and create an array of dictionaries for each row in the DB.
# takes the DB cursor.
# returns list of dictionaries for each row.
def __GLOBAL__associate_query(cursor):
	headers = [header[0] for header in cursor._description];
	return [{header : (row[x].decode() if row[x] else None) for x, header in enumerate(headers)} \
			for row in cursor._rows];

