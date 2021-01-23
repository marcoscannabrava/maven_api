from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask import request

from .models import user
from .helpers import round_time


app = Flask(__name__)


@app.route('/appointments/create', methods=['POST'])
def create_appointment():
    """ Input: {"user": <string:user_id>, "time": <str:utc_datetime_isostring>}
        Output: {"status": "success" | "failure"}
    """
    body = request.get_json()
    if 'time' in body and 'user' in body:
        try:
            time = round_time(body['time'])
        except ValueError:
            return {'status': 'failure', 'message': "Time format is not ISO 8601: 'YYYT-MM-DD hh:mm:ss'"}

        booked = False
        available, msg = user.check_schedule(body['user'], time)
        if available:
            booked, msg = user.book_appointment(body['user'], time)
        return {'status': 'success'} if booked else {'status': 'failure', 'message': msg}

    return {'status': 'failure', 'message': 'Request missing appointment time or user id.'}


@app.route('/users/<string:user_id>/appointments', methods=['GET'])
def get_appointments(user_id):
    """ Input: user id in url
        Output: {"status": "success" | "failure", "appointments": isoformatted_times_list[]}
    """
    appointments, msg = user.get_appointments(user_id)
    if appointments == 'error':
        return {'status': 'failure', 'message': msg}
    return {'status': 'success', 'appointments': appointments}


@app.route('/users/create', methods=['POST'])
def create_user():
    """ Input: {"user": <string:user_id>}
        Output: {"status": "success" | "failure"}
    """
    body = request.get_json()
    if 'user' in body:
        success, msg = user.create(body['user'])
        if success:
            return {'status': 'success'}
        return {'status': 'failure', 'message': msg}
