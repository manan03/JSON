from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        json_string = request.form['json_string']
        # Process the JSON string as needed
        # ...
        return render_template('result.html', result=json_string)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)