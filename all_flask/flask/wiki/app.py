from flask import Flask , render_template , request
import wikipedia

app = Flask(__name__)

@app.route('/')
def home():
    print(request)
    return render_template('index.html')

@app.route('/wiki',methods = ['GET','POST'])
def wiki():
    if request.method == 'POST':
        query = request.form['query']
        try:
            result = wikipedia.summary(query, sentences=10)
            return render_template('index.html' , result = result  , query = query)
        except:
            return render_template('index.html' , result = f"{query} Not found"  , query = query)


app.run(debug=True)

# weather and news