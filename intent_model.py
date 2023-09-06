import pickle
import nltk
nltk.download('stopwords')

label_mapping = {
    1: "earthquake",
    2: "tornado",
    3: "volcano",
    4: "war",
    5: "floods",
    6: "misc",
}

with open('model_and_vectorizer.pkl', 'rb') as model_path:
    model, vectorizer = pickle.load(model_path)


test_text = "The United States of America, commonly known as the United States (U.S. or US), is a country primarily located in North America.The capital city is Washington, D.C., and the most populous city is New York City."


def predict_intent(text):
    print("predict_int")
    text = vectorizer.transform([text])
    # return model.predict(text)
    return label_mapping.get(model.predict(text).item(), 'Unknown')


# uncomment and run file to test
# print(predict_intent(test_text))
