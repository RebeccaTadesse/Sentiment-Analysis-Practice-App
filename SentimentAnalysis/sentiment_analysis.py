# NLP Sentiment Analysis Application
''' This file contains the primary function for running sentiment analysis using Watson.
    It is part of the SentimentAnalysis package and is to be referenced in server.py. 
'''
# Import relevant methods
import json
import requests

# Define a function for running sentiment analysis using the Watson
# NLP BERT Sentiment Analysis Function
def sentiment_analyzer(text_to_analyze):
    ''' This function takes the input text_to_analyze and uses Watson NLP library
        to perform sentiment analysis. The output is given as a dictionary containing
        the label (POSITIVE, NEGATIVE, NEUTRAL)and score of the text, which are None 
        if the text input is invalid.
    '''
    if text_to_analyze == "":
        return None
    #URL of sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    # Headers required for API request
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    # Dictionary with text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze }}
    # Send POST request to the API with the text to be analyzed
    response = requests.post(url, json = myobj, headers=headers, timeout=30)
    # Format the response as dictionary (JSON)
    formatted_response = json.loads(response.text)
    # Check response code to see if 'response' is valid or invalid text
    if response.status_code == 500:
        # If 500 (error code) is received, return None
        score = None
        label = None
    elif response.status_code == 200:
        # if status is OK, extract and return score and label
        score = formatted_response['documentSentiment']['score']
        label = formatted_response['documentSentiment']['label']
    else:
        score = None
        label = None
    # Return label and score in a dictionary
    return {'label': label, 'score': score }
