from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/demography')
def demography():
    return render_template('demography.html')

@app.route('/culinary_tourism')
def culinary_tourism():
    return render_template('culinary_tourism.html')

@app.route('/historical_tourism')
def historical_tourism():
    return render_template('historical_tourism.html')

@app.route('/natural_tourism')
def natural_tourism():
    return render_template('natural_tourism.html')

@app.route('/government')
def government():
    return render_template('government.html')

@app.route('/population_service')
def population_service():
    return render_template('population_service.html')

@app.route('/healthcare_service')
def healthcare_service():
    return render_template('healthcare_service.html')

@app.route('/education_service')
def education_service():
    return render_template('education_service.html')

if __name__ == '__main__':
    app.run(debug=True)