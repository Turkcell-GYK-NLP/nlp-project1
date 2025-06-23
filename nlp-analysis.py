import pandas as pd
import nltk
import re
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from textblob import TextBlob
from sklearn.decomposition import LatentDirichletAllocation, NMF

# Step 1: Download required NLTK datasets
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

# Step 2: Load the dataset (json file should be in the same folder)
df = pd.read_json("News_Category_Dataset_v3.json", lines=True)
df = df[['headline', 'category']].dropna().reset_index(drop=True)

# Step 3: Clean and prepare text for processing
def preprocess(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\d+', '', text)  # Remove numbers
    tokens = word_tokenize(text)  # Split into words
    stop_words = set(stopwords.words('english'))  # Stop words list (the, is, and...)
    tokens = [word for word in tokens if word not in stop_words]  # Remove stop words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]  # Reduce to root forms
    return tokens

df['tokens'] = df['headline'].apply(preprocess)

# Step 4: Convert token list back to string
df['clean_text'] = df['tokens'].apply(lambda x: ' '.join(x))

# Step 5: Vectorization (BoW and TF-IDF)
count_vectorizer = CountVectorizer()
X_count = count_vectorizer.fit_transform(df['clean_text'])  # BoW representation

tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(df['clean_text'])  # TF-IDF representation

# Step 6: POS Tagging (assign part-of-speech tags to each word)
def tag_pos(tokens):
    return nltk.pos_tag(tokens)  # Example: [('dog', 'NN'), ('runs', 'VBZ')]

df['pos_tags'] = df['tokens'].apply(tag_pos)

# Generate tokens enriched with POS information
def tokens_with_pos(pairs):
    return [f"{word}_{pos}" for word, pos in pairs]

df['tokens_pos'] = df['pos_tags'].apply(tokens_with_pos)
df['clean_text_pos'] = df['tokens_pos'].apply(lambda x: ' '.join(x))  # String in word_POS format

# TF-IDF: Based on POS-enhanced text
tfidf_pos = TfidfVectorizer()
X_tfidf_pos = tfidf_pos.fit_transform(df['clean_text_pos'])  # TF-IDF with POS information

# Step 7: Sentiment Analysis (TextBlob)
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment'] = df['headline'].apply(get_sentiment)

# Step 8: Topic Modeling (LDA & NMF)
lda = LatentDirichletAllocation(n_components=5, random_state=42)
lda.fit(X_tfidf_pos)  # Train LDA model with POS-enhanced representation

nmf = NMF(n_components=5, random_state=42)
nmf.fit(X_tfidf_pos)

# Function to display topics
def display_topics(model, feature_names, no_top_words=5):
    topics = []
    for topic_idx, topic in enumerate(model.components_):
        top_words = [feature_names[i].split('_')[0] for i in topic.argsort()[:-no_top_words - 1:-1]]
        topics.append(f"Topic {topic_idx+1}: {', '.join(top_words)}")
    return topics

print("\nLDA Topics:")
print('\n'.join(display_topics(lda, tfidf_pos.get_feature_names_out())))

print("\nNMF Topics:")
print('\n'.join(display_topics(nmf, tfidf_pos.get_feature_names_out())))

# Step 9: Sample output - Sentiment distribution
print("\nSample Sentiment Counts:")
print(df['sentiment'].value_counts())