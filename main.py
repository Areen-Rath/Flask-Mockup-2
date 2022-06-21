import csv
from flask import Flask, request, jsonify
from demographic_filter import output
from content_based_filter import recommend

app = Flask(__name__)

with open('articles.csv', encoding = "utf-8") as f:
    reader = csv.reader(f)
    articles = list(reader)
    all_articles = articles[1:]

liked_articles = []
disliked_articles = []

@app.route("/first")
def first():
    return jsonify({
        "data": [{
            "title": all_articles[0][-4],
            "text": all_articles[0][-3],
            "lang": all_articles[0][-2]
        }],
        "message": "Success"
    }), 200

@app.route("/popular")
def popular_articles():
    return jsonify({
        "data": output,
        "message": "Success"
    }), 200

@app.route("/recommended")
def recommended_articles():
    recommended = []
    for movie in liked_articles:
        output = movie[-4]
        for data in output:
            recommended.append(data)

    import itertools

    recommended.sort()
    recommended = list(recommend for recommend, _ in itertools.groupby(recommended))

    return jsonify({
        "data": recommended,
        "message": "Success"
    }), 200

@app.route("/liked_articles", methods = ["POST"])
def get_liked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)

    return jsonify({
        "message": "Success"
    }), 200

@app.route("/disliked_articles", methods = ["POST"])
def get_disliked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    disliked_articles.append(article)

    return jsonify({
        "message": "Success"
    }), 200

if __name__ == "__main__":
    app.run()