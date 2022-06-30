from application import db

class Treats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cake_name = db.Column(db.String(60))
    milk_name = db.Column(db.String(30))
    toothache = db.Column(db.String(2))
    def __str__(self):
        return f"{self.cake_name} and {self.milk_name} have toothache rating of {self.toothache} out of 20 ૮₍´｡ᵔ ꈊ ᵔ｡`₎ა"