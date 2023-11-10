from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROJECTS = [
  {
    'id': 1,
    'language': 'C/C++',
    'description': 'Algorithm & Programming',
    'topic': 'Searching, Sorting, Data Structure'
  },
  {
    'id': 2,
    'language': 'Java',
    'description': 'Android & Smartphone Application Development',
    'topic': '공공데이터포털(Open API), GPS'
  },
  {
    'id': 3,
    'language': 'Python',
    'description': 'Machine Learning & Data Science',
  },
  {
    'id': 4,
    'language': 'C#',
    'description': 'Unity & Game Development',
    'topic': 'Muscle Synergy, EMG Data Report'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', projects=PROJECTS, Author_name="DW")

@app.route("/api/projects")
def list_projects():
  return jsonify(PROJECTS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)