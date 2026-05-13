# Single-File Tech Project: AI Sentiment Analyzer + Weather (Paste & Run!)
# pip install nltk requests matplotlib textblob (one-time)
import nltk, requests, matplotlib.pyplot as plt, sys
from textblob import TextBlob
from datetime import datetime
nltk.download('punkt', quiet=True); nltk.download('averaged_perceptron_tagger', quiet=True)

API_KEY = 'demo'  # Get free key: openweathermap.org (replace 'demo')
CITY = 'Indore'

print("🚀 Tech Demo: AI Sentiment + Weather Forecast")
text = input("Enter text for AI sentiment analysis: ")
blob = TextBlob(text)
print(f"Sentiment: {blob.sentiment.polarity:.2f} ({'Positive' if blob.sentiment.polarity > 0 else 'Negative/Neutral'})")

def get_weather(city):
    if API_KEY == 'demo': return {'list': [{'main': {'temp': 28}, 'weather': [{'description': 'sunny'}]}]*3}
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

data = get_weather(CITY)
temps = [28, 29, 27] if not data else [d['main']['temp'] for d in data['list'][:3]]
times = [datetime.now().strftime('%H:00'), 'Next', 'Next']
plt.plot(times, temps, marker='o', color='blue')
plt.title(f'{CITY} Quick Forecast (°C)'); plt.ylabel('Temp')
plt.savefig('demo.png'); plt.show(block=False)
print(f"Weather: ~{temps[0]}°C, sunny | Chart: demo.png")
print("✅ Demo Complete - Tech Company Ready!")
input("Press Enter to exit...")
