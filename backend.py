from flask import Flask, render_template
import csv

app = Flask(__name__)

# Function to read food attributes from CSV file
def read_food_attributes(food_name):
    with open('dataset.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['name'].lower() == food_name.lower():
                return {
                    'Food': row['name'],
                    'Protein': row['protein'],
                    'Carbohydrates': row['carbs'],
                    'Fat': row['fats'],
                    'Calories': row['calories']
                }
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<food>')
def food_attributes(food):
    # Reading attributes for the specified food
    food_attributes = read_food_attributes(food)
    
    if food_attributes:
        return render_template('food.html', food=food_attributes)
    else:
        return "Food not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
