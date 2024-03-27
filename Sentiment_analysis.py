from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

def perform_sentiment_analysis(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        comments = request.form.getlist('comments')
        sentiments = [perform_sentiment_analysis(comment) for comment in comments]
        positive_count = sentiments.count('Positive')
        negative_count = sentiments.count('Negative')
        neutral_count = sentiments.count('Neutral')
        total_comments = len(comments)
        return render_template('results.html', total_comments=total_comments, positive_count=positive_count, negative_count=negative_count, neutral_count=neutral_count)

if __name__ == '__main__':
    app.run(debug=True)
