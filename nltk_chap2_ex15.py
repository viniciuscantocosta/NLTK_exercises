import nltk
from nltk.corpus import brown

fd = nltk.FreqDist(word.lower() for word in brown.words())

answer = [word for word in brown.words() if fd[word] >= 3]

print(answer)