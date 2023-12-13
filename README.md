#### Movie Recommendation System 

This application leverages Machine Learning concepts, specifically NLP and cosine similarity to suggest a 10 movies to user. By definition, content-based recommender systems are recommendation systems that suggest items, movies in our case, based on the characteristics or features of the items themselves.

##### How to Use the Recommender system

1. **Select a Movie**: Use the dropdown menu to choose a movie that piques your interest.

2. **Get Recommendations**: Click the "Recommend" button to unveil a curated list of movie suggestions related to your selection.

3. **Explore Recommendations**: Delve into the recommendations presented in a visually appealing layout, complete with movie titles and eye-catching posters.

##### Code Overview

The application with Python using the following key libraries:

- `streamlit`: For creating the user interface.
- `pandas`: For data manipulation.
- `requests`: For making API requests.
- `pickle`: For serializing and deserializing Python objects.

##### How It Works

1. **Movie Data**: The system relies on a pre-processed movie dataset stored in 'movies_list.pkl'.

2. **Similarity Calculation**: A similarity matrix ('similarity.pkl') is used to determine the closeness between movies.

3. **Recommendation Algorithm**: The recommender function suggests a set of movies based on the user's selection.

4. **Poster Retrieval**: Posters for recommended movies are fetched from The Movie Database (TMDb) API.

## Prerequisites

- Python 3.x
- Install required libraries using: `pip install streamlit pandas requests`

##### Quick Start

1. Clone the repository.

   ```bash
   git clone https://github.com/Marie-Ishimwe/Movie-Recommender-system.git
   cd Book-Recommender-system
##### Appendix
- [Deployed system](https://movie-recommender-systemgit-89erqew5mmuc6kz8xadk6n.streamlit.app/)
- [Video walkthrough](https://www.openai.com)

