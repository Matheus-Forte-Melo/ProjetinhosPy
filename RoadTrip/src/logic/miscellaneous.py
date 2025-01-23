from datetime import datetime
from src.weather import Weather
color = ['\033[32m', '\033[0m']
w = Weather()


def weather_now():
    weath = w.get_weather()
    print(color[0])
    print(f"You take a look outside, you're not totally certain, but the weather seems {weath.lower()}!")
    print(color[1])


def temperature():
    temp = w.get_temperature()
    print(color[0])
    print(f'You open your car windows and put your hand outside.', end=' ')
    if temp <= 5:
        print('Immediately, a frigid gust of wind passes through your fingers, causing a tingling sensation and\n'
              'shivers running down your arm. The intense cold pierces your skin, creating a feeling of numbness as\n'
              'you feel the tips of your fingers becoming icy')
    elif temp > 5 and temp <= 15:
        print('A chilly gust of wind rushes through your fingers, creating a cool sensation and causing a slight\n'
              'shiver to run down your arm.')
    elif temp > 15 <= 25:
        print('A refreshing breeze brushes against your fingers, creating a pleasant sensation as it caresses your\n'
              'skin.')
    elif temp > 35:
        print('A wave of intense heat engulfs your fingers, creating a sensation of warmth that verges on discomfort.\n'
              'The scorching air sears your skin, causing a prickling sensation and making your hand feel flushed and\n'
              'sweaty.')
    print(color[1])
    print(f'Temperature feels like {temp:.0f}C°')


def time():
    print(color[0])
    print(f'You take a look at your wrist watch, it marks: {color[1]}{datetime.now().time()}')
    print()






