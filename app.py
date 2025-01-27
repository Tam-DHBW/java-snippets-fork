from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

# Database configuration (can use environment variables)
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "exampledb")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")

# Connect to PostgreSQL
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        return None

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Flask API!"})

@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Could not connect to the database"}), 500

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users;")
        users = cursor.fetchall()
        cursor.close()
        conn.close()

        # Convert to JSON response
        user_list = [{"id": row[0], "name": row[1], "email": row[2]} for row in users]
        return jsonify(user_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Could not connect to the database"}), 500

    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;", (name, email))
        user_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "User created successfully", "id": user_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
