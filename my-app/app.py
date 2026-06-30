from flask import Flask, request, render_template_string
import sqlite3
import os

app = Flask(__name__)
DB_PATH = 'data/library.db'


def init_db():
    if not os.path.exists('data'): os.makedirs('data')
    conn = sqlite3.connect(DB_PATH)
    # Добавили поле 'status' (0 - не прочитано, 1 - прочитано)
    conn.execute('''CREATE TABLE IF NOT EXISTS books 
                    (id INTEGER PRIMARY KEY, title TEXT, author TEXT, status INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect(DB_PATH)
    if request.method == 'POST':
        if 'add' in request.form:
            title, author = request.form['title'], request.form['author']
            conn.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
        elif 'del' in request.form:
            conn.execute('DELETE FROM books WHERE id = ?', (request.form['id'],))
        elif 'toggle' in request.form:
            conn.execute('UPDATE books SET status = 1 - status WHERE id = ?', (request.form['id'],))
        conn.commit()

    search = request.args.get('q', '')
    query = 'SELECT * FROM books WHERE title LIKE ? OR author LIKE ?'
    books = conn.execute(query, (f'%{search}%', f'%{search}%')).fetchall()
    conn.close()

    html = """
    <!DOCTYPE html>
    <html lang="ru"><head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background: #f8f9fa; }
        .card { border-radius: 15px; border: none; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        .read { text-decoration: line-through; color: #6c757d; }
    </style></head><body>
    <div class="container mt-5">
        <div class="card p-4 mb-4">
            <h2 class="text-primary">📚 Моя библиотека</h2>
            <form method="POST" class="row g-3 mt-2">
                <div class="col-md-5"><input name="title" placeholder="Название книги" class="form-control" required></div>
                <div class="col-md-4"><input name="author" placeholder="Автор" class="form-control" required></div>
                <div class="col-md-3"><button name="add" class="btn btn-success w-100">Добавить книгу</button></div>
            </form>
        </div>

        <form class="mb-3"><input name="q" class="form-control" placeholder="🔍 Поиск по названию или автору..."></form>

        <ul class="list-group">
            {% for b in books %}
            <li class="list-group-item d-flex justify-content-between align-items-center">
                <span class="{{ 'read' if b[3] == 1 }}">{{ b[1] }} — <b>{{ b[2] }}</b></span>
                <form method="POST" class="btn-group">
                    <input type="hidden" name="id" value="{{ b[0] }}">
                    <button name="toggle" class="btn btn-sm btn-outline-info">✔</button>
                    <button name="del" class="btn btn-sm btn-outline-danger">✕</button>
                </form>
            </li>
            {% endfor %}
        </ul>
    </div></body></html>
    """
    return render_template_string(html, books=books)


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)