from flask import Flask, render_template, jsonify

app = Flask(__name__) # python app.py -> __name__ = __main__

PROJECTS = [
  {
    'id': 1,
    'language': 'C/C++',
    'description': 'Algorithm & Programming',
    'topic': 'Searching, Sorting, Data Structure'
  }, 
  {
    'id': 2,
    'language': 'C#',
    'description': 'Unity & Android Application Development',
    'topic': '공공데이터포털(Open API), GPS, Google API'
  }, 
  {
    'id': 3,
    'language': 'Java',
    'description': 'Chat app & Android Application Development',
  }, 
  {
    'id': 4,
    'language': 'C#',
    'description': 'Healthcare Application Development',
    'topic': 'Muscle Synergy, EMG Data Report'
  },
  {
    'id' : 5,
    'language': 'Python'
  }
]


@app.route("/") # route (url)
def hello_world():
  return render_template('home.html', projects=PROJECTS, author_name="다원")


@app.route("/api/projects")
def list_projects():
  return jsonify(PROJECTS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
