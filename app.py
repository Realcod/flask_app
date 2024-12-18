from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])
def calculate():
    if request.method == 'POST':
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if ops == "add":
            res = num1 + num2
            result = "The sum of " + str(num1) + 'and ' + str(num2) + "is " + str(res)
        elif ops == "subtract":
            res = num1 - num2
        elif ops == "multiply":
            res = num1 * num2
        elif ops == "divide":
            res = num1 / num2 if num2 != 0 else "Division by zero error"
        else:
            res = "Invalid operation"

        return render_template('results.html' , result = res)

if __name__ == "__main__":
    app.run(debug=True)
 