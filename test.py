import plotly.graph_objects as go
import pandas as pd
import requests

# Funktion zum Abrufen der Wetterdaten von OpenWeatherMap
def get_weather_data(city):
    api_key = '7e90b28cff484e2dec37a45f3daa259e'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

# Funktion zum Erstellen des interaktiven Diagramms
def create_plot(data):
    temperatures = [entry['main']['temp'] for entry in data['list']]
    timestamps = [entry['dt'] for entry in data['list']]
    dates = pd.to_datetime(timestamps, unit='s')
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=temperatures, name='Temperatur (°C)'))
    
    fig.update_layout(
        title='Temperaturverlauf',
        xaxis_title='Zeit',
        yaxis_title='Temperatur (°C)',
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label='1 Tag', step='day', stepmode='backward'),
                    dict(count=3, label='3 Tage', step='day', stepmode='backward'),
                    dict(count=7, label='1 Woche', step='day', stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(visible=True),
            type='date'
        )
    )
    
    fig.show()

# Eingabe der Stadt und Abruf der Wetterdaten
city = 'Mehrnbach'
weather_data = get_weather_data(city)

# Erstellung des interaktiven Diagramms
create_plot(weather_data)