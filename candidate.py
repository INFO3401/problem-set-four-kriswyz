class candidate:
	def __init__(slef, name, data):
		self.candidate = name
		self.data = data.loc[data['endorsee'] == name]

	def countEndorsements(self):
		return self.countEndorsements 		