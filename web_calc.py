from flask import Flask, request
app = Flask(__name__)

html_form_with_message = '''
<!DOCTYPE html>
<html>
<head>
<title>Text Echo App</title>
</head>
<body>
    <h2>Enter Number</h2>
    <form method="post" action="/">
        <label for="text">Number:</label><br>
        <input type="number" name="my_input_value"><br><br>
        <input type="submit" value="My Button">
    </form>
    <p>put_data_here</p>
</body>
</html>
'''

def my_calculation(value):
    return value * value

@app.route('/', methods=['GET', 'POST'])
def home():
    user_input = ''
    calculated_value = 0
    if request.method == 'POST':
        user_input = request.form['my_input_value']
        calculated_value = my_calculation( int(user_input) )

    display_text = "Input " + user_input + " squared is " + str(calculated_value)
    return html_form_with_message.replace("put_data_here", display_text)

app.run()