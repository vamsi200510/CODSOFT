import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

print("RECOMMENDATION SYSTEM STARTED")

data = {
    'Movie': ['Inception', 'Interstellar', 'The Matrix', 'Avengers', 'Titanic'],
    'SciFi': [1, 1, 1, 0, 0],
    'Action': [1, 1, 1, 1, 0],
    'Romance': [0, 0, 0, 0, 1]
}

df = pd.DataFrame(data)

features = df.iloc[:, 1:]
similarity = cosine_similarity(features)

def recommend(movie):
    if movie not in df['Movie'].values:
        print("Movie not found!")
        return

    idx = df[df['Movie'] == movie].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nRecommendations for {movie}:")
    for i in scores[1:3]:
        print("-", df.iloc[i[0]]['Movie'])

print("Available movies:", list(df['Movie']))
choice = input("Enter a movie name: ")
recommend(choice)

input("\nPress Enter to exit...")
