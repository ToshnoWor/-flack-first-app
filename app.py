from flask import Flask, render_template, jsonify

app = Flask(__name__)

VAR = [{
  'id': 0,
  'catName': 'cat1',
  'name': 'Alex',
  'problem': ''
}, {
  'id': 1,
  'catName': 'cat2',
  'name': 'Jonne',
  'problem': ''
}]


@app.route("/")
def hello_world():
  return render_template('home.html', var=VAR)


@app.route("/api/names")
def list_name():
  return jsonify(VAR)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
