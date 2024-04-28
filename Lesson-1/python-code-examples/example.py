"""basic Flask app - demo of using a variable in a route"""

from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    greeting = '<h1>Welcome to the Daily Motivation App!</h1>'
    instruction = '<p>Visit <a href="/day/monday">Monday\'s motivation</a> or change the day in the <em>browser address bar</em> to get a motivational quote for today.</p>'
    return greeting + instruction

@app.route('/day/<dayname>')

def day(dayname=None):
    if not dayname:
        dayname = datetime.datetime.now().strftime('%A').lower()
    quotes = {
        'monday': "Monday: Conquer your challenges with courage and confidence!",
        'tuesday': "Tuesday: Every step forward is a step toward achieving something bigger.",
        'wednesday': "Wednesday: Keep pushing through the week—you're halfway there!",
        'thursday': "Thursday: Focus on what matters and let go of what doesn't.",
        'friday': "Friday: Finish your week strong and get ready for a relaxing weekend!",
        'saturday': "Saturday: Take time to enjoy the fruits of your hard work.",
        'sunday': "Sunday: Prepare for the upcoming week with a peaceful mind."
    }
    quote = quotes.get(dayname.lower(), "Sorry, that's not a valid day. Please choose another day.")
    return f'<h1>{quote}</h1><p>Change the day in the <em>browser address bar</em> to see quotes for other days.</p>'

if __name__ == '__main__':
    app.run(debug=True)
