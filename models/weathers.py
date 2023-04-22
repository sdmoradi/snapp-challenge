from app import db
class Weathers(db.Model):
    id = db.Column('request_id', db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    temperature = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    time = db.Column(db.String(50))

    def __init__(self, city, temperature, humidity, time):
        self.city = city
        self.temperature = temperature
        self.humidity = humidity
        self.time = time
    def create(self):
        db.create_all()
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()
