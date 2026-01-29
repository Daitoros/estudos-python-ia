import pandas as pd
df = pd.read_csv('C:/Users/davix/Desktop/Arquivos/Profissional/Estudos/Análise de dados/amazon_cells_labelled.txt', names=['review', 'sentiment'], sep='\t')

#Dividindo conjunto em amostra e em teste
from sklearn.model_selection import train_test_split 
reviews = df['review'].values
sentiments = df['sentiment'].values
reviews_train, reviews_test, sentiment_train, sentiment_test = train_test_split(reviews, sentiments, test_size=0.2, random_state=500)

#Transformando texto em vetor de features numéricas

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
vectorizer.fit(reviews)
X_train = vectorizer.transform(reviews_train)
X_test = vectorizer.transform(reviews_test)

#Classificador e treino do modelo

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, sentiment_train)


#Testando Acurácia

accuracy = classifier.score(X_test, sentiment_test)
print("Accuracy:", accuracy)