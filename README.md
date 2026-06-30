Вот ваша курсовая работа, оформленная в формате Markdown для удобства чтения и дальнейшего редактирования.

---

# Курсовая работа

**По дисциплине:** «Прикладные информационные технологии»

**Тема:** «Разработка и контейнеризация веб-приложения для управления личной библиотекой с использованием Docker и автоматизация выпуска сертификатов Let's Encrypt»

**Автор:** Смородина А.А. (3 курс, очная форма)
**Руководитель:** Аксютин П.А., старший преподаватель кафедры ИТЭО
**Вуз:** РГПУ им. А. И. Герцена
**Год:** 2026

---

## Оглавление

1. [Введение](https://www.google.com/search?q=%23%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5)
2. [Теоретическая часть](https://www.google.com/search?q=%23%D1%82%D0%B5%D0%BE%D1%80%D0%B5%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F-%D1%87%D0%B0%D1%81%D1%82%D1%8C)
3. [Программная реализация TaskTracker Pro](https://www.google.com/search?q=%23%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%B0%D1%8F-%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F-bookshelf-manager)
4. [Результат работы](https://www.google.com/search?q=%23%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B)
5. [Приложение А. Исходный код](https://www.google.com/search?q=%23%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B0-%D0%B8%D1%81%D1%85%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%B4)

---

## 1. Введение

### 1.1 Актуальность темы исследования

В условиях цифровизации личных коллекций управление домашней библиотекой требует инструментов, обеспечивающих доступность и структурированность данных. Приложение «BookShelf Manager» требует современных подходов к инфраструктуре. Использование контейнеризации и автоматизация SSL-сертификатов Let's Encrypt позволяют создать защищенное и надежное веб-решение.

### 1.2 Цель и задачи исследования

**Цель:** разработать веб-приложение «BookShelf Manager», реализовать его контейнеризацию, настроить NGINX и автоматизировать процесс выпуска SSL-сертификатов.

**Задачи:**

* Разработать API на Python (Flask) для учета книг.
* Реализовать интерфейс для добавления, отображения и удаления книг.
* Подготовить конфигурации `Dockerfile` и `docker-compose.yml`.
* Настроить NGINX в качестве reverse-proxy.
* Автоматизировать HTTPS через Let's Encrypt.
* Провести тестирование системы.

### 1.3 Объект и предмет исследования

* **Объект:** процесс разработки и развертывания веб-приложений.
* **Предмет:** технологии контейнеризации (Docker, Docker Compose), reverse-proxy сервер NGINX и методы автоматизации HTTPS (Let’s Encrypt, ACME Companion).

### 1.4 Методы исследования

1. Метод разработки RESTful API.
2. Метод контейнеризации и оркестрации сервисов.
3. Метод настройки reverse-proxy для обеспечения безопасности.
4. Метод функционального тестирования.

### 1.5 Практическая значимость

Создание функционального веб-приложения «BookShelf Manager», готового к эксплуатации в защищенной среде HTTPS. Разработанная архитектура может выступать шаблоном для быстрого развертывания аналогичных веб-сервисов.

---

## 2. Теоретическая часть

### 2.1 Контейнеризация и платформа Docker

Контейнеризация — технология изоляции ПО, позволяющая упаковать приложение со всеми зависимостями в единый образ. Docker обеспечивает идентичность среды разработки и продакшена.

### 2.2 Оркестрация с помощью Docker Compose

Docker Compose — инструмент для управления многоконтейнерными приложениями через декларативный `YAML`-файл, позволяющий запускать всю экосистему одной командой.

### 2.3 Веб-сервер NGINX как Reverse-Proxy

NGINX принимает входящие соединения, проксирует их к контейнерам и обеспечивает безопасность, скрывая внутреннюю архитектуру сети.

### 2.4 Безопасность HTTPS и автоматизация Let’s Encrypt

Для защиты трафика используются центр сертификации Let’s Encrypt и утилита ACME Companion, обеспечивающие автоматическое продление сертификатов.

### 2.5 Выбор технологического стека

* **Бэкенд:** Flask (Python).
* **База данных:** SQLite (легковесность, отсутствие необходимости в отдельном контейнере).

---

## 3. Программная реализация BookShelf Manager

### 3.1 Архитектура системы

Система состоит из двух основных компонентов, работающих в Docker:

1. `nginx-proxy` (с контейнером `acme-companion` для HTTPS).
2. `bookshelf_app` (веб-приложение на Flask).

### 3.2-3.5 Реализация

Приложение использует `python:3.9-slim`. Конфигурация Nginx автоматически настраивается через переменные окружения `VIRTUAL_HOST` и `VIRTUAL_PORT`. Данные хранятся в томе (`volume`), что обеспечивает их сохранность при перезапуске контейнеров.

---

## 4. Результат работы

### 4.2 Интерфейс приложения

*(Здесь подразумевается вставка скриншота интерфейса)*

### 4.2 Документация по запуску

1. Настройте DNS-запись домена (A-запись) на IP вашего сервера.
2. Установите Docker и Docker Compose.
3. Разместите файлы проекта в рабочей директории.
4. Запустите: `docker compose up -d --build`.
5. Приложение доступно по адресу `https://assmi.duckdns.org`.

---

## Приложение А. Исходный код

### А.1 Файл `docker-compose.yml`

```yaml
services:
  nginx-proxy:
    image: nginxproxy/nginx-proxy
    container_name: nginx-proxy
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - /var/run/docker.sock:/tmp/docker.sock:ro
      - certs:/etc/nginx/certs:ro
      - vhost.d:/etc/nginx/vhost.d
      - html:/usr/share/nginx/html
    networks:
      - webnet

  acme-companion:
    image: nginxproxy/acme-companion
    container_name: acme-companion
    volumes_from:
      - nginx-proxy
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - acme:/etc/acme.sh
    networks:
      - webnet

  app:
    build: .
    container_name: bookshelf_app
    environment:
      - VIRTUAL_HOST=assmi.duckdns.org
      - VIRTUAL_PORT=5000
      - LETSENCRYPT_HOST=assmi.duckdns.org
      - LETSENCRYPT_EMAIL=ls481693@gmail.com
    volumes:
      - ./data:/app/data
    networks:
      - webnet

networks:
  webnet:
volumes:
  certs:
  vhost.d:
  html:
  acme:

```

### А.2 Файл `Dockerfile`

```dockerfile
FROM python:3.9-slim
WORKDIR /app
RUN pip install flask
COPY . .
CMD ["python", "app.py"]

```

### А.3 Файл `app.py`

```python
from flask import Flask, request, render_template_string
import sqlite3
import os

app = Flask(__name__)
DB_PATH = 'data/library.db'

def init_db():
    if not os.path.exists('data'): os.makedirs('data')
    conn = sqlite3.connect(DB_PATH)
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
    """
    return render_template_string(html, books=books)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)

```

---

*Подскажите, требуется ли вам какая-либо помощь с детализацией теоретических разделов или настройкой конфигурационных файлов?*
