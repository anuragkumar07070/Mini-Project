import mysql.connector
from flask import Flask, render_template
import mysql.connector

def get_food_data(food_id):
    food = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Anu@0718',
            database='Nutrients'
        )
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM foods WHERE id = %s"
            cursor.execute(query, (food_id,))
            food = cursor.fetchone()

    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            
    return food


app = Flask(__name__)

def get_food_data(food_id):
    # Function to retrieve food data from MySQL database
    # Implement this function as shown in the previous response

@app.route('/food/<int:food_id>')
def food_page(food_id):
    # Retrieve food data based on the food ID
    food_data = get_food_data(food_id)
    if food_data:
        # Render the food.html template with the food data
        return render_template('food.html', food=food_data)
    else:
        # Return a 404 error page if food data not found
        return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)



      