from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)
app.static_folder = 'static'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_time')
def get_time():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify(current_time)

if __name__ == '__main__':
    app.run(debug=True)
