import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def build_user_movie_matrix(movies_cleaned, user_profiles):
    all_movies = movies_cleaned['title'].unique()
    all_users = list(user_profiles.keys())
    user_movie_matrix = pd.DataFrame(0.0, index=all_users, columns=all_movies)

    for user_id, data in user_profiles.items():
        for movie in data['watch_history']:
            user_movie_matrix.loc[user_id, movie['title']] = movie['watch_time'] / movie['runtime']

    return user_movie_matrix


def compute_user_similarity(user_movie_matrix):
    sim = cosine_similarity(user_movie_matrix)
    return pd.DataFrame(sim, index=user_movie_matrix.index, columns=user_movie_matrix.index)


def recommend_movies(userid, user_profiles, user_movie_matrix, user_similarity_df, n=10):
    all_movies = user_movie_matrix.columns
    watched_titles = [m['title'] for m in user_profiles[userid]['watch_history']]
    unwatched_movies = [m for m in all_movies if m not in watched_titles]

    if user_similarity_df[userid].sum() == 0:
        return user_movie_matrix.sum().sort_values(ascending=False).head(n).index.tolist()

    similar_users = user_similarity_df[userid].sort_values(ascending=False)[1:6].index
    similar_users_movies = user_movie_matrix.loc[similar_users]
    scores = similar_users_movies[unwatched_movies].mean(axis=0)

    return scores.sort_values(ascending=False).head(n * 2).index.tolist()


def filter_by_genres(recommended_movies, movies_cleaned, user_profile, top_n=5):
    preferred_genres = list(user_profile['watched_genres'].keys())[:3]
    filtered = []
    for title in recommended_movies:
        genres_list = movies_cleaned[movies_cleaned['title'] == title]['genres'].values
        if genres_list.size > 0 and any(g in preferred_genres for g in genres_list[0]):
            filtered.append(title)
        if len(filtered) >= top_n:
            break
    return filtered
