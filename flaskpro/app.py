from flask import Flask , render_template,request,redirect , url_for,send_file, flash
from flask_mail import Mail, Message
import os
import requests
from googletrans import Translator
from pytube import YouTube
import random
import yfinance as yf
import pyshorteners


app = Flask(__name__)


app.secret_key = 'supersecretkey'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'

mail = Mail(app)





API_KEY = os.getenv('API_KEY')
API_URL = 'https://v6.exchangerate-api.com/v6/{}/latest/'.format(API_KEY)

@app.route('/currency', methods=['GET', 'POST'])
def currency():
    if request.method == 'POST':
        base_currency = request.form['base_currency']
        target_currency = request.form['target_currency']
        amount = float(request.form['amount'])

        response = requests.get(API_URL + base_currency)
        data = response.json()

        if data['result'] == 'success':
            exchange_rate = data['conversion_rates'][target_currency]
            converted_amount = amount * exchange_rate
            return render_template('currency.html', converted_amount=converted_amount, base_currency=base_currency, target_currency=target_currency, amount=amount)
        else:
            return render_template('currency.html', error="Invalid currency code")

    return render_template('currency.html')

@app.route("/translator", methods=["GET", "POST"])
def translator():
    translated_text = ""
    if request.method == "POST":
        text_to_translate = request.form["text_to_translate"]
        source_language = request.form["source_language"]
        destination_language = request.form["destination_language"]

        translator = Translator()
        translation = translator.translate(text_to_translate, src=source_language, dest=destination_language)
        translated_text = translation.text

    return render_template("translator.html", translated_text=translated_text)

@app.route('/youtube', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            yt = YouTube(url)
            video = yt.streams.filter(progressive=True, file_extension='mp4').first()
            print(video , "Video")
            video.download(filename='video.mp4')
            return send_file('video.mp4', as_attachment=True)
        except Exception as e:
            return f"An error occurred: {e}"
    return render_template('youtube.html')


@app.route('/mail', methods=['GET', 'POST'])
def email():
    if request.method == 'POST':
        recipient = request.form['recipient']
        subject = request.form['subject']
        body = request.form['body']
        
        msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient])
        msg.body = body
        
        try:
            mail.send(msg)
            flash('Email sent successfully!', 'success')
        except Exception as e:
            flash(f'An error occurred: {e}', 'danger')
        
        return redirect(url_for('email'))
    
    return render_template('email.html')

@app.route('/dice', methods=['GET', 'POST'])
def dice():
    dice_result = None
    if request.method == 'POST':
        dice_result = random.randint(1, 6)
    return render_template('dice.html', dice_result=dice_result)

@app.route('/stock', methods=['GET', 'POST'])
def stock():
    stock_price = None
    error = None
    stock_symbol = None
    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']
        try:
            stock = yf.Ticker(stock_symbol)
            stock_info = stock.history(period="1d")
            stock_price = round(stock_info['Close'].iloc[-1], 2)
        except Exception as e:
            error = "Could not fetch the stock price. Please check the stock symbol."
    return render_template('stock.html', stock_price=stock_price, stock_symbol=stock_symbol, error=error)

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you get if you cross a snowman and a vampire? Frostbite.",
    "Why was the math book sad? Because it had too many problems."
]

@app.route('/joke', methods=['GET', 'POST'])
def joke():
    joke = None
    if request.method == 'POST':
        joke = random.choice(jokes)
    return render_template('joke.html', joke=joke)


@app.route('/url', methods=['GET', 'POST'])
def url():
    short_url = None
    if request.method == 'POST':
        long_url = request.form['long_url']
        shortener = pyshorteners.Shortener()
        try:
            short_url = shortener.tinyurl.short(long_url)
        except Exception as e:
            short_url = "Error: Invalid URL"
    return render_template('url.html', short_url=short_url)

@app.route('/newa')
def index():
    params = {
        'country': 'us',  # Change to your preferred country
        'apiKey': 'NEWS_API_KEY'
    }
    response = requests.get('NEWS_API_URL', params=params)
    news_data = response.json()

    articles = news_data.get('articles', [])
    return render_template('index.html', articles=articles)




app.run(debug=True)