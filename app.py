from flask import Flask, request, jsonify
from flask_login import LoginManager

from database import db
import models.user as User
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    if username and password:
        pass

    return jsonify({"message": "Credenciais inválidas"}), 400

@app.route("/hello-world", methods=['GET'])
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)