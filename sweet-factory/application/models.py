from application import db

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cake_name = db.Column(db.String(60))
    milk_name = db.Column(db.String(60))
    result_ice = db.Column(db.String(60))
    def __str__(self):
        return f"{self.cake_name} and {self.milk_name} go well with {self.result_ice}"