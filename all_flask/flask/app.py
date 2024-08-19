from flask import Flask , render_template
import datetime
import wikipedia


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return '<h1><center>About Page</center></h1>'

@app.route('/wiki/<query>')
def wiki(query):
    data = wikipedia.summary(query , sentences = 10)
    return f'<h1><center> User Query : {query} </center></h1>
<p><center>{data}</center></p>'

@app.route('/contact')
def contact():
    return '<h1><center>contact Page</center></h1>'

@app.route('/welcome/<name>')
def welcome(name):
    houre = datetime.datetime.now().hour#only date
    if(houre >=5 and houre <12):
        greet = "Good Mornig ..."
    elif(houre >= 12 and houre < 18):
        greet ="Good Afternon ..."
    elif(houre >= 18 and houre < 24 ):
        greet ="Good Evening ..."
    else:
        greet ="Good night ..."
    
    return f'<h1 style="background-color: purple; color:white;"><center>{greet} {name}</center></h1>' 

@app.route('/time')
def time():
    return f'<h1 style="background-color: purple; color:white;"><center> {datetime.datetime.now().strftime("%H:%M:%S ")}</center></h1>' 

@app.route('/date')
def date():
    return f'<h1 style="background-color: purple; color:white;"><center> {datetime.datetime.now().strftime("%d/%m/%y")}</center></h1>' 


app.run(debug=True)