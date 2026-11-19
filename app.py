from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(
            host="db",
            database="tareas",
            user="admin",
            password="admin123"
        )

        conn.close()

        return "Conexion exitosa con PostgreSQL"

    except Exception as e:
        return f"Error: {e}"

app.run(host="0.0.0.0")