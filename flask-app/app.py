from flask import Flask, render_template
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/schools')
def display_schools():
    return render_template('schools.html')

@app.route('/prices')
def send_report():
    return render_template('prices.html')

@app.route('/prices-area')
def prices_area():
    return render_template('price-per-area.html')

@app.route('/prices-appreciation')
def prices_appreciation():
    return render_template('price-appreciation.html')

@app.route('/days-listed')
def days_listed():
    return render_template('days-listed.html')

@app.route('/crime')
def crime():
    return render_template('crime.html')

@app.route('/old')
def old_index():
	return render_template('old-index.html')

@app.route('/old/schools')
def old_schools():
	return render_template('old-schools.html')

@app.route('/old/prices')
def old_prices():
    return render_template('old-prices.html')

@app.route('/old/prices-area')
def old_prices_area():
    return render_template('old-price-per-area.html')

@app.route('/old/prices-appreciation')
def old_prices_appreciation():
    return render_template('old-price-appreciation.html')

@app.route('/old/market-statistics')
def old_market_statistics():
    return render_template('old-market-statistics.html')