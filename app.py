from flask import Flask, render_template, jsonify, request
from sqlalchemy import text
from database import add_application_to_db, engine, load_projects_from_db, load_project_from_db

app = Flask(__name__) # python app.py -> __name__ = __main__

@app.route("/") # route (url)
def hello_world():
  projects_db = load_projects_from_db()
  return render_template('home.html', projects=projects_db)

@app.route("/api/projects")
def list_projects():
  return jsonify(load_projects_from_db())

@app.route("/project/<id>")
def show_project(id):
  project_db = load_project_from_db(id)

  if not project_db:
    return "Not Found", 404
  return render_template('project.html', project=project_db)

@app.route("/project/<id>/apply", methods=['post'])
def apply_to_project(id):
  data = request.form # url -> request.args
  project_db = load_project_from_db(id)
  # store this in the DB
  add_application_to_db(id, data)
  # send an email
  # display an acknowledgement
  return render_template('application_submitted.html', 
                         application=data,
                         project = project_db)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)