import sqlite3
from flask import Flask, g, render_template

app = Flask(__name__)

# database details - to remove some duplication
db_name = 'attitude_data.db'

def connect_db():
    conn = sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn.row_factory = sqlite3.Row
    return conn

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ID')
def ID():
    db = get_db()
    # get results from customers
    cur = db.execute("select * from ID")
    rows = cur.fetchall()
    return render_template('ID.html', rows=rows)

@app.route('/ID_details/<id>')
def ID_details(id):
    db = get_db()
    # get results from customers
    cur = db.execute('select * from ID WHERE id=?', (id,))
    Identify = cur.fetchall()
    return render_template('ID_details.html', Identify=Identify)

@app.route('/gender')
def gender():
    db = get_db()
    # get results from orders
    cur = db.execute('select * from gender')
    rows = cur.fetchall()
    return render_template('gender.html', rows=rows)


@app.route('/gender_details/<id>')
def gender_details(id):
    db = get_db()
    # get results from orders
    cur = db.execute('select * from gender WHERE id=?', (id,))
    mf = cur.fetchall()
    return render_template('gender_details.html', mf=mf)
