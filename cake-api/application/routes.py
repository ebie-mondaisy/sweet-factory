from application import app
import random

@app.route('/get_cake', methods=['GET'])
def cake():
    cake_name = ["Red Velvet", "Victoria Sponge", "Chocolate", "Confetti", "Bubblegum", "Lemon Drizzle"]
    cake = random.choice(cake_name)
    return cake
