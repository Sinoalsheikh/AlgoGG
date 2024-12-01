from flask import Flask, render_template
from full_web_app import FullWebApp

app = Flask(__name__)
web_app = FullWebApp()

@app.route('/')
def index():
    return render_template('index.html', suites=web_app.suites)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
