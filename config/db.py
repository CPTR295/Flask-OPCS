from __main__ import app 
import pyscopg2
import functools
import myconfig


def connect_db(func):
    @functools.wraps(func)
    def repo_function(*args,**kwargs):
        conn = pyscopg2.connect(
            host=myconfig.DB_HOST,
            database=myconfig.DB_NAME,
            user=myconfig.DB_USER,
            password=myconfig.DB_PASSWORD,
            port=myconfig.DB_PORT
        )
        resp = func(conn, *args, **kwargs)
        conn.commit()
        conn.close()
        return resp
    return repo_function


