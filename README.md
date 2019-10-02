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

- `GET` */hello/\<name>* - returns a custom hello message
- `GET` */json/* - returns a dict using `json.dumps`
- `GET` */jsonify/* - returns a dict using `flask.jsonify`
- `GET` */return?\<key>=\<value>* - returns the `value` content
- `GET` */users/* - returns a list of users
- `GET` */users/\<id>* - returns a specific user

- `POST` */users/* - saves the user according to the given parameters
    - Parameters: *username*: str, *email*: str, *is_active*: bool

- `PUT` */user/\<id>* - edits a user data

- `DELETE` */user/\<id>* - removes the user from database
