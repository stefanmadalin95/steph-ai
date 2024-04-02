from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Retrieving the text input from the form by using the input's name attribute
        user_input = request.form['userInput']
        
        return f'You entered: {user_input}'
    return render_template('input_form.html')

@app.route('/admin')
def admin():
    return redirect(url_for('form'))

if __name__ == "__main__":
    app.run(debug=True)