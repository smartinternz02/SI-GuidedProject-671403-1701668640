from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/inner-page')
def inner_page():
    return render_template("inner-page.html")

@app.route('/output')
def output():
    return render_template("output.html")

if __name__ == '__main__':
    app.run(debug=True)
