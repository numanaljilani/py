from flask import Flask , render_template,request
import google.generativeai as genai



app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    data =''
    query=''
    if request.method == "POST":
        query = request.form['query']
        genai.configure(api_key='AIzaSyATJobjmnYy2OQkCE50GFiAD-0YO472b50')
        model = genai.GenerativeModel(model_name='gemini-1.5-flash')
        response = model.generate_content(query)
        data = response.text

    return render_template('index.html',data=data , query=query)
app.run(debug=True)