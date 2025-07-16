# movie-recommender-system
Movie Recommendation System
Data Preparation
Synthetic User Data
Generated 100 synthetic user profiles with complete watch histories

Each profile contains: age, gender, region, and randomly assigned movies

Tracked watch time and genre preferences for each user

Movie Dataset
Processed movies_metadata.csv containing:

Movie titles

Genres

Runtime

Original language

Filtered movies with runtimes between 30-240 minutes

Recommendation Algorithm
Collaborative Filtering
Constructed user-movie matrix with normalized watch time scores

Calculated user similarities using cosine similarity

Recommended unwatched movies from most similar users

Genre-Based Filtering
Incorporated user's genre preferences from watch history

Applied additional filtering based on most-watched genres

Implementation
Python 3.10+

pandas for data processing

scikit-learn for cosine similarity calculations