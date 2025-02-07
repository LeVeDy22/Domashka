from request_weather import get_data
from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return get_data()


if __name__ == "__main__":
    app.run(debug=True)
