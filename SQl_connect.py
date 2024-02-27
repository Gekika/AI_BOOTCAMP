# To enable connection to a Database
import psycopg2
import pandas as pd

conn = psycopg2.connect(database = 'bike_store',
                        user="postgres",
                        host="localhost",
                        password="postgres",
                        port="5432" 
                        )
# we create a cusor to enable database operations(eg Select , Insert )
cur= conn.cursor()
# command to execute a query
cur.execute("SELECT * FROM production.brands")

rows = cur.fetchall()

# cur.close()
# conn.close()

for row in rows:
    print(row)
    
    

# convert the rows to a pandas Dataframe
column_names = [desc[0] for desc in cur.description]
df = pd.DataFrame(rows, columns=column_names)

print(df)    
