import pymysql.cursors
import sys
import redis
import time
import pickle as cPickle
import hashlib
from datetime import datetime

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

	def getRedisGifs(self):
		R_SERVER  = redis.StrictRedis(host = "localhost", port =6379, db = 0 )
		hash = hashlib.sha224(("SELECT url, descripcion, contador FROM `gifs_gif` ORDER BY contador LIMIT 10").encode('utf-8')).hexdigest()
		key = "sql_cache:"+hash
		print ("New  key ", key)
		
		if(R_SERVER.get(key)):
			print("This was returned from redis")
			return R_SERVER.get(key)
		else:
			data = self.getAllGifs()
			R_SERVER.set(key, cPickle.dumps(data))
			R_SERVER.expire(key, 12)
			print ("Send data to redis and return the data")
			return R_SERVER.get(key)

