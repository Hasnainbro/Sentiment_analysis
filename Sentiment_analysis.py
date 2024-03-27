import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

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

def main():
    print("Welcome to Sentiment Analysis Tool!")
    print("Please enter the comments you want to analyze (press Enter after each comment, or leave blank to exit):")

    comments = []
    while True:
        user_input = input("> ")
        if not user_input:
            print("Analyzing comments...")
            break

        comments.append(user_input)

    sentiments = []
    for comment in comments:
        sentiment = perform_sentiment_analysis(comment)
        sentiments.append(sentiment)

    positive_count = sentiments.count('Positive')
    negative_count = sentiments.count('Negative')
    neutral_count = sentiments.count('Neutral')

    print("\nSentiment Analysis Results:")
    print(f"Total Comments: {len(comments)}")
    print(f"Positive Comments: {positive_count}")
    print(f"Negative Comments: {negative_count}")
    print(f"Neutral Comments: {neutral_count}")

if __name__ == "__main__":
    main()
