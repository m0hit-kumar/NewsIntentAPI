from intent_model import predict_intent
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import nltk

summarizer = TextRankSummarizer()
nltk.download('punkt')

test_data = """
    The United States of America, commonly known as the United States (U.S. or US), is a country primarily located
    in North America. It consists of 50 states, a federal district, five major unincorporated territories, 186
    Indian reservations, and some minor possessions. The capital city is Washington, D.C., and the most populous
    city is New York City.
"""


def summary(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summary = summarizer(parser.document, 2)
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)
    return text_summary

# uncomment and run file to test
# print(summary(test_data))
