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

<<<<<<< Updated upstream
=======
@app.route('/search')
def search():
    query = request.args.get('q', '').strip()
    if not query:
        flash('Please enter a food name to search.', 'error')
        return redirect(url_for('index'))

    food_attributes = read_food_attributes(query)
    if food_attributes:
        return redirect(url_for('food_attributes', food=query))
    else:
        # Directly render the error page from here if no food found
        return render_template('error.html', error_message=f"No results found for '{query}'")


>>>>>>> Stashed changes
@app.route('/<food>')
def food_attributes(food):
    # Reading attributes for the specified food
    food_attributes = read_food_attributes(food)
    
    if food_attributes:
        return render_template('food.html', food=food_attributes)
    else:
<<<<<<< Updated upstream
        return "Food not found!", 404
=======
        return render_template('error.html', error_message=f"Food not found: {food}")


@app.errorhandler(404)
def page_not_found(e):
    # Note, we set 404 status explicitly
    return render_template('error.html', error_message="404: Page not found!"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error_message="500: Internal Server Error!"), 500
>>>>>>> Stashed changes

if __name__ == '__main__':
    app.run(debug=True)
