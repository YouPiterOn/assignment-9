import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Побудуйте окремі гістограмми розподілу фільмів
# та серіалів за оцінкою IMDB з кроком у 0.2 бали.
# У кого вища середня оцінка? - 0.5 бали;
def imdb_scores_hist():
    title = pd.read_csv("titles.csv")
    # print(title)
    shows = title[title["type"] == 'SHOW']
    # print(shows.loc[:, "type"])
    movies = title[title["type"] == 'MOVIE']
    # print(movies.loc[:, "type"])

    figure, axes = plt.subplots(2)
    imdb_scores_shows = shows.loc[:, "imdb_score"].dropna()
    # print(imdb_scores_shows)
    axes[0].hist(imdb_scores_shows, np.arange(0, 10.2, 0.2))
    imdb_scores_movies = movies.loc[:, "imdb_score"].dropna()
    axes[1].hist(imdb_scores_movies, np.arange(0, 10.2, 0.2))

    mean_score_movies = imdb_scores_movies.mean()
    mean_score_shows = imdb_scores_shows.mean()
    print(f"Mean score for movies is {mean_score_movies}, and for shows is {mean_score_shows}")

    plt.show()


# imdb_scores_hist()


# Найвдаліший рік для кіно. Для років починаючи з 2000,
# побудуйте графік відсотку фільмів та шоу що мають рейтинг,
# більший за 8.0 в залежності від року (вісь x - роки, y - відсоток).
# Назвіть найуспішніший рік - 1 бал;
def the_best_year():
    number_of_good_scores = {}
    number_of_scores = {}
    title = pd.read_csv("titles.csv")
    title_starting_from_2000 = title[(~title["imdb_score"].isna()) & (title["release_year"] > 1999)]
    good_scores = title_starting_from_2000[(title_starting_from_2000["imdb_score"] > 8.0)]
    print(good_scores["imdb_score"])
    print(title_starting_from_2000["imdb_score"])
    years = np.unique(title_starting_from_2000["release_year"])
    for year in years:
        number_of_good_scores[year] = 0
        number_of_scores[year] = 0
        for row_idx, row_obj in title_starting_from_2000.iterrows():
            print(row_obj)
            for row_good_idx, row_good_obj in good_scores.iterrows():
                if row_obj == row_good_obj:
                    number_of_good_scores[year] += 1
            number_of_scores[year] += 1
    list_with_percentage = []
    for year in years:
        percentage = number_of_good_scores[year] / number_of_scores[year]
        list_with_percentage.append(percentage)
    print(years)
    print(list_with_percentage)
    plt.plot(years, list_with_percentage)
    plt.show()





    #
    # years = np.arange(title_starting_from_2000["release_year"])
    # print(years)
    # print(title_starting_from_2000["imdb_score"])
    # # plt.plot(years, good)
    # # plt.show()


the_best_year()
