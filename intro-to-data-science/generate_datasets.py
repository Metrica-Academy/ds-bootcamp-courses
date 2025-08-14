"""
Dataset Generator for Data Science Bootcamp
============================================
Creates sample datasets for exercises and projects
"""

import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta
import random
import os

np.random.seed(42)
random.seed(42)


def create_mystery_shopper_data():
    """Create dataset for opening mystery shopper challenge"""
    
    # Generate shopping patterns
    customers = []
    for i in range(100):
        customer = {
            'customer_id': f'C{i:03d}',
            'age_group': np.random.choice(['18-25', '26-35', '36-45', '46-55', '56+'], 
                                        p=[0.2, 0.3, 0.25, 0.15, 0.1]),
            'shopping_time': np.random.choice(['Morning', 'Afternoon', 'Evening'],
                                            p=[0.3, 0.4, 0.3]),
            'avg_purchase': round(np.random.gamma(2, 50), 2),
            'favorite_category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Books', 'Home'],
                                                 p=[0.2, 0.25, 0.3, 0.15, 0.1]),
            'payment_method': np.random.choice(['Credit', 'Debit', 'Cash', 'Mobile'],
                                              p=[0.4, 0.3, 0.2, 0.1]),
            'visits_per_month': np.random.poisson(4),
            'loyalty_member': np.random.choice([True, False], p=[0.6, 0.4])
        }
        customers.append(customer)
    
    # Add mystery shopper with distinctive pattern
    mystery = {
        'customer_id': 'MYSTERY',
        'age_group': '36-45',
        'shopping_time': 'Afternoon',
        'avg_purchase': 127.50,
        'favorite_category': 'Electronics',
        'payment_method': 'Credit',
        'visits_per_month': 6,
        'loyalty_member': True
    }
    
    customers[42] = mystery  # Hide in the middle
    random.shuffle(customers)
    
    return pd.DataFrame(customers)


def create_netflix_dataset():
    """Create Netflix-style viewing data"""
    
    shows = ['Stranger Things', 'The Crown', 'Ozark', 'Bridgerton', 'The Witcher',
             'Money Heist', 'Black Mirror', 'Narcos', 'The Queen\'s Gambit', 'Dark']
    genres = ['Drama', 'Thriller', 'Comedy', 'Horror', 'Documentary', 'Romance', 'Action', 'Sci-Fi']
    
    data = []
    for i in range(5000):
        record = {
            'user_id': f'U{np.random.randint(1, 1000):04d}',
            'show': np.random.choice(shows),
            'genre': np.random.choice(genres),
            'watch_time_minutes': np.random.gamma(2, 25),
            'rating': min(5, max(1, np.random.normal(3.8, 0.8))),
            'completed': np.random.choice([True, False], p=[0.7, 0.3]),
            'device': np.random.choice(['TV', 'Mobile', 'Laptop', 'Tablet'],
                                      p=[0.4, 0.25, 0.25, 0.1]),
            'time_of_day': np.random.choice(['Morning', 'Afternoon', 'Evening', 'Night'],
                                           p=[0.1, 0.2, 0.4, 0.3])
        }
        data.append(record)
    
    df = pd.DataFrame(data)
    df['rating'] = df['rating'].round(1)
    df['watch_time_minutes'] = df['watch_time_minutes'].round(0)
    
    return df


def create_covid_healthcare_data():
    """Create COVID-19 healthcare dataset"""
    
    # Generate synthetic patient data
    n_patients = 2000
    
    data = {
        'patient_id': [f'P{i:05d}' for i in range(n_patients)],
        'age': np.random.gamma(7, 7, n_patients).astype(int).clip(1, 95),
        'gender': np.random.choice(['M', 'F'], n_patients),
        'temperature': np.random.normal(98.6, 1.5, n_patients).round(1),
        'oxygen_level': np.random.normal(95, 5, n_patients).round(0).clip(70, 100),
        'cough': np.random.choice([0, 1], n_patients, p=[0.4, 0.6]),
        'fatigue': np.random.choice([0, 1], n_patients, p=[0.3, 0.7]),
        'breathing_difficulty': np.random.choice([0, 1], n_patients, p=[0.7, 0.3]),
        'existing_conditions': np.random.choice(['None', 'Diabetes', 'Heart Disease', 'Hypertension', 'Multiple'],
                                               n_patients, p=[0.5, 0.15, 0.15, 0.15, 0.05]),
        'test_result': np.random.choice(['Negative', 'Positive'], n_patients, p=[0.7, 0.3])
    }
    
    df = pd.DataFrame(data)
    
    # Add hospitalization based on severity
    df['hospitalized'] = ((df['oxygen_level'] < 90) | 
                          (df['temperature'] > 102) | 
                          (df['breathing_difficulty'] == 1)).astype(int)
    
    # Positive cases more likely with symptoms
    symptom_score = df['cough'] + df['fatigue'] + df['breathing_difficulty']
    positive_prob = symptom_score / 6 + 0.2
    df.loc[np.random.random(n_patients) < positive_prob, 'test_result'] = 'Positive'
    
    return df


def create_retail_transaction_data():
    """Create retail transaction dataset for customer segmentation"""
    
    n_transactions = 10000
    n_customers = 500
    
    products = {
        'Electronics': ['Laptop', 'Phone', 'Headphones', 'Camera', 'Tablet'],
        'Clothing': ['Shirt', 'Jeans', 'Dress', 'Shoes', 'Jacket'],
        'Food': ['Groceries', 'Snacks', 'Beverages', 'Frozen', 'Fresh Produce'],
        'Home': ['Furniture', 'Decor', 'Kitchen', 'Bedding', 'Storage'],
        'Books': ['Fiction', 'Non-fiction', 'Educational', 'Comics', 'Magazines']
    }
    
    prices = {
        'Electronics': (50, 2000),
        'Clothing': (20, 200),
        'Food': (5, 100),
        'Home': (30, 500),
        'Books': (10, 50)
    }
    
    data = []
    for i in range(n_transactions):
        category = np.random.choice(list(products.keys()))
        product = np.random.choice(products[category])
        price_range = prices[category]
        
        transaction = {
            'transaction_id': f'T{i:06d}',
            'customer_id': f'C{np.random.randint(1, n_customers):04d}',
            'date': datetime.now() - timedelta(days=np.random.randint(0, 365)),
            'category': category,
            'product': product,
            'quantity': np.random.poisson(2) + 1,
            'unit_price': round(np.random.uniform(*price_range), 2),
            'day_of_week': np.random.choice(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']),
            'promotion': np.random.choice([True, False], p=[0.2, 0.8])
        }
        transaction['total_amount'] = round(transaction['quantity'] * transaction['unit_price'], 2)
        data.append(transaction)
    
    return pd.DataFrame(data)


def create_fraud_detection_data():
    """Create credit card fraud detection dataset"""
    
    n_transactions = 10000
    fraud_rate = 0.02
    
    data = []
    for i in range(n_transactions):
        is_fraud = np.random.random() < fraud_rate
        
        if is_fraud:
            # Fraudulent transaction patterns
            amount = np.random.exponential(500)
            hour = np.random.choice([2, 3, 4, 23])  # Unusual hours
            location_risk = np.random.choice(['High', 'Medium'], p=[0.7, 0.3])
            merchant_risk = np.random.choice(['New', 'Suspicious'], p=[0.6, 0.4])
            velocity = np.random.randint(5, 20)  # Many transactions quickly
        else:
            # Normal transaction patterns
            amount = np.random.gamma(2, 50)
            hour = np.random.choice(range(6, 22))  # Normal hours
            location_risk = np.random.choice(['Low', 'Medium', 'High'], p=[0.7, 0.25, 0.05])
            merchant_risk = np.random.choice(['Known', 'New'], p=[0.8, 0.2])
            velocity = np.random.randint(1, 5)
        
        transaction = {
            'transaction_id': f'TXN{i:06d}',
            'card_id': f'CARD{np.random.randint(1, 2000):04d}',
            'amount': round(amount, 2),
            'hour': hour,
            'location_risk': location_risk,
            'merchant_risk': merchant_risk,
            'transactions_today': velocity,
            'international': np.random.choice([True, False], p=[0.1, 0.9] if not is_fraud else [0.4, 0.6]),
            'online': np.random.choice([True, False], p=[0.3, 0.7] if not is_fraud else [0.7, 0.3]),
            'is_fraud': int(is_fraud)
        }
        data.append(transaction)
    
    return pd.DataFrame(data)


def create_spotify_data():
    """Create Spotify-style music listening data"""
    
    artists = ['Taylor Swift', 'Drake', 'The Weeknd', 'Bad Bunny', 'Ed Sheeran',
               'Ariana Grande', 'Post Malone', 'Billie Eilish', 'Justin Bieber', 'Dua Lipa']
    genres = ['Pop', 'Hip-Hop', 'Rock', 'Electronic', 'R&B', 'Country', 'Latin', 'Indie']
    moods = ['Happy', 'Sad', 'Energetic', 'Calm', 'Focused', 'Party', 'Romantic', 'Motivational']
    
    n_songs = 1000
    data = []
    
    for i in range(n_songs):
        song = {
            'song_id': f'S{i:04d}',
            'artist': np.random.choice(artists),
            'genre': np.random.choice(genres),
            'duration_seconds': np.random.randint(120, 360),
            'tempo_bpm': np.random.randint(60, 180),
            'energy': np.random.random(),
            'danceability': np.random.random(),
            'valence': np.random.random(),  # Musical positivity
            'acousticness': np.random.random(),
            'mood': np.random.choice(moods),
            'play_count': int(np.random.exponential(1000)),
            'skip_rate': np.random.beta(2, 5),  # Most songs not skipped
            'added_to_playlist': np.random.choice([True, False], p=[0.3, 0.7]),
            'release_year': np.random.randint(2015, 2024)
        }
        data.append(song)
    
    return pd.DataFrame(data)


def create_weather_data():
    """Create weather pattern dataset"""
    
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
              'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
    
    data = []
    for city in cities:
        for day in range(365):
            date = datetime(2023, 1, 1) + timedelta(days=day)
            
            # Seasonal patterns
            season_factor = np.sin(2 * np.pi * day / 365)
            
            record = {
                'city': city,
                'date': date,
                'temperature': 60 + 30 * season_factor + np.random.normal(0, 10),
                'humidity': 50 + 20 * np.random.random(),
                'precipitation': max(0, np.random.normal(0.1, 0.5)),
                'wind_speed': abs(np.random.normal(10, 5)),
                'conditions': np.random.choice(['Sunny', 'Cloudy', 'Rainy', 'Stormy'],
                                             p=[0.4, 0.3, 0.2, 0.1]),
                'uv_index': max(0, min(11, np.random.normal(6, 2)))
            }
            data.append(record)
    
    df = pd.DataFrame(data)
    df['temperature'] = df['temperature'].round(1)
    df['humidity'] = df['humidity'].round(0)
    df['precipitation'] = df['precipitation'].round(2)
    df['wind_speed'] = df['wind_speed'].round(1)
    df['uv_index'] = df['uv_index'].round(0)
    
    return df


def create_movie_ratings_data():
    """Create movie recommendation dataset"""
    
    movies = [
        'The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction',
        'Forrest Gump', 'Inception', 'The Matrix', 'Interstellar', 'Parasite', 'The Avengers',
        'Titanic', 'Jurassic Park', 'Star Wars', 'The Lion King', 'Toy Story'
    ]
    
    genres_map = {
        'The Shawshank Redemption': ['Drama'],
        'The Godfather': ['Crime', 'Drama'],
        'The Dark Knight': ['Action', 'Thriller'],
        'Pulp Fiction': ['Crime', 'Drama'],
        'Forrest Gump': ['Drama', 'Romance'],
        'Inception': ['Sci-Fi', 'Thriller'],
        'The Matrix': ['Sci-Fi', 'Action'],
        'Interstellar': ['Sci-Fi', 'Drama'],
        'Parasite': ['Thriller', 'Drama'],
        'The Avengers': ['Action', 'Adventure'],
        'Titanic': ['Romance', 'Drama'],
        'Jurassic Park': ['Adventure', 'Sci-Fi'],
        'Star Wars': ['Sci-Fi', 'Adventure'],
        'The Lion King': ['Animation', 'Family'],
        'Toy Story': ['Animation', 'Comedy']
    }
    
    n_users = 500
    n_ratings = 5000
    
    data = []
    for i in range(n_ratings):
        movie = np.random.choice(movies)
        
        rating = {
            'user_id': f'U{np.random.randint(1, n_users):04d}',
            'movie': movie,
            'genres': ', '.join(genres_map[movie]),
            'rating': min(5, max(1, np.random.normal(3.7, 1.0))),
            'timestamp': datetime.now() - timedelta(days=np.random.randint(0, 730)),
            'watch_time_percent': min(100, max(0, np.random.normal(75, 25)))
        }
        data.append(rating)
    
    df = pd.DataFrame(data)
    df['rating'] = df['rating'].round(1)
    df['watch_time_percent'] = df['watch_time_percent'].round(0)
    
    return df


def create_social_media_data():
    """Create social media sentiment analysis dataset"""
    
    platforms = ['Twitter', 'Instagram', 'Facebook', 'TikTok', 'LinkedIn']
    topics = ['Technology', 'Sports', 'Politics', 'Entertainment', 'Business', 'Health', 'Education']
    
    # Sample posts with sentiment
    positive_words = ['amazing', 'excellent', 'love', 'great', 'wonderful', 'fantastic', 'best']
    negative_words = ['terrible', 'awful', 'hate', 'worst', 'horrible', 'disappointing', 'bad']
    neutral_words = ['okay', 'fine', 'average', 'normal', 'regular', 'standard', 'typical']
    
    n_posts = 2000
    data = []
    
    for i in range(n_posts):
        sentiment = np.random.choice(['Positive', 'Negative', 'Neutral'], p=[0.4, 0.2, 0.4])
        
        if sentiment == 'Positive':
            words = np.random.choice(positive_words, 3)
        elif sentiment == 'Negative':
            words = np.random.choice(negative_words, 3)
        else:
            words = np.random.choice(neutral_words, 3)
        
        post = {
            'post_id': f'POST{i:05d}',
            'platform': np.random.choice(platforms),
            'topic': np.random.choice(topics),
            'text_length': np.random.randint(20, 280),
            'likes': int(np.random.exponential(100)),
            'shares': int(np.random.exponential(20)),
            'comments': int(np.random.exponential(10)),
            'hashtags': np.random.randint(0, 10),
            'mentions': np.random.randint(0, 5),
            'sentiment': sentiment,
            'engagement_rate': np.random.random(),
            'verified_account': np.random.choice([True, False], p=[0.1, 0.9]),
            'sample_text': f"This is {' '.join(words)} content about {np.random.choice(topics).lower()}"
        }
        data.append(post)
    
    return pd.DataFrame(data)


def save_all_datasets():
    """Save all datasets to CSV files"""
    
    datasets = {
        'mystery_shopper': create_mystery_shopper_data(),
        'netflix_viewing': create_netflix_dataset(),
        'covid_healthcare': create_covid_healthcare_data(),
        'retail_transactions': create_retail_transaction_data(),
        'fraud_detection': create_fraud_detection_data(),
        'spotify_music': create_spotify_data(),
        'weather_patterns': create_weather_data(),
        'movie_ratings': create_movie_ratings_data(),
        'social_media': create_social_media_data()
    }
    
    # Create datasets directory if it doesn't exist
    os.makedirs('datasets', exist_ok=True)
    
    for name, df in datasets.items():
        filename = f'datasets/{name}_data.csv'
        df.to_csv(filename, index=False)
        print(f"✅ Saved {name}_data.csv ({len(df)} rows)")
    
    # Create a metadata file
    metadata = {
        'created_date': datetime.now().isoformat(),
        'datasets': {name: {'rows': len(df), 'columns': len(df.columns)} 
                    for name, df in datasets.items()}
    }
    
    with open('datasets/metadata.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print("\n📊 All datasets created successfully!")
    return datasets


if __name__ == "__main__":
    # Generate and save all datasets
    all_datasets = save_all_datasets()
    
    # Display sample of each dataset
    print("\n" + "="*50)
    print("DATASET SAMPLES")
    print("="*50)
    
    for name, df in all_datasets.items():
        print(f"\n📌 {name.upper().replace('_', ' ')}")
        print(f"Shape: {df.shape}")
        print(df.head(3))
        print("-"*30)