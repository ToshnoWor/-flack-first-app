from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://2fa8r8jmwetare08k6fx:pscale_pw_2LnNhN0oJJXR5hXKJSfO512vt8TAIPA619vF85XXXAu@aws.connect.psdb.cloud/medapp?charset=utf8mb4"

connect_args = {"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}}

engine = create_engine(db_connection_string, connect_args=connect_args)

with engine.connect() as conn:
  result = conn.execute(text("select * from person"))
  print(type(result))
  result_all = result.all()
  print(type(result_all))
  print(result_all)
