from sentence_transformers import SentenceTransformer
import pickle


model = SentenceTransformer('nli-distilroberta-base-v2')
pickle.dump(model, open("model.pkl", "wb"))

# sentences = [
#     "This is an awesome book to learn NLP.",
#     "DistilBERT is an amazing NLP model.",
#     "We can interchangeably use embedding, encoding, or vectorizing.",
# ]

# vectorizer.run(sentences)
# vectors = vectorizer.vectors