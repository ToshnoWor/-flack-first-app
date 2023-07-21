import os
from sqlalchemy import create_engine, text


my_secret = os.environ['DB_CONNECTION_STRING']
db_connection_string = my_secret

connect_args = {"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}}

engine = create_engine(db_connection_string, connect_args=connect_args, echo=False)

def load_person_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from person"))
    persons = []
    for row in result.mappings():
      persons.append(dict(row))
    return persons