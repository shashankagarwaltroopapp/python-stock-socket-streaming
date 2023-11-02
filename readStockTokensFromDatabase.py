import psycopg2
import os
from dotenv import load_dotenv

def readStockTokensFromDatabase():
    load_dotenv(override=True)
    try:
        conn = psycopg2.connect(
            host=os.environ["PGHOST"],
            database=os.environ["PGDATABASE"],
            user=os.environ["PGUSER"],
            password=os.environ["PGPASSWORD"])
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
    cur = conn.cursor()
    select_query = 'SELECT "token" FROM public."Stocks"'
    cur.execute(select_query)
    results = cur.fetchall()

    string_list = [t[0] for t in results]
    cur.close()

    return string_list

def main():
    print(readStockTokensFromDatabase())


if __name__ == "__main__":
    main()