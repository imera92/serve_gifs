import pymysql.cursors
from Gif import Gif

class DbInterface:
	host="localhost"
	user="root"
	password="root"
	db="PROYECTO"
	charset="utf8mb4"
	connection=None
	result=None

	def openConnection(self):
		# Connect to the database
		self.connection = pymysql.connect(self.host,user='root',password='root',db='PROYECTO',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

	def getAllGifs(self):
		try:
			self.openConnection()
			with self.connection.cursor() as cursor:
				sql = "SELECT url, descripcion, contador FROM `gifs_gif` ORDER BY contador LIMIT 10"
				cursor.execute(sql)
				rows = cursor.fetchall()
				result_set = []
				for row in rows:
					gif = []
					gif.append(row["url"])
					gif.append(row["descripcion"])
					gif.append(str(row["contador"]))
					result_set.append(gif)
				self.result = result_set
		finally:
			self.connection.close()
			return self.result
