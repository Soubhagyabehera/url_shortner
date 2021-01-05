from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
	return "Hello Flask!"

@app.route("/about")
def about():
	return "With url_shortner can shorten the link you provide"


if __name__=="__main__":
	app.run(debug=True)