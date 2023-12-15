import os
import psycopg2

conn = psycopg2.connect(
	host="postgres",
	database="flas_db",
	user='baldur',
	password='5459605')

cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS albums (id serial PRIMARY KEY,'
				 'title varchar (150) NOT NULL,'
				 'author varchar (50) NOT NULL,'
				 'songs_num integer NOT NULL,'
				 'review text,'
				 'date_added date DEFAULT CURRENT_TIMESTAMP);')

conn.commit()




