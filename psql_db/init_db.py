import os
import psycopg2

conn = psycopg2.connect (
	host="localhost",
	database="flas_db",
	user=os.environ['DB_USERNAME'],
	password=os.environ['DB_PASSWORD'])

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS albums;')
cur.execute('CREATE TABLE albums (id serial PRIMARY KEY,'
				 'title varchar (150) NOT NULL,'
				 'author varchar (50) NOT NULL,'
				 'songs_num integer NOT NULL,'
				 'review text,'
				 'date_added date DEFAULT CURRENT_TIMESTAMP);'				 	 )

cur.execute('INSERT INTO albums (title, author, songs_num, review)'
	    'VALUES (%s, %s, %s, %s)',
	    ('Minas Morgul',
	     'Summoning',
	     11,
	     'A great classic!')
	   )

cur.execute('INSERT INTO albums (title, author, songs_num, review)'
	    'VALUES (%s, %s, %s, %s)',
	    ('Arntor',
	     'Windir',
	     7,
	     'Another great classic!')
	   )

conn.commit()

cur.close()
conn.close()

	     
