from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html')

@app.route("/your-url",methods=['GET','POST'])
def your_url():
	if request.method== 'POST':
		return render_template('your_url.html',code=request.form['code']) #if it is post request then request.form['--']
																		  #else request.args['']'''
	else:
		return "This is not valid"


if __name__=="__main__":
	app.run(debug=True)