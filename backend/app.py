from flask import Flask, jsonify
from flask_cors import CORS          # 👈 add this
import psycopg2
import os

app = Flask(__name__)
CORS(app)                            # 👈 add this

def get_db():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("DB_NAME", "helloworld"),
        user=os.environ.get("DB_USER", "postgres"),
        password=os.environ.get("DB_PASS", "postgres")
    )

@app.route('/message')
def message():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT text FROM messages LIMIT 1;")
        row = cur.fetchone()
        return jsonify({"message": row[0] if row else "Hello from DB!"})
    except Exception as e:
        return jsonify({"message": f"DB error: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)