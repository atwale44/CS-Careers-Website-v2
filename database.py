from sqlalchemy import create_engine, text
import env

db_connection_string = env.database['connection_string']

engine = create_engine(db_connection_string,
connect_args = {
"ssl":{
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
