from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from database import load_jobs_from_db, load_job_from_db, add_application_to_db, create_user_to_db, login_user_to_db, user_exist_in_db, email_exist_in_db
import os

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = os.urandom(24)

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

# validate that the email and username is not already taken.
   if (user_exist_in_db(data['username'])):
      return redirect(url_for('registration_to_job'))
   
   if (email_exist_in_db(data['email'])):
      return redirect(url_for('registration_to_job'))


   create_user_to_db(data)
   return redirect (url_for('success'))

@app.route('/success')
def success():
   return render_template('success.html')

@app.route('/login', methods=['get'])
def login_to_job():
   error = request.args.get('err')

    
   return render_template('login.html', error = error)

@app.route('/user_auth', methods=['post'])
def user_auth():
   data = request.form

   # check if email is provided
   if ('username' not in data or data['username'] == ''):
      return redirect(url_for('login_to_job', err = 'username'))

   # check if password if provided
   if ('password' not in data or data['password'] == ''):
      return redirect(url_for('login_to_job', err = 'password'))

   user = login_user_to_db(data)

   if (user == None):
      return redirect(url_for('login_to_job', err = 'login'))

   # Session -- It is used to store the currently logged in user on a browser.
   
    
   # Read on MD5 for password hashing


   return redirect(url_for('logon'))



@app.route('/logon')
def logon():
   return render_template('logon.html')





if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)