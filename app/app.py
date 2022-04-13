from flask import Flask, render_template
app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bigfoot_files.html')
def bigfoot():
    return render_template('bigfoot_files.html')

@app.route('/ghost_files.html')
def ghost():
    return render_template('ghost_files.html')

@app.route('/ufo_files.html')
def ufo():
    return render_template('ufo_files.html')

@app.route('/index.html')
def back_home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()