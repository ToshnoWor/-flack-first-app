from flask import Flask, render_template, jsonify
from database import load_person_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  persons = load_person_from_db()
  return render_template('home.html', persons=persons)


@app.route("/api/persons")
def list_name():
  persons = load_person_from_db()
  return jsonify(persons)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
