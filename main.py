from src.data_loader import load_and_clean_data
from src.user_generator import generate_user_profiles
from src.recommender import (
    build_user_movie_matrix,
    compute_user_similarity,
    recommend_movies,
    filter_by_genres
)


def main():
    filepath = "data/movies_metadata.csv"
    movies_cleaned = load_and_clean_data(filepath)
    user_profiles = generate_user_profiles(movies_cleaned, num_users=100)

    user_movie_matrix = build_user_movie_matrix(movies_cleaned, user_profiles)
    user_similarity_df = compute_user_similarity(user_movie_matrix)

    target_user = "user_1"
    raw_recs = recommend_movies(target_user, user_profiles, user_movie_matrix, user_similarity_df, n=10)
    final_recs = filter_by_genres(raw_recs, movies_cleaned, user_profiles[target_user], top_n=5)

    print(f"\nRecommended movies for {target_user}:")
    for i, movie in enumerate(final_recs, 1):
        print(f"{i}. {movie}")

    # Display sample watch history
    for uid in list(user_profiles.keys())[:3]:
        print(f"\nWatch history for {uid}:")
        for movie in user_profiles[uid]['watch_history'][:3]:
            print(f"- {movie['title']} (Watched {movie['watch_time']} mins)")


if __name__ == "__main__":
    main()
