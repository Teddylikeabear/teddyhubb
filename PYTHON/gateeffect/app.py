from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/open_gate')
def open_gate():
    time.sleep(1)  # Simulate gate opening
    return render_template('open_gate.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
