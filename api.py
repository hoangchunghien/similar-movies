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

indices = pd.Series(data.index, index=data['id']).drop_duplicates()

def get_recommendations(id):
    index = indices[id]

    # Get the pairwsie similarity scores of all movies with that movie
    cosine_sim = linear_kernel(tfidf_matrix[index], tfidf_matrix)
    sim_scores = list(enumerate(cosine_sim[0]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return data.iloc[movie_indices]


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

@app.route('/movies/<id>', methods=['GET'])
def movie(id):
    return jsonify(
        data=json.loads(data.iloc[[indices[id]]].to_json(orient='records')),
        similar_movies=json.loads(get_recommendations(id).to_json(orient='records')))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
