import pymysql.cursors

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
				sql = "SELECT * FROM `gifs_gif_old` WHERE `id`=%s"
				cursor.execute(sql, (gif_id))
				self.result = cursor.fetchone()
		finally:
			self.connection.close()
			return self.result
