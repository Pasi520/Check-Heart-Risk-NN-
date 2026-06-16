from flask import Flask,render_template 

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('patient_details.html')

@app.route('/pa')
def pa():
    return"page1"


      
app.run(debug=True)