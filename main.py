import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Побудуйте окремі гістограмми розподілу фільмів
# та серіалів за оцінкою IMDB з кроком у 0.2 бали.
# У кого вища середня оцінка? - 0.5 бали;
def imdb_scores_hist():
    title = pd.read_csv("titles.csv")
    # print(title)
    shows = title[title["type"] == 'SHOW'].dropna()
    # print(shows.loc[:, "type"])
    movies = title[title["type"] == 'MOVIE']
    # print(movies.loc[:, "type"])

    figure, axes = plt.subplots(2)
    imdb_scores_shows = shows.loc[:, "imdb_score"].dropna()
    # print(imdb_scores_shows)
    axes[0].hist(imdb_scores_shows, np.arange(0, 10.2, 0.2))
    imdb_scores_movies = movies.loc[:, "imdb_score"]
    axes[1].hist(imdb_scores_movies, np.arange(0, 10.2, 0.2))

    mean_score_movies = imdb_scores_movies.mean()
    mean_score_shows = imdb_scores_shows.mean()
    print(f"Mean score for movies is {mean_score_movies}, and for shows is {mean_score_shows}")

    plt.show()


imdb_scores_hist()
