''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
# Import the sentiment_analyzer function from the package created
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
#Initiate the flask app :
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # Retrieve text from request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass input text to analyzer
    response = sentiment_analyzer(text_to_analyze)
    # If there is no response at all, the user must input a string to be evaluated
    if response is None:
        return "Please don't leave the field blank."
    # Extract label and score
    label = response['label']
    score = response['score']

    # If there is no label, then the input can't be evaluated by the sentiment analyzer
    if label is None:
        return "Invalid input! Try again."

    return f"The given test has been identified \
     as {label.split('_')[1]} with a score of {score}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")


if __name__ == "__main__":
    # This function executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
