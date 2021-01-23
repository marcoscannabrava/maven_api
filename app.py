from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/appointments/create', methods=['POST'])
def create_appointment():
    params = request.form
    return {'status': 'success', 'payload': params}

@app.route('/users/<int:user_id>/appointments', methods=['GET'])
def get_appointments(user_id):
    return f'Hello, {user_id}'