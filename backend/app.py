from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Usuario registrado exitosamente!"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        return jsonify({"message": "Hola desde el backend!"}), 200
    return jsonify({"message": "Credenciales incorrectas!"}), 401

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear las tablas
    app.run(host='0.0.0.0', port=5000)
