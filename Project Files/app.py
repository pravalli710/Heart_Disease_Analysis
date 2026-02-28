from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/starter')
def starter():
    return render_template('starter-page.html')

@app.route('/dashboard1')
def dashboard1():
    return render_template('dashboard1.html')

@app.route('/dashboard2')
def dashboard2():
    return render_template('dashboard2.html')

@app.route('/story')
def story():
    return render_template('story.html')

if __name__ == '__main__':
    app.run(debug=True, port=5003)