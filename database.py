from sqlalchemy import create_engine, text
import env

db_connection_string = env.database['connection_string']

engine = create_engine(db_connection_string,
                       connect_args={
                           "ssl": {
                               'rejectUnauthorized': False,
                           }
                       })


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append({
                'id': row[0],
                'title': row[1],
                'location': row[2],
                'salary': row[3],
                'currency': row[4],
                'responsibilities': row[5],
                'requirements': row[6],
            })

        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {"val": id}
                              )
        rows = result.mappings().all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])


def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES(:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

        conn.execute(query, [{
            'job_id': job_id,
            'full_name': data['full_name'],
            'email': data['email'],
            'linkedin_url': data['linkedin_url'],
            'education': data['education'],
            'work_experience': data['work_experience'],
            'resume_url': data['resume_url']
        }])


def create_user_to_db(data):
    with engine.connect() as conn:
        query = text(
            "INSERT INTO accounts ( username, password, email) VALUES(:username, :password, :email)")

        conn.execute(query, [{
            'username': data['username'],
            'password': data['password'],
            'email': data['email']
        }])


def login_user_to_db(data):
    with engine.connect() as conn:

        result = conn.execute(text("SELECT * FROM  accounts WHERE username = :username and password = :password"), [{
            'username': data['username'],
            'password': data['password']
        }])
        rows = result.mappings().all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])


def user_exist_in_db(uname):
    with engine.connect() as conn:

        result = conn.execute(text("SELECT * FROM  accounts WHERE username = :username"), [{
            'username': uname
        }])
        rows = result.mappings().all()
        if len(rows) == 0:
            return False
        else:
            return True

def email_exist_in_db(ename):
    with engine.connect() as conn:

        result = conn.execute(text("SELECT * FROM  accounts WHERE email = :email"), [{
            'email': ename
        }])
        rows = result.mappings().all()
        if len(rows) == 0:
            return False
        else:
            return True