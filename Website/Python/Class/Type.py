


class Type:
	def __init__(self, type_id):
		self.id = type_id;
		query = {"id": None, "title": None, "variable": None, "description": None};

		self.title = query["title"];
		self.variable = query["variable"];
		self.description = query["description"];