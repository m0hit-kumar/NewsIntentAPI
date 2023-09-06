from flask import Flask, request, jsonify

from text_summarizer import data_processing

app = Flask(__name__)


@app.route("/", methods=['POST'])
def intenter():
    data = request.json
    news = data_processing(data["news"])
    return jsonify(news)


if __name__ == '__main__':
    app.run(debug=True)
