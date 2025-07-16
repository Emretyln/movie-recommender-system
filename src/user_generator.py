import random

def generate_user_profiles(movies_df, num_users=100):
    users = {}
    for i in range(num_users):
        userid = f"user_{i + 1}"
        num_watched = random.randint(5, 25)
        watched_movies = movies_df.sample(n=num_watched)

        watch_history = []
        genre_counter = {}
        total_time = 0

        for _, row in watched_movies.iterrows():
            runtime = row['runtime']
            watch_time = runtime * random.uniform(0.3, 1.0)
            total_time += watch_time

            for g in row['genres']:
                genre_counter[g] = genre_counter.get(g, 0) + 1

            watch_history.append({
                "title": row['title'],
                "genres": row['genres'],
                "runtime": runtime,
                "watch_time": round(watch_time, 1)
            })

        sorted_genres = sorted(genre_counter.items(), key=lambda x: x[1], reverse=True)
        watched_genres = {g: count for g, count in sorted_genres}

        users[userid] = {
            "watch_history": watch_history,
            "watched_genres": watched_genres,
            "total_watch_time": round(total_time, 1)
        }
    return users
