import pandas as pd

articles = pd.read_csv('articles.csv')

c = articles["events"].mean()
m = articles["events"].quantile(0.9)

articles2 = articles.copy().loc[articles["events"] >= m]

def weighted_rating(x, m = m, c = c):
    v = x["events"]
    r = x["events"]

    return (v/(v + m) * r) + (m/(v + m) * c)

articles2["score"] = articles2.apply(weighted_rating, axis = 1)

articles2 = articles2.sort_values("score", ascending = False)
ids = articles2.head(20)["contentId"].tolist()

output = []
for id in ids:
    article = articles.loc[articles["contentId"] == id].values
    output.append({
        "title": article[0][-4],
        "text": article[0][-3],
        "lang": article[0][-2]
    })