from flask import Flask, render_template, jsonify
from database import load_persons_from_db, load_person_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  persons = load_persons_from_db()
  return render_template('home.html', persons=persons)


@app.route("/api/persons")
def list_name():
  persons = load_persons_from_db()
  return jsonify(persons)


@app.route("/person/<id>")
def show_person(id):
  person = load_person_from_db(id)
  if not person:
    err_messame = "Not found person with id: " + id
    return render_template('404.html', message=err_messame), 404
  return render_template('personpage.html', person=person)
  # return jsonify(person)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
