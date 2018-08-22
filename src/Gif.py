class Gif:
	url=""
	description=""
	count=""

	def __init__(self, gif_dict):
		self.url = gif_dict["url"]
		self.description = gif_dict["descripcion"]
		self.count = gif_dict["contador"]
