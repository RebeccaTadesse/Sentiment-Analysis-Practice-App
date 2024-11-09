# coding-project-template
This repo is for the practice project which is to be based on Embedded AI libraries. 

This project uses Embeddable Watson AI Libraries, specifically the Watson NLP Library. As this project was completed using the
Skills Network Labs Cloud IDE, these libraries were pre-installed. You can find the library at the following link:
https://www.ibm.com/products/natural-language-processing?utm_source=ibm_developer&utm_content=in_content_link&utm_id=articles_watson-libraries-embeddable-ai-that-works-for-you&cm_sp=ibmdev-_-developer-articles-_-product

# Overview
The goalof this project is to create an AI app called "Sentiment Analysis". Users can input text in the user face, and the app uses sentiment analysis to tell the user whether the text was positive, negative or neutral.

## Sentiment Analysis
Natural Language Processing(NLP) sentiment analysis is the practice of using computers to recognize sentiment or emotion expressed in a text. Through NLP, sentiment analysis categorizes words as positive, negative or neutral.

Sentiment analysis is often performed on textual data to help businesses monitor brand and product sentiment in customer feedback, and understanding customer needs. It helps attain the attitude and mood of the wider public which can then help gather insightful information about the context.

## NLP Library
The NLP library includes functions for sentiment analysis, emotion detection, text classification, language detection, etc. among others. The speech-to-text library contains functions that perform the transcription service and generates written text from spoken audio. The text-to-speech library generates natural sounding audio from written text. 
For this project, we use the BERT based Sentiment Analysis function of the Watson NLP Library.

## Project Overview
### Application
The application is packaged as SentimentAnalysis. It contains the __init__ file and the main file for our sentiment anaylsis function (sentiment_analyzer). sentiment_analyzer takes the input from the interface (the user) and returns the label (POSITIVE, NEGATIVE, NEUTRAL) and score (between 0 and 1) of the user's text.
If invalid text is received, the user will receive an invalid text error
If the user doesn't input anything, the user will be prompted to not leave the field blank.
### Unit Tests
Unit testing was conducted on the sentiment_analyzer in the file test_sentiment_analysis.py. Here, we test if sentiment_analyzer returns the correct labels for a positive, negative and neutral test case.
### Deployment
To deploy the app, index.html in the templates folder and mywebscript.js in the static folder were provided for the interface of this project.
When interacting with the html interface, clicking the "Run Sentiment Analysis" button calls the javascript file, which in turn executes a GET request and takes the text provided by the user as input.This text, saved in a variable named textToAnalyze, is then passed on to the server file to be sent to the application. The main task in this project, however, was the completion of server.py.
server.py initiates the application of sentiment analysis to be executed over the Flask channel and deployed on localhost:5000

### Notes
- This app works with several languages including French and German. Feel free to test more and see if you get an invalid text error!
- Static code analysis was performed to ensure that the code for sentiment_analysis.py and server.py follow PEP8 guidelines


### Topics covered
- Sentiment Analysis
- Watson NLP Library
- Packages
- Unit Tesing
- Flask
- Error Handling
- Pylint

