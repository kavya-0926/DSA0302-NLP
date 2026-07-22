from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "Python is a programming language",
    "Machine learning uses Python",
    "Python is used in NLP"
]

vectorizer = TfidfVectorizer()

tfidf = vectorizer.fit_transform(documents)

print("Feature Names:")
print(vectorizer.get_feature_names_out())

print("\nTF-IDF Matrix:")
print(tfidf.toarray())