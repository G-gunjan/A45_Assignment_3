from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if not age.isdigit():
            error = "Please enter a valid age."
            return render_template('greet.html', error=error)
        return f"Hello, {name}! You are {age} years old."
    return render_template('greet.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
