from flask import Flask, render_template, jsonify, request, redirect, url_for
from database import load_jobs_from_db, load_job_from_db, add_application_to_db, create_user_to_db

app = Flask(__name__)

@app.route("/")
def cs_careers():
  jobs = load_jobs_from_db()
  return render_template("index.html",jobs=jobs)

@app.route("/api/jobs")

def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
   job = load_job_from_db(id)

   if not job:
      return "Oops! Can't find what you are looking for!", 404
   
   return render_template('jobpage.html', job=job)

@app.route("/api/job/<id>")
def show_job_json(id):
   job= load_job_from_db(id)
   return jsonify(job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
   data= request.form
   job = load_job_from_db(id)
   add_application_to_db(id, data)
   return render_template('app_submitted.html',application=data, job=job)

@app.route("/register")
def registration_to_job():
   return render_template('registration.html')

@app.route("/create_user", methods=['post'])
def create_user():
   data = request.form
   create_user_to_db(data)
   return redirect (url_for('success'))

@app.route('/success')
def success():
   return 'logged in successfully'




if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)