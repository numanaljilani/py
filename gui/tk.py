import tkinter as tk
from tkinter import ttk, messagebox
# import requests

# Replace with your own API keys
WEATHER_API_KEY = 'ff26ae45ef3a19295f925079f24bd07f'
CURRENCY_API_KEY = 'https://v6.exchangerate-api.com/v6/{}/latest/'.format('a5dbdb21698bea71f320109d')

def get_weather():
    city = city_entry.get()
    if city:
        try:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric'
            response = requests.get(url)
            data = response.json()

            if data.get('cod') != 200:
                messagebox.showerror("Error", data.get('message'))
                return

            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            weather_result.config(text=f'Temperature: {temperature}°C\nDescription: {description.capitalize()}')

        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "City field cannot be empty")

def convert_currency():
    amount = amount_entry.get()
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()

    if not amount or not amount.isdigit():
        messagebox.showerror("Error", "Amount should be a valid number")
        return

    if from_currency and to_currency:
        try:
            url = f'https://v6.exchangerate-api.com/v6/{CURRENCY_API_KEY}/latest/{from_currency}'
            response = requests.get(url)
            data = response.json()

            if data.get('result') != 'success':
                messagebox.showerror("Error", data.get('error-type'))
                return

            exchange_rate = data['conversion_rates'][to_currency]
            converted_amount = float(amount) * exchange_rate
            conversion_result.config(text=f'{amount} {from_currency} = {converted_amount:.2f} {to_currency}')

        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Currency fields cannot be empty")

root = tk.Tk()
root.title("Weather and Currency Converter App")

# Weather App UI
weather_frame = ttk.LabelFrame(root, text="Weather App")
weather_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

ttk.Label(weather_frame, text="City:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
city_entry = ttk.Entry(weather_frame)
city_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

get_weather_button = ttk.Button(weather_frame, text="Get Weather", command=get_weather)
get_weather_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

weather_result = ttk.Label(weather_frame, text="")
weather_result.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Currency Converter UI
currency_frame = ttk.LabelFrame(root, text="Currency Converter")
currency_frame.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

ttk.Label(currency_frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
amount_entry = ttk.Entry(currency_frame)
amount_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

ttk.Label(currency_frame, text="From:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
from_currency_combobox = ttk.Combobox(currency_frame, values=['USD', 'EUR', 'INR'])
from_currency_combobox.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

ttk.Label(currency_frame, text="To:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
to_currency_combobox = ttk.Combobox(currency_frame, values=['USD', 'EUR', 'INR'])
to_currency_combobox.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

convert_button = ttk.Button(currency_frame, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

conversion_result = ttk.Label(currency_frame, text="")
conversion_result.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
