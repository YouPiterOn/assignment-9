import pandas as pd
import matplotlib.pyplot as plt


# Побудуйте окремі гістограмми розподілу фільмів
# та серіалів за оцінкою IMDB з кроком у 0.2 бали.
# У кого вища середня оцінка? - 0.5 бали;
def imdb_scores_hist():
    title = pd.read_csv("titles.csv")
    print(title)
    imdb_scores = title.loc[:, "imdb_score"]
    print(imdb_scores)
    plt.hist(imdb_scores, 50)
    plt.show()

imdb_scores_hist()
