from flask import Flask, request, jsonify
from intent_model import predict_intent
from flask_cors import CORS
from flask import Blueprint
from text_summarizer import summary

app = Flask(__name__)

my_blueprint = Blueprint('my_blueprint', __name__)

# Enable CORS for all routes under the blueprint
cors = CORS(my_blueprint, resources={r"/*": {"origins": "*"}})


def data_processing(data):
    for news in data:
        intent = predict_intent(summary(news["text"]))
        news["intent"] = intent
    return data


@app.route("/newsintent", methods=['POST'])
def intenter():
    data = request.json
    news = data_processing(data["news"])
    data["news"] = news
    return jsonify(data)


@app.route("/")
def index():
    return "application is running"


if __name__ == '__main__':
    app.run(debug=False)
