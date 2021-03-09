import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

# database details - to remove some duplication
db_name = 'attitude_data.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer')
def answer():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from customers
    cur.execute('select * from answer')
    rows = cur.fetchall()
    conn.close()
    return render_template('answer.html', rows=rows)

@app.route('/answer_details/<id>')
def answer_details(id):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from customers
    cur.execute('select * from answer WHERE id=?', (id,))
    Identify = cur.fetchall()
    conn.close()
    return render_template('answer_details.html', Identify=Identify)

@app.route('/gender')
def gender():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from orders
    cur.execute('select * from gender')
    rows = cur.fetchall()
    conn.close()
    return render_template('gender.html', rows=rows)


@app.route('/gender_details/<id>')
def opinion(id):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from orders
    cur.execute('select * from gender WHERE id=?', (id,))
    mf = cur.fetchall()
    conn.close()
    return render_template('gender_details.html', mf)
