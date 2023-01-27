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


def age_certification_pie():
    title = pd.read_csv("titles.csv")
    shows = title[title["type"] == 'SHOW']
    #shows = shows.loc[:, "age_certification"]
    age_certification = shows.groupby(["age_certification"])["age_certification"].count()
    print(age_certification)
    plt.pie(age_certification, labels=age_certification.index.values.tolist())
    plt.show()


# imdb_scores_hist()


# Найвдаліший рік для кіно. Для років починаючи з 2000,
# побудуйте графік відсотку фільмів та шоу що мають рейтинг,
# більший за 8.0 в залежності від року (вісь x - роки, y - відсоток).
# Назвіть найуспішніший рік - 1 бал;
def the_best_year():
    title = pd.read_csv("titles.csv")
    title_starting_from_2000 = title[(~title["imdb_score"].isna()) & (title["release_year"] > 1999)]
    years = np.unique(title_starting_from_2000["release_year"])
    list_with_scores = []
    for year in years:
        number_of_scores = len(title_starting_from_2000[title_starting_from_2000["release_year"] == year])
        number_of_good_scores = len(title_starting_from_2000[(title_starting_from_2000["imdb_score"] >= 8) & ( title_starting_from_2000["release_year"] == year)])
        percentage = number_of_good_scores/ number_of_scores
        list_with_scores.append(percentage)

    index_with_best_percent = list_with_scores.index(max(list_with_scores))
    year_with_best_percent = 2000 + index_with_best_percent
    print(year_with_best_percent)
    plt.plot(years, list_with_scores)
    plt.show()


# the_best_year()

    # number_of_good_scores = {}
    # number_of_scores = {}
    # title = pd.read_csv("titles.csv")
    # title_starting_from_2000 = title[(~title["imdb_score"].isna()) & (title["release_year"] > 1999)]
    # good_scores = title_starting_from_2000[(title_starting_from_2000["imdb_score"] > 8.0)]
    # print(good_scores["imdb_score"])
    # print(title_starting_from_2000["imdb_score"])
    # years = np.unique(title_starting_from_2000["release_year"])
    # for year in years:
    #     number_of_good_scores[year] = 0
    #     number_of_scores[year] = 0
    #     for row_idx, row_obj in title_starting_from_2000.iterrows():
    #         print(row_obj)
    #         for row_good_idx, row_good_obj in good_scores.iterrows():
    #             if row_obj == row_good_obj:
    #                 number_of_good_scores[year] += 1
    #         number_of_scores[year] += 1
    # list_with_percentage = []
    # for year in years:
    #     percentage = number_of_good_scores[year] / number_of_scores[year]
    #     list_with_percentage.append(percentage)
    # print(years)
    # print(list_with_percentage)
    # plt.plot(years, list_with_percentage)
    # plt.show()


# Рейтинг акторів, що знімаються в гарних фільмах. Використавши дані обох таблиць,
# візміть топ-1000 фільмів на платформі за рейтингом imdb, та наведіть топ-10 акторів за кількістю фільмів
# серед цієї тисячі. - 1 бал;
def best_actors():
    titles = pd.read_csv("titles.csv")
    credits_df = pd.read_csv("credits.csv")
    credits_df = credits_df[credits_df["role"] == "ACTOR"]
    titles = titles[titles["type"] == "MOVIE"]
    sorted_titles = titles.sort_values("imdb_score")
    sorted_titles = sorted_titles[~sorted_titles["imdb_score"].isna()]
    first_thousand = sorted_titles[-1001:-1]
    suitable_ids = first_thousand["id"]
    dictionary_with_actors = {}
    for film_id in suitable_ids:
        names_of_actors = credits_df[credits_df["id"] == film_id]["name"]
        for name in names_of_actors:
            if name in dictionary_with_actors:
                dictionary_with_actors[name] += 1
            else:
                dictionary_with_actors[name] = 1
    sorted_dictionary = {k: v for k, v in sorted(dictionary_with_actors.items(), key=lambda item: item[1], reverse=True)}
    print(sorted_dictionary)


def categories_bar():
    titles = pd.read_csv("titles.csv")
    credits_df = pd.read_csv("credits.csv")
    credits_df = credits_df[credits_df["role"] == "ACTOR"]
    titles = titles[titles["type"] == "MOVIE"]
    sorted_titles = titles.sort_values("imdb_score")
    sorted_titles = sorted_titles[~sorted_titles["imdb_score"].isna()]
    first_thousand = sorted_titles[-1001:-1]
    categories = {}
    for i in first_thousand.loc[:,"genres"]:
        i = i[2:-2]
        i = i.split("', '")
        for genre in i:
            if genre in categories:
                categories[genre] += 1
            else:
                categories[genre] = 1
    df = pd.DataFrame(list(categories.items()))
    plt.barh(df[0], df[1])
    plt.show()
categories_bar()

