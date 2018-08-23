import pymysql.cursors
import sys
import redis
import time
import pickle as cPickle
import hashlib
import time

class DbInterface:
	host="localhost"
	user="root"
	password="root"
	db="PROYECTO"
	charset="utf8"
	connection=None
	result=None

	def openConnection(self):
		# Connect to the database
		self.connection = pymysql.connect(self.host,user='root',password='root',db='PROYECTO',charset='utf8',cursorclass=pymysql.cursors.DictCursor)

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

	def getRedisGifs(self):
		R_SERVER  = redis.Redis(host = "localhost", port =6379, db = 0 )
		hash = hashlib.sha224(("SELECT url, descripcion, contador FROM `gifs_gif` ORDER BY contador LIMIT 10").encode('utf-8').strip()).hexdigest()
		key = "sql_cache:"+hash
		print ("Key is ", key)
		start_time = time.time()

		if(R_SERVER.get(key)):
			print("This was returned from redis")
			tf = time.time()
			print (tf - start_time)
			return R_SERVER.get(key)
		else:
			data = self.getAllGifs()
			R_SERVER.set(key, cPickle.dumps(data))
			R_SERVER.expire(key, 12)
			tf = time.time()
			print (tf - start_time)
			print ("Send data to redis and return the data")
			return R_SERVER.get(key)

