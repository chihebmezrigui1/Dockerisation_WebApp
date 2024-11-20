from flask import Flask, jsonify, render_template
import os
import mysql.connector

app = Flask(__name__)

# Connexion à la base de données
def get_db_connection():
    conn = mysql.connector.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME')
    )
    return conn

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/data')
def data():
    # Connexion à la base de données
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    # Exécution de la requête
    cursor.execute("SELECT * FROM test_table")
    result = cursor.fetchall()
    
    connection.close()
    
    # Rendre la page HTML avec les données
    return render_template('data.html', rows=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4743)
