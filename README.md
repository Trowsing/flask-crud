# Simple Flask CRUD app

Minimal Flask app integrated with a simple SQLite3 database and a single *User* model using SQLAlchemy

## Running locally

Clone the repository:
```bash
git clone https://github.com/Trowsing/flask-crud.git
cd flask-crud
```

Create and execute virtual environment:
```bash
python3 -m venv env
source env/bin/activate
```

Install all requirements:
```bash
pip3 install -r requirements.txt
```

Export the Flask app name:
```bash
export FLASK_APP=home.py
```

Run the development server:
```bash
flask run
```

## Avalible endpoints

- */hello/\<name>* - returns a custom hello message
- */json/* - returns a dict using `json.dumps`
- */jsonify/* - returns a dict using `flask.jsonify`
- */return?\<key>=\<value>* - returns the `value` content
- */users/* - returns a list of users
- */users/\<id>* - returns a specific user