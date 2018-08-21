import pymysql.cursors

class DbInterface:
	host="localhost"
	user="root"
	password="root"
	db="PROYECTO"
	charset="utf8mb4"
	connection=None

	def openConnection(self):
		# Connect to the database
		self.connection = pymysql.connect(self.host,user='root',password='root',db='PROYECTO',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

	def getGifById(self, gif_id):
		self.openConnection()		
		try:
			with self.connection.cursor() as cursor:
				sql = "SELECT * FROM `DATOS` WHERE `id`=%s"
				cursor.execute(sql, (gif_id))
				result = cursor.fetchone()
				return result	
		finally:
			self.connection.close()
