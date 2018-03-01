# Similar Movies
After watching an interesting movie, I always looking some movies that may interest me like the movie I have just watched. I will apply machine learning to learn about the similarity of a movie to another. I hope the movie with highest similarity score will be the movie that interest me the most.

# Requirements
This project run on **python 3.x** and **Jupyter Notebook** 

# Getting Started

## Dataset

Download movies dataset from [kaggle](https://www.kaggle.com/rounakbanik/the-movies-dataset)

## Install
```
pip install -r requirements.txt
```

## How to run
Follow notebook file [solution.ipynb](https://github.com/hoangchunghien/ml-movie-recommendation/blob/master/solution.ipynb) to understand how the solution work.


# Demo

## Run as a service api
```
python api.py
```
- **GET** `/movies`
```
{"data": [{}, ...], "count": int, "start": int, "limit": int}
```
- **GET** `/movies/<id>`
```
{"data": [{}], "similar-movies": [{}, ...]}
```

## Run as a website
Comming soon