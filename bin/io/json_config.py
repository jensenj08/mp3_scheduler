import os, json

class JsonConfig: 
	def __init__(self, relative_path):
		self.path = os.path.abspath(relative_path)
		self.type = 'json'
		self.read_or_create_file()

	def read_or_create_file(self):
		if os.path.isfile(self.path): 
			with open(self.path) as json_data_file:
				self.config = json.load(json_data_file)
		else:
			with open(self.path, 'w+') as config_file:
				config_file.write(json.dumps({}))
				self.config = {}

	def save(self):
		print("Writing to: " + self.path)
		with open(self.path, 'w') as outfile:
			json.dump(self.config, outfile)