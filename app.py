from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Database configuration
DB_NAME = "components.db"
DB_PATH = os.path.join(os.path.dirname(__file__), DB_NAME)

def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS components (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      component_name TEXT NOT NULL,
                      description TEXT NOT NULL,
                      quantity_left INTEGER,
                      date_borrowed TEXT,
                      remarks TEXT
                      )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM components')
    components = cursor.fetchall()
    conn.close()
    return render_template('index.html', components=components)

@app.route('/add_component', methods=['POST', 'GET'])
@app.route('/edit/<int:component_id>', methods=['POST', 'GET'])
def add_or_edit_component(component_id=None):
    if request.method == 'POST':
        component_name = request.form['component_name']
        description = request.form['description']
        quantity_left = int(request.form['quantity_left'])
        date_borrowed = request.form['date_borrowed'] or None
        remarks = request.form['remarks']

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        if component_id:
            cursor.execute('''UPDATE components SET component_name = ?, description = ?, quantity_left = ?, date_borrowed = ?, remarks = ?
                              WHERE id = ?''', (component_name, description, quantity_left, date_borrowed, remarks, component_id))
        else:
            cursor.execute('''INSERT INTO components (component_name, description, quantity_left, date_borrowed, remarks)
                              VALUES (?, ?, ?, ?, ?)''', (component_name, description, quantity_left, date_borrowed, remarks))

        conn.commit()
        conn.close()
        return redirect('/')

    elif request.method == 'GET' and component_id:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM components WHERE id = ?', (component_id,))
        component = cursor.fetchone()
        conn.close()
        return render_template('edit_component.html', component=component)

    else:
        return render_template('add_component.html')

@app.route('/delete/<int:component_id>', methods=['GET'])
def delete_component(component_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM components WHERE id = ?', (component_id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
