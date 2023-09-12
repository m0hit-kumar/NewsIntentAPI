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


def predict_intent(text):
    text = vectorizer.transform([text])
    return label_mapping.get(model.predict(text).item(), 'Unknown')
