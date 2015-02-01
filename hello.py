from flask import Flask, render_template, request
from pymongo import Connection

database = Connection()["ab2015"]


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		if request.form['name'] == "" or request.form['message'] == "":
			return "please fill blanks"
		else:
			database.message.insert({"name": request.form['name'], "message": request.form['message']})
	
	messages = database.message.find()
	return render_template('hello.html', messages=messages)
	
if __name__ == "__main__":
    app.run(port=8001, debug=True)
