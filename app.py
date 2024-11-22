from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with a form for inputting two numbers
HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <title>Sum Calculator</title>
</head>
<body>
    <h1>Sum Calculator</h1>
    <form method="POST" action="/">
        <label for="num1">Number 1:</label>
        <input type="text" id="num1" name="num1" required>
        <br><br>
        <label for="num2">Number 2:</label>
        <input type="text" id="num2" name="num2" required>
        <br><br>
        <button type="submit">Calculate Sum</button>
    </form>
    {% if result is not none %}
        <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            # Get numbers from the form
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            # Calculate the sum
            result = num1 + num2
        except ValueError:
            result = "Invalid input. Please enter valid numbers."
    
    # Render the HTML with the result (if any)
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
