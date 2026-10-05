from flask import Flask , render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])

def home():
    message = ''
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = f'Thank you {name}, we have received your email: {email}.'
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)