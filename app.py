from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Sound Engineer',
    'location': 'Lagos, Nigeria',
    'salary': '#500,000.00'
  },
  {
    'id': 2,
    'title': 'Talent Manager',
    'location': 'Lagos, Nigeria',
    'salary': '#500,000.00'

  },
  {
    'id': 3,
    'title': 'Data Analyst',
    'location': 'Remote',
    'salary': '$50,000.00'
  }
]
@app.route("/")
def hello_world():
  return render_template("index.html",jobs=JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)