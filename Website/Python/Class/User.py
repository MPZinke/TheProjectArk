

from Python.Class import Type;


class User:
	def __init__(self, user_id):
		self.id = user_id
		# query DB
		query = {	"first_name": None, "last_name": None, "username": None, "email": None, "password": None, 
					"picture": None, "website": None, "location": None, "info": None, "type_id": None};

		self.first_name = query["first_name"];
		self.last_name = query["last_name"];
		self.username = query["username"];
		self.email = query["email"];
		self.password = query["password"];
		self.picture = query["picture"];
		self.website = query["website"];
		self.location = query["location"];
		self.info = query["info"];
		self.type_id = Type(query["type_id"]);