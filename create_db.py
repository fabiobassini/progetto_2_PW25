import pymysql
import os
import sys
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "distribuzione_acqua")


def create_database():
    print(f"Tentativo di connessione a MySQL su {DB_HOST}...")

    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        cursor = conn.cursor()

        print(f"Creazione database '{DB_NAME}' in corso...")
        sql = f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
        cursor.execute(sql)

        print(f"✅ Successo! Il database '{DB_NAME}' è pronto.")

        cursor.close()
        conn.close()

    except pymysql.MySQLError as e:
        code = e.args[0]
        if code == 1045:
            print("\n❌ ERRORE: Accesso negato (Password errata).")
        elif code == 2003:
            print("\n❌ ERRORE: Impossibile connettersi al server MySQL (è avviato?).")
        else:
            print(f"\n❌ ERRORE MySQL: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ ERRORE Generico: {e}")
        sys.exit(1)


if __name__ == "__main__":
    create_database()
