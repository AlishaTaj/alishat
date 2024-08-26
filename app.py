from flask import Flask, request, render_template
from sklearn import linear_model

app = Flask(__name__)

# Initialize the linear regression model
height = [[4.0], [5.0], [6.0], [7.0], [8.0], [9.0], [10.0]]
weight = [8, 10, 12, 14, 16, 18, 20]

reg = linear_model.LinearRegression()
reg.fit(height, weight)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    error = None
    if request.method == 'POST':
        try:
            user_height = float(request.form['height'])
            prediction = reg.predict([[user_height]])[0]
        except ValueError:
            error = "Invalid input. Please enter a valid number."
    return render_template('index.html', prediction=prediction, height=user_height if prediction else None, error=error)

if __name__ == '__main__':
    app.run(debug=True)
