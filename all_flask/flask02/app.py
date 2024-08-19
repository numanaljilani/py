from flask import Flask , render_template,request
import requests



app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    data = {}
    if request.method == "POST":
       
        city = request.form['city']
        apiKey = 'ff26ae45ef3a19295f925079f24bd07f'
        source = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric'
        response = requests.get(source)
        if response.status_code == 200:
            list_data = list_data = response.json()
        
        
            data = {
                'country_code' : str(list_data['sys']['country']),
                'cordinates' : str(list_data['coord']['lon']) + ' ' + str(list_data['coord']['lat']) ,
                'temp' : round((list_data['main']['temp']-32)*5.0/9.0,2) ,
                'humidity' : str(list_data['main']['humidity'])  , 
                'pressure' : str(list_data['main']['pressure'])   
            }
            print(data)
        else:
            data={}
    return render_template('weather.html',data=data)




app.run(debug=True)