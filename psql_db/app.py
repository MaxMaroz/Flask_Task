import psycopg2
from waitress import serve
from flask import Flask, render_template, request, url_for, redirect
import init_db

app = Flask (__name__)

def get_db_connection():
    conn = psycopg2.connect(host='postgres',
			    database='flas_db',
                user='baldur',
                password='5459605')

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

if __name__ == "__main__":
    print('Server has being run')
    serve(app, listen='*:8888')

