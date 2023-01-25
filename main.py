import pandas as pd
import matplotlib.pyplot as plt


# Побудуйте окремі гістограмми розподілу фільмів
# та серіалів за оцінкою IMDB з кроком у 0.2 бали.
# У кого вища середня оцінка? - 0.5 бали;
def imdb_scores_hist():
    title = pd.read_csv("titles.csv")
    print(title)
    shows = title[title["type"] == 'SHOW']
    print(shows.loc[:, "type"])
    movies = title[title["type"] == 'MOVIE']
    print(movies.loc[:, "type"])

    figure, axes = plt.subplots(2)
    imdb_scores = shows.loc[:, "imdb_score"]
    axes[0].hist(imdb_scores, 50)
    imdb_scores = movies.loc[:, "imdb_score"]
    axes[1].hist(imdb_scores, 50)
    plt.show()

imdb_scores_hist()
