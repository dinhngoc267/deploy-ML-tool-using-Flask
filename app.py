from flask import Flask, request, jsonify, render_template
import pickle
from scipy import spatial

from numpy import vectorize


# Create Flask app
app = Flask(__name__)

# Load the pickle model
model = pickle.load(open("model.pkl", "rb"))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sents = request.json       
        sent1 = sents['sent1']
        sent2 = sents['sent2']
        print(sent1,sent2)
        vectors = model.encode([sent1, sent2])
        dist_1 = spatial.distance.cosine(vectors[0], vectors[1])        
        print(dist_1)
        return str(round(dist_1, 2))

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

