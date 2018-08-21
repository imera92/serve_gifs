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

	def getGifById(self, gif_id):
		try:
			self.openConnection()
			with self.connection.cursor() as cursor:
				sql = "SELECT * FROM `gifs_gif` WHERE `id`=%s"
				cursor.execute(sql, (gif_id))
				row = cursor.fetchone()
        		gif = Gif(row)
				self.result = gif
		finally:
			self.connection.close()
			return self.result
