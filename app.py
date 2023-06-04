from flask import Flask, render_template, jsonify

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
    'salary': '#575,000.00'

  },
  {
    'id': 3,
    'title': 'Data Analyst',
    'location': 'Remote',
    'salary': ''
  },
  {
    'id': 4,
    'title': 'Brand Manager',
    'location': 'San Fransisco, USA',
    'salary': '$145,000.00'

  }
]
@app.route("/")
def hello_world():
  return render_template("index.html",jobs=JOBS,
  company_name='Cruel Station' )

@app.route("/api/jobs")

def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)