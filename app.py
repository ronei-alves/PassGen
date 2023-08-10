from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_password', methods=['GET', 'POST'])
def generate_password():
    if request.method == 'POST':
        length = int(request.form['length'])
        include_uppercase = request.form.get('uppercase')
        include_numbers = request.form.get('numbers')
        include_special = request.form.get('special')

        characters = string.ascii_letters
        if include_numbers:
            characters += string.digits
        if include_special:
            characters += string.punctuation

        generated_password = ''.join(random.choice(characters) for _ in range(length))
        return render_template('generate_password.html', generated_password=generated_password)

    return render_template('generate_password.html', generated_password=None)


if __name__ == '__main__':
    app.run(debug=True)

