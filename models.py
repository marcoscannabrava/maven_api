import json
from dateutil.parser import isoparse


# Models
class User():
    def save(self):
        with open('users_db', mode='w') as f:
            f.write(json.dumps(self.users))
    
    def load(self):
        with open('users_db', mode='r') as f:
            db = json.loads(f.read())
            self.users = db if db != '' else {}

    def get_appointments(self, uid):
        self.load()
        if uid in self.users:
            return self.users[uid], None
        return 'error', 'User doesn\'t exist'

    def create(self, uid):
        self.load()
        if uid not in self.users.keys():
            self.users[uid] = []
            self.save()
            return True, None
        return False, 'User already exists.'

    def check_schedule(self, uid, time):
        appointments, error = self.get_appointments(uid)
        if error:
            return False, error
        for booked in appointments:
            if time == isoparse(booked):
                return False, 'User already booked an appointment at this time'
        return True, None

    def book_appointment(self, uid, time):
        appointments, error = self.get_appointments(uid)
        if error:
            return False, error
        self.users[uid].append(time.isoformat())
        self.save()
        return True, None

user = User()
