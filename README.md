# Movie_recommendation_code
Movie recommendations based on watched films using genres, actors, and ratings. Follows Rule Based Recommendation Model and self as a foundation for many recommendation models.
The Movie Recommendation System is a Python-based application designed to suggest movies to users based on their previously watched films. It uses a rule-based content filtering approach, analyzing movie metadata such as genres and actors to determine user preferences.

Key Features and Workflow:

Watched Movies Input:
The user provides a list of movies they have recently watched. The system extracts the relevant entries from the dataset to analyze preferences.

Genre Analysis:
The system parses the “genres” field of watched movies and creates a frequency distribution of genres. It identifies preferred genres based on the most frequently appearing genres and searches the dataset for other movies belonging to those genres.

Actor Analysis:
Similarly, it examines the “actors” field from watched movies, identifies frequently appearing actors, and finds other movies featuring those actors.

Combining Results:
Movies identified from genre and actor analysis are combined, duplicates are removed, and previously watched movies are excluded.

Ranking:
The final recommendations are sorted by ratings to present the highest-rated movies first, ensuring the most relevant and popular options appear at the top.

Technical Details:

Uses Pandas for data manipulation.

Uses ast.literal_eval to parse list-like strings in dataset fields.

Rule-based filtering determines user preferences without requiring prior training or machine learning.

Can handle missing or malformed data safely.

Potential Upgrades to Machine Learning:

While the current system is rule-based, it can be extended into a machine learning recommendation system using:

Content-based filtering: TF-IDF vectorization of genres, actors, and descriptions, followed by cosine similarity.

Collaborative filtering: Matrix factorization or SVD to learn from multiple users’ ratings and behavior.
