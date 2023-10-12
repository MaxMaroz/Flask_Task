import os
import psycopg2

conn = psycopg2.connect (
	host="localhost",
	database="flas_db",
	user=os.environ['DB_USERNAME'],
	password=os.environ['DB_PASSWORD'])

cur = conn.cursor()

cur.execute('CREATE TABLE albums (id serial PRIMARY KEY,'
				 'title varchar (150) NOT NULL,'
				 'author varchar (50) NOT NULL,'
				 'songs_num integer NOT NULL,'
				 'review text,'
				 'date_added date DEFAULT CURRENT_TIMESTAMP);'				 	 )




conn.commit()

cur.close()
conn.close()

	     
