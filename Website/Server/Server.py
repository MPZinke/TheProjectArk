


from flask import Flask, request, session;
from json import dumps;
from sys import path as __SYS_path;

from Global import *


# randomly create a key to secure the session
def random_keygen(length):
	from random import randint
	ascii_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c"
	return "".join([ascii_chars[randint(0, 99)] for x in range(length)])


app = Flask(__name__, template_folder=MAIN_HTML_DIR, static_folder=STATIC_HTML_DIR)
app.secret_key = random_keygen(64)

# import other route
__SYS_path.append(PROJECT_DIR+"/Server/Routes");
import Root


# import Requests




def main():
	app.run()


if __name__ == '__main__':
	main()