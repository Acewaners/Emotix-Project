from flask import Flask, jsonify
from models.db_connect import get_connection  #Memanggil fungsi koneksi

app = Flask(__name__)

# Route HOME
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Emotix Backend!"})

# Route Users
@app.route('/users')
def get_users():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT id_user, nama, email, role FROM User")
    users = cursor.fetchall()
    db.close()

# Olah data ke json
    result = []
    for u in users:
        result.append({
            'id_user': u[0],
            'nama': u[1],
            'email': u[2],
            'role': u[3]
        })
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)