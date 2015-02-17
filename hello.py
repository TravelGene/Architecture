from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index.html')
def home_page():
    return render_template('index.html')

@app.route('/CreateTrip.html')
def create_trip():
	return render_template('CreateTrip.html')

@app.route('/Activities.html')
def activities():
	return render_template('Activities.html')

@app.route('/trip_detail_main.html')
def tripdetail():
	return render_template('trip_detail_main.html')

@app.route('/profilec.html')
def profiles():
	return render_template('profilec.html')

@app.route('/friendlist.html')
def friendlist():
    return render_template('friendlist.html')

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/calendar.html')
def calendar():
    return render_template('calendar.html')

if __name__ == '__main__':
  app.run(debug=True)

