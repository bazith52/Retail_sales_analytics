import os, sqlite3, pandas as pd
path='output/retail_sales.db'
exists=os.path.exists(path)
size=os.path.getsize(path) if exists else None
info={'exists':exists,'size':size,'cwd':os.getcwd()}
if exists:
    try:
        conn=sqlite3.connect(path)
        tables=pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)
        conn.close()
        info['tables']=tables['name'].tolist()
    except Exception as e:
        info['error']=str(e)
info