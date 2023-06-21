from flask import Flask, render_template, jsonify

app = Flask(__name__)

VAR = [{'id': 0, 'name': 'Alex'}, {'id': 1, 'name': 'Jonne'}]


@app.route("/")
def hello_world():
  return render_template('home.html', var=VAR)


@app.route("/api/names")
def list_name():
  return jsonify(VAR)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
