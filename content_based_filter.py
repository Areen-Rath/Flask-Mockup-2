import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

articles = pd.read_csv('articles.csv')
articles = articles[articles["title"].notna()]

count = CountVectorizer(stop_words = "english")
count_matrix = count.fit_transform(articles["title"])

similarity = cosine_similarity(count_matrix, count_matrix)

articles = articles.reset_index()
indices = pd.Series(articles.index, index = articles["title"])

def recommend(title, cs):
    id = indices[title]
    sim_score = list(enumerate(cs[id]))
    sim_score = sorted(sim_score, key = lambda x: x[1], reverse = True)
    sim_score = sim_score[1:11]
    article_indices = [i[0] for i in sim_score]
    return articles[["title", "text", "lang"]].iloc[article_indices].values.tolist()