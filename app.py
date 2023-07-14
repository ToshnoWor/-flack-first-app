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

VAR2 = [{
  'lesson':
  '1',
  'tasks': [{
    'id':
    1,
    'task':
    'Look at the pictures of Helen and use the prompts to write sentences. Use the correct form of hte present simple.',
    'quest_type':
    '',
    'quest': [{
      'num': 1,
      'text': 'Every day, Helen gets up at half past seven.'
    }, {
      'num': 2,
      'text': ''
    }, {
      'num': 3,
      'text': ''
    }, {
      'num': 4,
      'text': ''
    }, {
      'num': 5,
      'text': ''
    }, {
      'num': 6,
      'text': ''
    }],
    'image_path':
    'https://-flack-first-app.alekseikoval.repl.co/static/Screenshot_1.png'
  }, {
    'id':
    2,
    'task':
    'Complete using the correct present countinuous form of the verbs in brackets. You may have to some negative forms.',
    'quest_type':
    '',
    'quest': [{
      'num': 1,
      'text': 'Gordon? I think he _____(write) a letter at the moment.'
    }, {
      'num': 2,
      'text': 'Yes, the match is on TV now, but we ____(lose).'
    }, {
      'num':
      3,
      'text':
      'Right now, Margaret ____(have) a shower. Do you want to ring later?'
    }, {
      'num': 4,
      'text': 'Sally ____(stay) with her aunt for a few days.'
    }, {
      'num':
      5,
      'text':
      'I ___(lie)! It\'s true! I did see Madonna at the supermarket.'
    }, {
      'num': 6,
      'text': 'Josh ____(always/use) my bike! It\'s so annoying.'
    }, {
      'num':
      7,
      'text':
      'We ____(have) lunch, but I can come round and help you later.'
    }, {
      'num': 8,
      'text': '____(you/play) music up there? It\'s really noisy!'
    }],
    'image_path':
    None
  }]
}]


@app.route("/")
def hello_world():
  return render_template('home.html', var=VAR, var2=VAR2)


@app.route("/api/names")
def list_name():
  return jsonify(VAR)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
