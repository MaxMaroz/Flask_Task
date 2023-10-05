import os
import psycopg2 
from flask import Flask, render_template, request, url_for, redirect

app = Flask (__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
			    database='flas_db',
			    user=os.environ['DB_USERNAME'],
			    password=os.environ['DB_PASSWORD']
			   )

    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM albums;')
    albums = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', albums=albums)

@app.route('/create', methods=('GET', 'POST'))
def create():
  if request.method == 'POST':
      title = request.form['title']
      author = request.form['author']
      songs_num = int(request.form['songs_num'])
      review = request.form['review']

      conn = get_db_connection()
      cur = conn.cursor()
      cur.execute('INSERT INTO albums (title, author, songs_num, review)'
                  'VALUES (%s, %s, %s, %s)',
                  (title, author, songs_num, review))
      conn.commit()
      cur.close()
      conn.close()
      return redirect(url_for('index'))

  return render_template('create.html')

