from flask import Flask, Response
from flask import request
from flask import jsonify

import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

IMAGE_IMDB = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2'

data = pd.read_csv('movies_metadata.csv', low_memory=False)
data['overview'] = data['overview'].fillna('')

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['overview'])


app = Flask(__name__)

@app.route('/movies', methods=['GET'])
def movies():
    """
    Show a list of movies
    """
    args = request.args
    start = int(args['start']) if 'start' in args else 0
    limit = int(args['limit']) if 'limit' in args else 10

    return jsonify(
            data=json.loads(data[start:start+limit].to_json(orient='records')),
            count=data.shape[0],
            start=start,
            limit=limit)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
