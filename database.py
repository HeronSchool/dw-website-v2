from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl" : {
      "ssl_ca" : "/etc/ssl/cert.pem"
    }
  }
)

# return data as dictionary
def load_projects_from_db():
  with engine.connect() as connection:
    result = connection.execute(text("select * from projects"))

    projects_dict = []
    for row in result.all():
      projects_dict.append(row._asdict())

    return projects_dict

    
# with engine.connect() as connection:
#   result = connection.execute(text("select * from projects"))

#   result_dict = []
#   for row in result.all():
#     result_dict.append(row._asdict())

#   print(result_dict)

  # print("type of result :", type(result))

  # result_all = result.all()
  # print("result_all :", result_all)
  # print("type of result_all", type(result_all))
  
  # first_result = result_all[0]
  # print("first_result :", first_result)
  # print("type of first_result :", type(first_result))
  
  # first_result_dict = first_result._mapping
  # print("first_result_dict :", first_result_dict)
  # print("type of first_result_dict :", type(first_result_dict))