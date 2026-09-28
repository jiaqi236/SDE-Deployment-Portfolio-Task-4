from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Get current time to make the app dynamic
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', current_time=now)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)