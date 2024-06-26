from flask import Flask, render_template
from api.home import home_bp
import util.config as config

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(file_bp)
app.register_blueprint(user_bp)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=1, host="0.0.0.0", port="5000")

# docker run --rm -p 5000:5000 -v $(pwd):/app server.dockerfile
