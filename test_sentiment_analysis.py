from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def testsentiment_analyzer(self):

        # Test case for positive statement
        test1 = sentiment_analyzer("I love working with Python")
        self.assertEqual(test1['label'], 'SENT_POSITIVE')

        # Test case for negative statement
        test2 = sentiment_analyzer("I hate working with Python")
        self.assertEqual(test2['label'], 'SENT_NEGATIVE')

        # Test case for neutral statement
        test3 = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(test3['label'], 'SENT_NEUTRAL')


unittest.main()