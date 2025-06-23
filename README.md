## NLP Analysis on News Headlines

This project applies text preprocessing, vectorization, sentiment analysis, and topic modeling techniques to news headlines. The goal is to extract meaningful structures from the text and observe the effects of natural language processing methods on news data.

## Project Overview

This project performs advanced NLP analyses on **209,527 news headlines** from the **Kaggle News Category Dataset**. The analyses include:

- **Sentiment Analysis** (with TextBlob)
- **Topic Modeling** (LDA and NMF algorithms)
- **Text Preprocessing** (enhanced with POS tagging)
- **Feature Engineering** (TF-IDF vectorization)

## Features

- **Multi-Algorithm Topic Modeling**: Both LDA and NMF are applied
- **Advanced Text Processing**: Improved accuracy with POS tagging
- **Comprehensive Sentiment Analysis**: Headlines are classified as Positive/Negative/Neutral
- **Scalable Pipeline**: Efficiently processes 200K+ documents
- **Comparative Analysis**: Algorithms are evaluated side by side

## Dataset

- **Source**: [Kaggle News Category Dataset v3](https://www.kaggle.com/datasets/rmisra/news-category-dataset)
- **Size**: 209,527 news headlines
- **Language**: English
- **Period**: Modern news media (2016-2020)
- **Format**: JSON Lines

## Setup

### Requirements
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**

git clone https://github.com/yourusername/news-nlp-analysis.git
cd news-nlp-analysis

2. **Create a virtual environment**

python3 -m venv nlp_env
source nlp_env/bin/activate  # Windows: nlp_env\Scripts\activate

3. **Install dependencies**


pip install -r requirements.txt


4. **Download the dataset**
   - Download the `News_Category_Dataset_v3.json` file from [Kaggle](https://www.kaggle.com/datasets/rmisra/news-category-dataset)
   - Place it in the project root directory

-----

## **Dataset Analysis**

# **Dataset Properties:**
- **Source:** Kaggle News Category Dataset v3
- **Total Records:** 209,527 news headlines
- **Language:** English
- **Time Range:** Modern news media (2016-2020)
- **Data Quality:** Clean, almost no missing data

# **Dataset Distribution Insights:**
The dataset offers a balanced distribution from American media, covering politics, lifestyle, technology, and entertainment.

-----

##  **Text Preprocessing Pipeline Analysis**

# Applied Preprocessing Techniques:

In natural language processing, the text must first be cleaned and simplified to be properly represented. This flow simplifies and enriches the text, making it ready for analysis. The steps applied in this project are as follows:

1. Lowercasing: 
   Ensures that different forms of the same word ("News" and "news") are unified.

2. Removal of punctuation and numbers:  
   Punctuation marks and numbers are removed as they usually do not carry meaning in most analyses.

3. Tokenization: 
   Headlines are split into words to enable word-based analysis.

4. Stopword removal: 
   Frequently occurring words that do not carry meaning ("the", "and", "is") are removed.

5. Lemmatization:
   Words are reduced to their root forms so that similar words are evaluated in a unified way ("running" → "run").

6. POS (Part-of-Speech) tagging:  
   The type of each word (noun, verb, adjective, etc.) is determined and this information is added to the words to enrich the text representation ("run_VB").

This order is designed with the logic of simplify → add meaning → enrich. Each step provides suitable data for the next step.

-----

## **Comparison of Vectorization Methods**

1. CountVectorizer (Bag-of-Words):
   Converts text into a numerical form based on word frequencies. The method is simple and fast but does not consider the importance of the word in context.

2. TF-IDF (Term Frequency – Inverse Document Frequency): 
   Considers both the frequency of the word in the document and its prevalence in the dataset. Assigns higher weights to more distinctive words.

Both methods were used on POS-tagged texts to obtain more detailed representations.

-----

## **Sentiment Analysis Evaluation**

Sentiment analysis was performed using the TextBlob library, and news headlines were classified as Positive, Negative, or Neutral.

# TextBlob Results:

Neutral:   126,829 (60.7%)
Positive:   58,739 (28.1%)
Negative:   23,959 (11.4%)

# Evaluation:  

It is expected that most news texts remain neutral. Positive headlines are generally found in lifestyle and culture news, while negative ones are mostly seen in political and crisis-related headlines.

-----

## **In-Depth Topic Modeling Analysis**

Using LDA (Latent Dirichlet Allocation) and NMF (Non-negative Matrix Factorization), headlines were semantically clustered. Key words and themes:

LDA Output:

- Topic 1: trump, woman, health, clinton → Politics and social themes  
- Topic 2: trump, say, photo, video, new → Media-related political headlines  
- Topic 3: day, way, year, new, photo → Time-based lifestyle news  
- Topic 4: photo, new, best, food, week → Lifestyle and content suggestions  
- Topic 5: trump, new, photo, donald, video → Trump agenda and media

NMF Output:

- Topic 1: photo, best, world, home, style → Style, culture, life  
- Topic 2: trump, donald, clinton, say → American politics  
- Topic 3: new, year, york, resolution, time → New year and city life  
- Topic 4: day, way, thing, life, one → Personal content and comments  
- Topic 5: woman, week, tweet, funniest, parent → Humor and parenting

LDA produces broader and overlapping topic clusters, while NMF reveals sharper and more distinct topics.

-----

## **Algorithm Performance Comparison**

LDA vs NMF Analysis:

# LDA Strengths:
- Probabilistic modeling approach
- Models transitions between topics
- Provides document-topic distribution

# NMF Advantages:
- Clearer topic separation
- Interpretability due to non-negativity constraint
- More distinct topic boundaries

## General Evaluation

- Although the headlines are short and provide limited context, the preprocessing steps made the texts suitable for analysis.  
- When TF-IDF and POS tagging are used together, topic modeling results become more distinguishable.  
- The sentiment analysis output shows that the neutral class is dominant, which is in line with the generally impartial nature of news language.  
- LDA and NMF outputs could be interpreted with meaningful topic titles and revealed comparable differences.

## Used Libraries

- pandas  
- numpy
- nltk  
- scikit-learn  
- textblob  
- re

## Authors

- Bilgesu Miray Karakoç  
- Esra Kaya  
- Zeynep Öztürk
