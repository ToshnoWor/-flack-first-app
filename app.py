from flask import Flask, render_template, jsonify
import datetime
import phonenumbers as tel

app = Flask(__name__)

VAR = [{
  'id': 0,
  'pi': {
    'fullname':
    'Коваль Олексій Олександрович',
    'birthday':
    datetime.date(1995, 9, 9),
    'residence':
    'Вул. Миру 99, кв. 99, під\'їзд 2.',
    'phone':
    tel.format_number(tel.parse('+380958403255'), tel.PhoneNumberFormat.E164),
    'placeofwork':
    'From home',
    'complaint': {
      'Біль': True,
      'Скованість': True,
      'Обмеження рухів': False,
      'Температура': True,
      'Слабкість': False,
      'Сип': False,
      'Лімфо вузли': False,
      'Інше': False
    }
  }
}, {
  'id': 1,
  'pi': {
    'fullname':
    'Ім\'я Призвище Побатькові',
    'birthday':
    datetime.date(1996, 6, 6),
    'residence':
    'Вул. Шевченка 66, кв. 66, під\'їзд 2.',
    'phone':
    tel.format_number(tel.parse('+380951203255'), tel.PhoneNumberFormat.E164),
    'placeofwork':
    'Інше місце.',
    'complaint': {
      'Біль': True,
      'Скованість': False,
      'Обмеження рухів': False,
      'Температура': True,
      'Слабкість': True,
      'Сип': False,
      'Лімфо вузли': False,
      'Інше': False
    }
  }
}]


@app.route("/")
def hello_world():
  return render_template('home.html', var=VAR)


@app.route("/api/names")
def list_name():
  return jsonify(VAR)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
