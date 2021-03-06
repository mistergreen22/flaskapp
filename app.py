from flask import Flask, request
import sqlite3
import json

app = Flask(__name__)


@app.route('/create', methods=['POST'])
def create_user():
    try:
        id = 2  # change
        name = request.json['name']
        surname = request.json['surname']
        address = request.json['address']

        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute('INSERT INTO users (id, name, surname, address) VALUES (?, ?, ?, ?)',
                        (id, name, surname, address))

            con.commit()
    except:
        con.rollback()

    finally:
        con.close()
    return 'ok'


@app.route('/get/users', methods=['GET'])
def get_users():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute('SELECT * FROM users')

    rows = cur.fetchall()

    response = json.dumps([dict(x) for x in rows])
    return response


@app.route('/get/user/<int:get_id>', methods=['GET'])
def get_user_by_id(get_id):
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute('SELECT * FROM users where id = ?', str(get_id))

    rows = cur.fetchall()

    response = json.dumps([dict(x) for x in rows])
    return response


@app.route('/update/user/<int:upd_id>', methods=['PUT'])
def update_user_by_id(upd_id):
    new_name = request.json['name']
    new_surname = request.json['surname']
    new_address = request.json['address']
    try:
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute('UPDATE users SET name = ?, surname = ?, address = ?'
                        ' WHERE id = ?',
                        (new_name, new_surname, new_address, str(upd_id)))
            con.commit()
    except:
        con.rollback()
    finally:
        con.close()

    return 'ok'


@app.route('/delete/user/<int:del_id>', methods=['DELETE'])
def delete_user_by_id(del_id):
    try:
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute('DELETE from users WHERE id = ?', str(del_id))
            con.commit()
    except:
        con.rollback()
    finally:
        con.close()

    return 'ok'


if __name__ == '__main__':
    app.run()
