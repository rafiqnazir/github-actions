from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
	date = datetime.now()
	return str(date)

def test_function():
	return "Hello, World"

if __name__ == "__main__":
	app.run()