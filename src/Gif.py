class Gif:
	gif_id=""
	url=""
	description=""
	count=0

	def __init__(self, gif_dict):
		self.gif_id = gif_dict["id"]
		self.url = gif_dict["url"]
		self.description = gif_dict["descripcion"]
		self.count = gif_dict["contador"]